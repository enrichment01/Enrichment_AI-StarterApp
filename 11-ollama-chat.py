import ollama

r = ollama.chat(model="phi4", messages=[{"role":"user","content":"Sag Hallo"}])

print(r["message"]["content"])