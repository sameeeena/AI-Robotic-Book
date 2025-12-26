import os
from neon_service import NeonService
from dotenv import load_dotenv

load_dotenv(override=True)

def test_neon():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("Error: DATABASE_URL not found in .env file.")
        return

    print(f"Connecting to Neon at: {db_url.split('@')[-1]}") # Print host only for safety
    
    try:
        service = NeonService()
        if service.conn:
            print("Connection successful!")
            
            # Test upsert
            test_vec = [0.1] * 1536
            test_payload = {"text": "Neon test successful", "type": "test"}
            print("Testing upsert...")
            service.upsert_vectors([test_vec], [test_payload])
            
            # Test search
            print("Testing search...")
            results = service.search_vectors(test_vec, limit=1)
            if results:
                print(f"Search successful! Result: {results[0]['payload']['text']}")
            else:
                print("Search failed to return results.")
                
            service.close()
        else:
            print("Failed to initialize NeonService (connection might have failed).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    test_neon()
