import requests
import json

r = requests.get("http://localhost:11434/api/tags", timeout=600)

data = r.json()

print(data)
