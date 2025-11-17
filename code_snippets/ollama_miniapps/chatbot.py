import ollama

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

stream = ollama.chat(
    model='llama2',
    messages=messages,
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='')
