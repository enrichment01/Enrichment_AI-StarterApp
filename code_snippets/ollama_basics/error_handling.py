import ollama

try:
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'user',
                'content': 'Hello!'
            }
        ]
    )
    print(response['message']['content'])
    
except ollama.ResponseError as e:
    print(f"Error: {e.error}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
