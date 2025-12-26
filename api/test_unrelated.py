from openai_service import get_chat_completion

messages = [
    {"role": "system", "content": "You are an expert assistant on Physical AI and Humanoid Robotics. Answer the user's questions truthfully and concisely, based on the provided context. If the answer is not in the context, state that you don't have enough information."},
    {"role": "user", "content": "What is the capital of France?"}
]

print("Testing with unrelated question...")
response = get_chat_completion(messages)
print(f"Response: {response}")
