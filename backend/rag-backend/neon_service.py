import os
import psycopg2
from psycopg2.extras import execute_values
from pgvector.psycopg2 import register_vector
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv(override=True)

class NeonService:
    def __init__(self, dimension: int = 1024):
        self.dimension = dimension
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            print("Warning: DATABASE_URL not found in environment variables. NeonService will not be functional.")
            self.conn = None
            return

        try:
            self.conn = psycopg2.connect(self.database_url)
            self._prepare_database()
            print("Successfully connected to Neon/Postgres.")
        except Exception as e:
            print(f"Error connecting to Neon: {e}")
            self.conn = None

    def _prepare_database(self):
        """Ensures pgvector extension and table exist."""
        if not self.conn:
            return
        
        with self.conn.cursor() as cur:
            # Enable pgvector extension
            cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            
            # Create table for embeddings
            cur.execute(f"""
                CREATE TABLE IF NOT EXISTS document_embeddings (
                    id SERIAL PRIMARY KEY,
                    content TEXT,
                    embedding vector({self.dimension}),
                    metadata JSONB
                );
            """)
            self.conn.commit()
            register_vector(self.conn)

    def upsert_vectors(self, vectors: List[List[float]], payloads: List[Dict[str, Any]]):
        """Inserts vectors and their associated payloads into the database."""
        if not self.conn:
            print("NeonService: Connection not established.")
            return

        data = []
        for vec, payload in zip(vectors, payloads):
            content = payload.get("text", "")
            data.append((content, vec, payload))

        with self.conn.cursor() as cur:
            execute_values(cur, 
                "INSERT INTO document_embeddings (content, embedding, metadata) VALUES %s", 
                data
            )
            self.conn.commit()
        print(f"Inserted {len(vectors)} vectors into Neon.")

    def search_vectors(self, query_vector: List[float], limit: int = 5) -> List[Dict[str, Any]]:
        """Performs a vector similarity search."""
        if not self.conn:
            print("NeonService: Connection not established.")
            return []

        results = []
        try:
            with self.conn.cursor() as cur:
                # Use <-> operator for L2 distance, or <=> for cosine distance
                # Docusaurus context usually uses cosine distance for embeddings
                cur.execute("""
                    SELECT content, metadata, embedding <=> %s AS distance
                    FROM document_embeddings
                    ORDER BY distance ASC
                    LIMIT %s;
                """, (query_vector, limit))
                
                rows = cur.fetchall()
                for row in rows:
                    results.append({
                        "payload": {"text": row[0], **(row[1] or {})},
                        "score": float(row[2])
                    })
        except Exception as e:
            print(f"Error searching vectors in Neon: {e}")
            
        return results

    def close(self):
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    # Simple test (requires DATABASE_URL)
    service = NeonService()
    if service.conn:
        test_vec = [0.1] * 1536
        service.upsert_vectors([test_vec], [{"text": "Testing Neon integration", "source": "test"}])
        res = service.search_vectors(test_vec, limit=1)
        print(f"Search result: {res}")
        service.close()
