import ollama

# Generate text
response = ollama.generate(
    model='phi4-mini',
    prompt='Write a haiku about coding'
)

print(response['response'])
