import requests
import json

url = "http://localhost:8000/chat"
data = {"user_message": "What is the Robotic Nervous System in ROS 2?"}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
