import ollama

# Simple chat
response = ollama.chat(
    model='phi4-mini',
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?'
        }
    ]
)

print(response['message']['content'])
