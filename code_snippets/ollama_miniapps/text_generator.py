import ollama

prompt = "Write a short story about a robot"
model = "llama2"
temperature = 0.7

response = ollama.generate(
    model=model,
    prompt=prompt,
    options={
        'temperature': temperature,
        'num_predict': 200,
    }
)

print(response['response'])
