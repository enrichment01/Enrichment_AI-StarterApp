import ollama

response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Write a creative story'
        }
    ],
    options={
        'temperature': 0.8,  # Higher = more creative
        'top_p': 0.9,        # Nucleus sampling
        'top_k': 40,         # Top-k sampling
        'num_predict': 100,  # Max tokens to generate
    }
)
