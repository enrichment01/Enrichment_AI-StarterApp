import streamlit as st
import json

st.header("🔍 Response Parsing — Ollama Basics")
st.markdown("Extracting structured data from AI responses.")

# Overview
st.subheader("Why Parse Responses?")

st.write("""
AI models return text responses, but often you need structured data 
(JSON, lists, specific values) for your application. Response parsing 
helps extract and validate this structured information.
""")

# Basic parsing
st.subheader("📋 Basic Response Access")

basic_code = """
import ollama

# Generate response
response = ollama.generate(
    model='phi4-mini',
    prompt='What is Python?'
)

# Access different parts
full_response = response['response']          # The generated text
done = response['done']                       # Boolean: completed?
model = response['model']                     # Model name used
created_at = response['created_at']          # Timestamp
total_duration = response['total_duration']   # Time in nanoseconds

print(f"Response: {full_response}")
print(f"Duration: {total_duration / 1e9:.2f} seconds")
"""

st.code(basic_code, language="python")

# JSON parsing
st.subheader("📊 Parsing JSON Responses")

json_code = """
import json
import ollama

# Request JSON output
prompt = '''
Extract information from this text as JSON:
"John Doe, age 30, works as a Software Engineer in New York"

Output format:
{
    "name": "...",
    "age": ...,
    "occupation": "...",
    "location": "..."
}
'''

response = ollama.generate(model='phi4-mini', prompt=prompt)

# Parse JSON from response
try:
    # Extract JSON from response (might have extra text)
    text = response['response']
    
    # Find JSON portion
    start = text.find('{')
    end = text.rfind('}') + 1
    json_text = text[start:end]
    
    # Parse JSON
    data = json.loads(json_text)
    
    print(data['name'])        # "John Doe"
    print(data['age'])         # 30
    print(data['occupation'])  # "Software Engineer"
    
except json.JSONDecodeError:
    print("Failed to parse JSON")
except Exception as e:
    print(f"Error: {e}")
"""

st.code(json_code, language="python")

# List parsing
st.subheader("📝 Parsing Lists")

list_code = """
# Request a list
prompt = "List 5 programming languages. Output only the names, one per line."

response = ollama.generate(model='phi4-mini', prompt=prompt)
text = response['response']

# Parse into list
languages = [
    line.strip() 
    for line in text.split('\\n') 
    if line.strip()
]

print(languages)
# ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']

# Remove numbering if present
languages = [
    line.split('.', 1)[1].strip() if '.' in line else line.strip()
    for line in text.split('\\n')
    if line.strip()
]
"""

st.code(list_code, language="python")

# Structured extraction
st.subheader("🎯 Structured Data Extraction")

extraction_code = """
def extract_json_from_response(response_text):
    '''Extract JSON from response that might contain extra text'''
    
    # Try to find JSON object
    start = response_text.find('{')
    end = response_text.rfind('}') + 1
    
    if start != -1 and end > start:
        json_text = response_text[start:end]
        try:
            return json.loads(json_text)
        except json.JSONDecodeError:
            pass
    
    # Try to find JSON array
    start = response_text.find('[')
    end = response_text.rfind(']') + 1
    
    if start != -1 and end > start:
        json_text = response_text[start:end]
        try:
            return json.loads(json_text)
        except json.JSONDecodeError:
            pass
    
    return None

# Usage
response = ollama.generate(
    model='phi4-mini',
    prompt='Extract person details as JSON: "Alice, 25, Engineer"'
)

data = extract_json_from_response(response['response'])
if data:
    print(f"Name: {data.get('name')}")
    print(f"Age: {data.get('age')}")
"""

st.code(extraction_code, language="python")

# Interactive demo
st.subheader("🎮 Interactive Parsing Demo")

sample_response = st.text_area(
    "Sample AI Response (with JSON):",
    '''Here's the information in JSON format:
{
    "name": "Alice Smith",
    "age": 28,
    "skills": ["Python", "JavaScript", "SQL"],
    "active": true
}
I hope this helps!''',
    height=150
)

if st.button("Parse JSON"):
    try:
        # Extract JSON
        start = sample_response.find('{')
        end = sample_response.rfind('}') + 1
        
        if start != -1 and end > start:
            json_text = sample_response[start:end]
            data = json.loads(json_text)
            
            st.success("✅ Successfully parsed JSON!")
            st.json(data)
            
            st.write("**Accessing fields:**")
            st.write(f"Name: {data.get('name')}")
            st.write(f"Age: {data.get('age')}")
            st.write(f"Skills: {', '.join(data.get('skills', []))}")
        else:
            st.error("No JSON found in response")
            
    except json.JSONDecodeError as e:
        st.error(f"❌ JSON parsing error: {e}")

# Validation
st.subheader("✅ Response Validation")

validation_code = """
def validate_json_response(data, required_fields):
    '''Validate parsed JSON has required fields'''
    
    if not isinstance(data, dict):
        return False, "Response is not a JSON object"
    
    missing = [f for f in required_fields if f not in data]
    if missing:
        return False, f"Missing fields: {missing}"
    
    return True, "Valid"

# Usage
data = extract_json_from_response(response['response'])

if data:
    valid, message = validate_json_response(
        data, 
        required_fields=['name', 'age', 'email']
    )
    
    if valid:
        print("Data is valid:", data)
    else:
        print("Validation failed:", message)
        # Retry or use default values
"""

st.code(validation_code, language="python")

# Common patterns
st.subheader("📋 Common Parsing Patterns")

st.write("**1. Key-Value Extraction**")
kv_pattern = """
# Parse "Key: Value" format
text = '''
Name: John Doe
Age: 30
City: New York
'''

data = {}
for line in text.strip().split('\\n'):
    if ':' in line:
        key, value = line.split(':', 1)
        data[key.strip().lower()] = value.strip()

print(data)
# {'name': 'John Doe', 'age': '30', 'city': 'New York'}
"""
st.code(kv_pattern, language="python")

st.write("**2. Numbered List Parsing**")
numbered_pattern = """
# Parse numbered list
text = '''
1. First item
2. Second item
3. Third item
'''

import re
items = re.findall(r'\\d+\\.\\s*(.+)', text)
print(items)
# ['First item', 'Second item', 'Third item']
"""
st.code(numbered_pattern, language="python")

st.write("**3. Code Block Extraction**")
code_pattern = """
# Extract code from markdown code blocks
text = '''
Here's the code:
```python
def hello():
    print("Hello, World!")
```
That's the function.
'''

import re
code_blocks = re.findall(r'```(?:\\w+)?\\n(.+?)```', text, re.DOTALL)
if code_blocks:
    code = code_blocks[0].strip()
    print(code)
"""
st.code(code_pattern, language="python")

# Error handling
st.subheader("⚠️ Error Handling")

error_code = """
def safe_parse_json(response_text, default=None):
    '''Safely parse JSON with fallback'''
    
    try:
        # Try to extract and parse JSON
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        
        if start != -1 and end > start:
            json_text = response_text[start:end]
            return json.loads(json_text)
        
        return default
        
    except Exception as e:
        print(f"Parsing error: {e}")
        return default

# Usage with retry logic
max_retries = 3
for attempt in range(max_retries):
    response = ollama.generate(model='phi4-mini', prompt=prompt)
    data = safe_parse_json(response['response'])
    
    if data:
        break  # Success
    
    if attempt < max_retries - 1:
        # Modify prompt to be more explicit
        prompt += "\\nIMPORTANT: Output valid JSON only."
"""

st.code(error_code, language="python")

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Prompt Engineering:**
- Be explicit about output format
- Provide examples of desired format
- Use phrases like "output only JSON" or "no extra text"

**Parsing:**
- Always validate parsed data
- Handle parsing errors gracefully
- Use regex for pattern matching
- Strip whitespace and clean text

**Error Handling:**
- Implement retry logic
- Provide default values
- Log parsing failures
- Give clear error messages
""")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **JSON format**: Most reliable for structured data
- **Explicit prompts**: "Output as JSON" works better than "give me data"
- **Examples**: Show the exact format you want
- **Validation**: Always validate parsed data
- **Fallbacks**: Have default values ready
- **Testing**: Test with various response formats
""")
