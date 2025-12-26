import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv("OPENAI_ENDPOINT_API_KEY")
print(f"API Key found: {api_key[:10] if api_key else 'None'}...")

base_url = "https://openrouter.ai/api/v1"

client = OpenAI(api_key=api_key, base_url=base_url)

try:
    response = client.embeddings.create(
        input=["Hello, world!"],
        model="openai/text-embedding-3-small"
    )
    print(f"Success! Embedding size: {len(response.data[0].embedding)}")
except Exception as e:
    print(f"Error: {e}")
