import ollama

# Streaming chat
stream = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Tell me a story'
        }
    ],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='')
