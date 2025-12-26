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
try:
    embedding_service = CohereService()
except Exception as e:
    print(f"Warning: Failed to initialize CohereService: {e}")
    embedding_service = None

# Initialize Vector Service
# Priority: Qdrant > Neon > FAISS
vector_service = None
try:
    if os.getenv("QDRANT_URL"):
        vector_service = QdrantService(dimension=1024)
        print("Backend using Qdrant for vector storage.")
    elif os.getenv("DATABASE_URL"):
        vector_service = NeonService(dimension=1024)
        print("Backend using Neon for vector storage.")
    else:
        # FAISS might fail if writing to disk is restricted in Vercel (read-only filesystem usually)
        # But we can try using /tmp or just in-memory if we modified FaissService
        # For now, let's try standard initialization.
        vector_service = FaissService(dimension=1024)
        print("Backend using FAISS for vector storage.")
except Exception as e:
    print(f"Warning: Failed to initialize Vector Service: {e}")
    vector_service = None

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
    if not embedding_service:
        raise HTTPException(status_code=503, detail="Embedding service is not available (check API keys).")
    if not vector_service:
        raise HTTPException(status_code=503, detail="Vector service is not available.")

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
    return {"message": "Welcome to the RAG Backend API with Cohere and Qdrant/Neon.", 
            "status": {
                "embedding_service": "Active" if embedding_service else "Inactive",
                "vector_service": "Active" if vector_service else "Inactive"
            }}

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

    # Graceful fallback if services are missing
    if not embedding_service:
        return ChatResponse(response="I am currently unable to search my knowledge base because the Embedding Service is not configured (missing API keys). However, I can still try to answer generally if you like.")
    
    if not vector_service:
        return ChatResponse(response="I am unable to access my memory (Vector Database) at the moment. Please check the server configuration.")

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
