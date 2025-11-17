import ollama

try:
    # List available models
    models = ollama.list()
    
    print("✅ Ollama is running!")
    print(f"Models: {len(models['models'])}")
    
    for model in models['models']:
        print(f"- {model['name']}")
        
except Exception as e:
    print(f"❌ Error: {e}")
