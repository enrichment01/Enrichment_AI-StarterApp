import ollama

text = "Your text here..."
analysis_type = "Summarize"

prompt = f"Summarize the following text concisely:\n\n{text}"

response = ollama.generate(
    model='llama2',
    prompt=prompt,
    options={'temperature': 0.3}
)

print(response['response'])
