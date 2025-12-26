from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Dict, Any
from openai_service import get_chat_completion # Still using OpenAI/OpenRouter for LLM
from cohere_service import CohereService
from qdrant_service import QdrantService
from neon_service import NeonService
from faiss_service import FaissService
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
import traceback

# Load environment variables from .env file
load_dotenv(override=True)

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000", # Docusaurus default port
    "http://127.0.0.1:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Embedding Service (Cohere)
embedding_service = CohereService()

# Initialize Vector Service
# Priority: Qdrant > Neon > FAISS
if os.getenv("QDRANT_URL"):
    vector_service = QdrantService(dimension=1024)
    print("Backend using Qdrant for vector storage.")
elif os.getenv("DATABASE_URL"):
    vector_service = NeonService(dimension=1024)
    print("Backend using Neon for vector storage.")
else:
    vector_service = FaissService(dimension=1024)
    print("Backend using FAISS for vector storage.")

class Document(BaseModel):
    text: str
    embedding: List[float] = None # Embedding can be generated if not provided

class EmbeddingRequest(BaseModel):
    text: str

class EmbeddingResponse(BaseModel):
    embedding: List[float]

@app.post("/embed", response_model=EmbeddingResponse)
async def create_embedding(request: EmbeddingRequest):
    """
    Generates a Cohere embedding for the given text and stores it in the vector database.
    """
    try:
        embedding = embedding_service.get_embedding(request.text, input_type="search_document")
        if not embedding:
            raise HTTPException(status_code=500, detail="Failed to generate embedding.")
        
        # Store in vector database
        vector_service.upsert_vectors(vectors=[embedding], payloads=[{"text": request.text}])

        return EmbeddingResponse(embedding=embedding)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        traceback.print_exc() # Print traceback
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the RAG Backend API with Cohere and Qdrant/Neon."}

class ChatRequest(BaseModel):
    user_message: str = None
    query: str = None
    message: str = None

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def handle_chat(request: ChatRequest):
    """
    Handles a user's chat query, retrieves relevant documents,
    and provides an answer.
    """
    user_query = request.user_message or request.query or request.message
    
    if not user_query:
        raise HTTPException(status_code=400, detail="No message or query provided.")

    print(f"Received query: {user_query}")

    try:
        query_embedding = embedding_service.get_embedding(user_query, input_type="search_query")
        if not query_embedding:
            raise HTTPException(status_code=500, detail="Failed to generate embedding for query.")
        
        search_results = vector_service.search_vectors(query_embedding, limit=3)
        print(f"Search results: {search_results}")
        
        messages = [
            {"role": "system", "content": "You are an expert assistant on Physical AI and Humanoid Robotics. Answer the user's questions truthfully and concisely, based on the provided context. If the answer is not in the context, state that you don't have enough information."},
        ]

        if search_results:
            retrieved_texts = [result['payload']['text'] for result in search_results if 'payload' in result and 'text' in result['payload']]
            print(f"Retrieved {len(retrieved_texts)} contexts.")
            context = "\n\n".join(retrieved_texts)
            messages.append({"role": "user", "content": f"Context: {context}\n\nQuestion: {user_query}"})
        else:
            messages.append({"role": "user", "content": user_query})
        
        answer = get_chat_completion(messages)
        
        return ChatResponse(response=answer)
    except Exception as e:
        import logging
        logging.basicConfig(filename='backend_service.log', level=logging.ERROR, 
                            format='%(asctime)s %(levelname)s:%(message)s')
        logging.error(f"Unhandled error in /chat endpoint: {e}")
        
        traceback.print_exc() # Print traceback
        raise HTTPException(status_code=500, detail=f"An error occurred during chat retrieval: {e}")
