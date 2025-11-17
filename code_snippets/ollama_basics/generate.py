import ollama

# Generate text
response = ollama.generate(
    model='llama2',
    prompt='Write a haiku about coding'
)

print(response['response'])
