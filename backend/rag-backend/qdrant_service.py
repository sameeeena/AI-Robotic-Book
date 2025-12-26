import os
import uuid
from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv(override=True)

class QdrantService:
    def __init__(self, collection_name: str = None, dimension: int = 1024):
        self.url = os.getenv("QDRANT_URL")
        self.api_key = os.getenv("QDRANT_API_KEY")
        self.collection_name = collection_name or os.getenv("COLLECTION_NAME", "Humanoid-robotic-book")
        self.dimension = dimension

        if not self.url:
            print("Warning: QDRANT_URL not found. QdrantService will not be functional.")
            self.client = None
            return

        self.client = QdrantClient(url=self.url, api_key=self.api_key)
        self._ensure_collection()

    def _ensure_collection(self):
        if not self.client:
            return
        
        collections = self.client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)

        if not exists:
            print(f"Creating collection: {self.collection_name}")
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(size=self.dimension, distance=models.Distance.COSINE),
            )
        else:
            print(f"Collection {self.collection_name} already exists.")

    def upsert_vectors(self, vectors: List[List[float]], payloads: List[Dict[str, Any]]):
        if not self.client:
            return

        points = [
            models.PointStruct(
                id=str(uuid.uuid4()), 
                vector=vector, 
                payload=payload
            ) for vector, payload in zip(vectors, payloads)
        ]
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        print(f"Upserted {len(vectors)} points into Qdrant.")

    def search_vectors(self, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        if not self.client:
            return []

        search_result = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit
        ).points

        results = []
        for res in search_result:
            results.append({
                "payload": res.payload,
                "score": res.score
            })
        return results