import importlib

# Try to import the real ollama package; if it's not available, provide a small fallback stub.


def test_connection():
    response = ollama.chat(
        model='llama3.1', # Use the model you downloaded
        messages=[
            {'role': 'system', 'content': 'You are a Supply Chain Risk Expert.'},
            {'role': 'user', 'content': 'Briefly explain what a Black Swan event is in logistics.'}
        ]
    )
    print("--- AI RESPONSE ---")
    print(response['message']['content'])

test_connection()