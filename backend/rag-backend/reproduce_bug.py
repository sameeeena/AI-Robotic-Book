import requests
import json

def test_chat(payload):
    url = "http://localhost:8000/chat"
    try:
        response = requests.post(url, json=payload)
        print(f"Payload: {payload}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Test with user_message
    print("Testing with user_message...")
    test_chat({"user_message": "What is ROS 2?"})
    
    # Test with query
    print("\nTesting with query...")
    test_chat({"query": "What is ROS 2?"})

