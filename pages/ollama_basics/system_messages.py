import ollama

response = ollama.chat(
    model='phi4-mini',
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful coding assistant.'
        },
        {
            'role': 'user',
            'content': 'How do I reverse a string in Python?'
        }
    ]
)
