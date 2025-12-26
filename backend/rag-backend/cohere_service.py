import cohere
import os
from typing import List
from dotenv import load_dotenv

load_dotenv(override=True)

class CohereService:
    def __init__(self):
        self.api_key = os.getenv("COHERE_API_KEY")
        if not self.api_key:
            raise ValueError("COHERE_API_KEY not found in environment variables.")
        self.co = cohere.ClientV2(self.api_key)
        self.model = os.getenv("EMBED_MODEL", "embed-english-v3.0")

    def get_embeddings(self, texts: List[str], input_type: str = "search_query") -> List[List[float]]:
        """
        Generates embeddings for a list of texts using Cohere.
        input_type can be 'search_document' or 'search_query'.
        """
        import time
        import logging
        
        # Configure logging to file
        logging.basicConfig(filename='backend_service.log', level=logging.ERROR, 
                            format='%(asctime)s %(levelname)s:%(message)s')

        max_retries = 5
        for attempt in range(max_retries):
            try:
                response = self.co.embed(
                    texts=texts,
                    model=self.model,
                    input_type=input_type,
                    embedding_types=["float"]
                )
                return response.embeddings.float
            except Exception as e:
                logging.error(f"Cohere Embedding Attempt {attempt + 1} failed: {e}")
                import sys
                print(f"Error generating Cohere embeddings (Attempt {attempt + 1}): {e}", file=sys.stderr)
                
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt) # Exponential backoff
                else:
                    return []
        return []

    def get_embedding(self, text: str, input_type: str = "search_query") -> List[float]:
        embeddings = self.get_embeddings([text], input_type=input_type)
        return embeddings[0] if embeddings else []

if __name__ == '__main__':
    # Quick test
    service = CohereService()
    test_text = "Humanoid robots are the future of AI."
    emb = service.get_embedding(test_text)
    print(f"Embedding length: {len(emb)}")
    if emb:
        print(f"First 5 values: {emb[:5]}")
