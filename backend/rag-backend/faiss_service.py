import faiss
import numpy as np
import os
import pickle
from typing import List, Dict, Any

class FaissService:
    def __init__(self, dimension: int = 1536, index_path: str = "faiss_index.bin", payload_path: str = "payloads.pkl"):
        self.dimension = dimension
        self.index_path = index_path
        self.payload_path = payload_path
        
        if os.path.exists(index_path) and os.path.exists(payload_path):
            try:
                self.index = faiss.read_index(index_path)
                with open(payload_path, 'rb') as f:
                    self.payloads = pickle.load(f)
                print(f"Loaded existing FAISS index from {index_path}.")
            except Exception as e:
                print(f"Error loading FAISS index: {e}")
                self.index = faiss.IndexFlatL2(dimension)
                self.payloads = []
        else:
            self.index = faiss.IndexFlatL2(dimension)
            self.payloads = []
            print("Created new FAISS index.")

    def _save(self):
        try:
            faiss.write_index(self.index, self.index_path)
            with open(self.payload_path, 'wb') as f:
                pickle.dump(self.payloads, f)
            print("Saved FAISS index and payloads.")
        except Exception as e:
            print(f"Error saving FAISS index: {e}")

    def upsert_vectors(self, vectors: List[List[float]], payloads: List[Dict[str, Any]]):
        vectors_np = np.array(vectors, dtype='float32')
        self.index.add(vectors_np)
        self.payloads.extend(payloads)
        self._save()
        print(f"Upserted {len(vectors)} vectors into FAISS index.")

    def search_vectors(self, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        query_np = np.array([query_vector], dtype='float32')
        distances, indices = self.index.search(query_np, limit)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx != -1:
                results.append({
                    "payload": self.payloads[idx],
                    "score": float(distances[0][i])
                })
        return results

# Example Usage (for testing)
if __name__ == '__main__':
    faiss_service = FaissService()

    dummy_embeddings = [
        [0.1] * 1536,
        [0.2] * 1536,
        [0.3] * 1536,
    ]
    dummy_payloads = [
        {"text": "The quick brown fox jumps over the lazy dog."},
        {"text": "A robot is a machine."},
        {"text": "Humanoid robots are a type of robot."},
    ]

    faiss_service.upsert_vectors(dummy_embeddings, dummy_payloads)

    query_vector = [0.25] * 1536
    search_results = faiss_service.search_vectors(query_vector, limit=2)
    print("\nSearch Results:")
    for result in search_results:
        print(f"Score: {result['score']}, Text: {result['payload']['text']}")
