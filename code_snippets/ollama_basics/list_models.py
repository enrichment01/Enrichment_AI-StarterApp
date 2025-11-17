import ollama

# List all models
models = ollama.list()

for model in models['models']:
    print(f"Name: {model['name']}")
    print(f"Size: {model['size']}")
    print(f"Modified: {model['modified_at']}")
    print("---")
