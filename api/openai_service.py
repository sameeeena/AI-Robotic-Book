import os
from openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv(override=True)

class OpenAIProvider:
    """
    Manages the OpenAI client for various operations, including embeddings.
    Configurable to use Gemini API with OpenAI-compatible endpoint.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OpenAIProvider, cls).__new__(cls)
            
            # Prioritize OPENAI_ENDPOINT_API_KEY for OpenRouter (or similar OpenAI-compatible endpoint)
            api_key = os.getenv("OPENAI_ENDPOINT_API_KEY")
            base_url = os.getenv("GEMINI_API_BASE_URL", "https://openrouter.ai/api/v1") # Default to OpenRouter

            if not api_key:
                # Fallback to GEMINI_API_KEY if OPENAI_ENDPOINT_API_KEY is not set
                api_key = os.getenv("GEMINI_API_KEY")
                if not api_key:
                    raise ValueError("Neither OPENAI_ENDPOINT_API_KEY nor GEMINI_API_KEY environment variable is set.")
                # If falling back, base_url should probably be the Google one if not overridden
                if base_url == "https://openrouter.ai/api/v1": # If using default, but key is GEMINI_API_KEY
                    base_url = os.getenv("GEMINI_API_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")


            cls._instance.client = OpenAI(api_key=api_key, base_url=base_url)
            # Using a confirmed working model on OpenRouter
            cls._instance.embedding_model = "openai/text-embedding-3-small"
        return cls._instance

    def get_client(self):
        return self.client

    def get_embedding_model(self):
        return self.embedding_model

def get_openai_embedding(text: str) -> List[float]:
    """
    Generates an embedding for the given text using OpenAI's embedding model.
    Includes retry logic.
    """
    provider = OpenAIProvider()
    client = provider.get_client()
    embedding_model = provider.get_embedding_model()

    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.embeddings.create(
                input=[text],
                model=embedding_model
            )
            return response.data[0].embedding
        except Exception as e:
            import time
            import sys
            print(f"Embedding attempt {attempt + 1} failed: {e}", file=sys.stderr)
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                return []
    return []

def get_chat_completion(messages: List[Dict[str, str]], model: str = "openai/gpt-4o-mini") -> str:
    """
    Generates a chat completion using the OpenAI-compatible chat model.
    Includes retry logic for improved reliability.
    """
    provider = OpenAIProvider()
    client = provider.get_client()

    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            import time
            import traceback
            import logging
            import sys
            
            # Configure logging to file
            logging.basicConfig(filename='backend_service.log', level=logging.ERROR, 
                                format='%(asctime)s %(levelname)s:%(message)s')
            
            logging.error(f"OpenAI/Gemini Chat Attempt {attempt + 1} failed: {e}")
            print(f"Chat Attempt {attempt + 1} failed: {e}", file=sys.stderr)
            
            if attempt < max_retries - 1:
                sleep_time = 2 ** attempt # Exponential backoff: 1, 2, 4 seconds
                time.sleep(sleep_time)
            else:
                traceback.print_exc()
                return "I apologize, but I encountered an error (Backend Connection Issue) trying to generate a response. Please try again in a moment."

if __name__ == '__main__':
    # Example usage:
    # Set your API key as an environment variable (GEMINI_API_KEY or OPENAI_API_KEY)
    # and GEMINI_API_BASE_URL if using Gemini's OpenAI-compatible endpoint.
    try:
        embedding = get_openai_embedding("Hello, world!")
        print(f"Embedding for 'Hello, world!': {embedding[:5]}...") # Print first 5 elements
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    try:
        # Test with a different text
        embedding_robot = get_openai_embedding("Humanoid robots are fascinating.")
        print(f"Embedding for 'Humanoid robots are fascinating.': {embedding_robot[:5]}...")
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
