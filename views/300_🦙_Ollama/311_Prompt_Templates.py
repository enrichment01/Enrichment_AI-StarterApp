import streamlit as st

st.header("📝 Prompt Templates — Ollama Basics")
st.markdown("Creating reusable and effective prompt templates.")

# Overview
st.subheader("What are Prompt Templates?")

st.write("""
Prompt templates are reusable patterns that help you create consistent, 
effective prompts for different tasks. They combine structure with 
flexibility through variable substitution.
""")

# Basic template
st.subheader("Basic Template Pattern")

basic_template = """
# Simple template with variables
template = '''
You are a {role}.
Task: {task}
Input: {input}
Output format: {format}
'''

# Use the template
prompt = template.format(
    role="Python expert",
    task="Explain this code",
    input="def factorial(n): return 1 if n <= 1 else n * factorial(n-1)",
    format="Simple explanation for beginners"
)

response = ollama.generate(model='phi4-mini', prompt=prompt)
"""

st.code(basic_template, language="python")

# Template library
st.subheader("📚 Template Library")

templates = {
    "Code Explanation": """You are a programming instructor.
Explain the following code in simple terms:

```
{code}
```

Focus on:
- What it does
- How it works
- When to use it""",
    
    "Text Summarization": """Summarize the following text in {num_sentences} sentences:

{text}

Make the summary {tone}.""",
    
    "Question Answering": """Given the following context, answer the question.

Context: {context}

Question: {question}

Answer:""",
    
    "Translation": """Translate the following {source_lang} text to {target_lang}:

{text}

Translation:""",
    
    "Data Extraction": """Extract {fields} from the following text:

{text}

Output as JSON."""
}

for name, template in templates.items():
    with st.expander(f"📋 {name}"):
        st.code(template)

# Interactive template builder
st.subheader("🎮 Template Builder")

st.write("**Build your own template:**")

role = st.text_input("AI Role", "helpful assistant")
task = st.text_area("Task Description", "Answer questions accurately")
tone = st.selectbox("Tone", ["Professional", "Casual", "Technical", "Friendly"])
output_format = st.selectbox("Output Format", ["Plain text", "JSON", "Markdown", "List"])

user_input = st.text_area("User Input", "What is Python?")

# Generate template
custom_template = f"""You are a {role}.
Your task is to: {task}
Tone: {tone}
Output format: {output_format}

User request: {user_input}

Response:"""

st.write("**Generated Template:**")
st.code(custom_template)

if st.button("Test Template"):
    st.info("In a real app, this would call Ollama with the generated prompt")
    st.write("**Sample Response:**")
    st.success("Python is a high-level, interpreted programming language known for its simplicity and readability...")

# Advanced templates
st.subheader("🎯 Advanced Template Patterns")

st.write("**1. Few-Shot Learning Template**")
few_shot = """Classify the sentiment of these movie reviews:

Review: "This movie was amazing! Best film I've seen this year."
Sentiment: Positive

Review: "Terrible plot, waste of time."
Sentiment: Negative

Review: "It was okay, nothing special."
Sentiment: Neutral

Review: "{review}"
Sentiment:"""

st.code(few_shot)

st.write("**2. Chain-of-Thought Template**")
cot = """Solve this problem step by step:

Problem: {problem}

Let's break it down:
1. Identify what we need to find
2. List the given information
3. Choose the approach
4. Work through the solution
5. Verify the answer

Solution:"""

st.code(cot)

st.write("**3. Role-Based Template**")
role_based = """<|system|>
You are a {role} with expertise in {domain}.
Your communication style is {style}.
<|end|>

<|user|>
{user_message}
<|end|>

<|assistant|>"""

st.code(role_based)

# Template with examples
st.subheader("💼 Real-World Examples")

st.write("**Email Generator Template:**")
email_template = """
template = '''
Write a {tone} email for the following scenario:

To: {recipient}
Subject: {subject}
Context: {context}

Requirements:
- Keep it {length}
- Include {elements}

Email:
'''

# Usage
prompt = template.format(
    tone="professional",
    recipient="team members",
    subject="Project Update",
    context="We've completed the first milestone",
    length="brief (3-4 sentences)",
    elements="greeting, main point, next steps, closing"
)
"""
st.code(email_template, language="python")

st.write("**Code Generation Template:**")
code_gen_template = """
template = '''
Generate {language} code for the following task:

Task: {task}
Requirements:
{requirements}

Include:
- Proper error handling
- Comments explaining key parts
- Example usage

Code:
'''

# Usage
prompt = template.format(
    language="Python",
    task="Read a CSV file and calculate statistics",
    requirements="- Use pandas\\n- Handle missing values\\n- Return dict with stats"
)
"""
st.code(code_gen_template, language="python")

# Best practices
st.subheader("💡 Template Best Practices")

st.info("""
**Structure:**
- Clear role definition
- Specific task description
- Explicit output format
- Examples when helpful

**Clarity:**
- Use simple, direct language
- Break complex tasks into steps
- Define any domain-specific terms

**Flexibility:**
- Use variables for changeable parts
- Keep templates modular
- Version and test templates

**Optimization:**
- Remove unnecessary words
- Use consistent formatting
- Test with different inputs
""")

# Template testing
st.subheader("🧪 Testing Templates")

testing_code = """
# Test template with multiple inputs
template = "Summarize: {text}"

test_cases = [
    "Long article about AI...",
    "Short paragraph...",
    "Technical documentation..."
]

for i, test_input in enumerate(test_cases):
    prompt = template.format(text=test_input)
    response = ollama.generate(model='phi4-mini', prompt=prompt)
    print(f"Test {i+1}: {response['response'][:100]}...")
"""

st.code(testing_code, language="python")

# Template management
st.subheader("📦 Template Management")

management = """
# Store templates in a module
# templates.py

TEMPLATES = {
    'summarize': {
        'template': 'Summarize in {num} sentences: {text}',
        'defaults': {'num': 3}
    },
    'explain': {
        'template': 'Explain {concept} to a {level} audience',
        'defaults': {'level': 'beginner'}
    }
}

def get_template(name, **kwargs):
    t = TEMPLATES[name]
    params = {**t.get('defaults', {}), **kwargs}
    return t['template'].format(**params)

# Usage
from templates import get_template

prompt = get_template('summarize', text='...', num=5)
prompt = get_template('explain', concept='recursion')
"""

st.code(management, language="python")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **Start simple**: Begin with basic templates, add complexity as needed
- **Test thoroughly**: Try edge cases and different inputs
- **Version control**: Track template changes
- **Document**: Explain what each template is for
- **Iterate**: Improve templates based on results
- **Share**: Reuse successful templates across projects
""")
