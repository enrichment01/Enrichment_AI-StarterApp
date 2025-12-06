import streamlit as st
import json

from lib.helper_streamlit import show_code


st.header("📋 Working with JSON — Python Basics")
st.markdown("Parsing, creating, and manipulating JSON data in Python.")

# Creating JSON from Python objects
st.subheader("Python to JSON")

python_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_active": True,
    "salary": None
}

json_string = json.dumps(python_data, indent=2)
st.write("**Python dict:**")
st.write(python_data)

st.write("**JSON string:**")
st.code(json_string, language="json")

# Parsing JSON
st.subheader("JSON to Python")

json_text = '''
{
    "product": "Laptop",
    "price": 999.99,
    "specs": {
        "cpu": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD"
    },
    "in_stock": true
}
'''

parsed_data = json.loads(json_text)
st.write("**Parsed data:**", parsed_data)
st.write("**Product name:**", parsed_data["product"])
st.write("**CPU:**", parsed_data["specs"]["cpu"])

# JSON formatting options
st.subheader("JSON Formatting Options")

data = {"name": "Bob", "scores": [85, 92, 78]}

# Compact format
compact = json.dumps(data)
st.write("**Compact:**", compact)

# Pretty format
pretty = json.dumps(data, indent=4, sort_keys=True)
st.write("**Pretty:**")
st.code(pretty, language="json")

# Working with JSON arrays
st.subheader("JSON Arrays")

users_json = '''
[
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
    {"id": 3, "name": "Charlie", "role": "User"}
]
'''

users = json.loads(users_json)
st.write("**Users list:**")
for user in users:
    st.write(f"- {user['name']} ({user['role']})")

# Nested JSON
st.subheader("Nested JSON Structures")

nested_json = {
    "company": "TechCorp",
    "employees": [
        {
            "name": "John",
            "department": "Engineering",
            "projects": ["Project A", "Project B"]
        },
        {
            "name": "Jane",
            "department": "Marketing",
            "projects": ["Campaign X"]
        }
    ]
}

st.write("**Nested structure:**")
st.json(nested_json)

# Error handling
st.subheader("Error Handling")

invalid_json = '{"name": "Test", invalid}'

try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    st.error(f"❌ JSON parsing error: {e}")

# Common JSON operations
st.subheader("Common Operations")

operations = {
    "json.dumps()": "Convert Python to JSON string",
    "json.loads()": "Parse JSON string to Python",
    "json.dump()": "Write JSON to file",
    "json.load()": "Read JSON from file"
}

for func, desc in operations.items():
    st.write(f"**{func}**: {desc}")
