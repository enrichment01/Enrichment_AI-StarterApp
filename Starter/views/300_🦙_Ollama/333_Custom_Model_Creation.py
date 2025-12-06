import streamlit as st

st.header("🔧 Custom Model Creation — Ollama Basics")
st.markdown("Creating and customizing your own Ollama models with Modelfiles.")

# Overview
st.subheader("What is a Modelfile?")

st.write("""
A Modelfile is like a Dockerfile but for AI models. It allows you to:
- Create custom models with specific behaviors
- Set default parameters
- Define system prompts
- Customize model behavior
""")

# Basic Modelfile
st.subheader("📝 Basic Modelfile Structure")

basic_modelfile = """
# Start from an existing model
FROM phi4-mini

# Set the temperature (creativity)
PARAMETER temperature 0.8

# Set the system message
SYSTEM You are a helpful coding assistant who explains things clearly.

# Set other parameters
PARAMETER top_p 0.9
PARAMETER top_k 40
"""

st.code(basic_modelfile, language="dockerfile")

# Creating a model
st.subheader("🚀 Creating a Custom Model")

create_code = """
# Step 1: Create a Modelfile
# Save the content above to a file named 'Modelfile'

# Step 2: Create the model using Ollama CLI
# Run in terminal:

ollama create my-coding-assistant -f ./Modelfile

# Step 3: Use your custom model
import ollama

response = ollama.generate(
    model='my-coding-assistant',
    prompt='Explain what a variable is in Python'
)

print(response['response'])
"""

st.code(create_code, language="python")

# Modelfile directives
st.subheader("📋 Modelfile Directives")

directives = {
    "FROM": "Base model to start from (required)",
    "PARAMETER": "Set model parameters (temperature, etc.)",
    "SYSTEM": "System message that defines behavior",
    "TEMPLATE": "Full prompt template (advanced)",
    "MESSAGE": "Example conversation history",
    "ADAPTER": "Fine-tuned model adapter"
}

for directive, description in directives.items():
    st.write(f"**{directive}**: {description}")

# Example: Python tutor
st.subheader("💼 Example: Python Tutor")

python_tutor = """
FROM phi4-mini

# System prompt defining the role
SYSTEM '''
You are an expert Python programming tutor.
Your goal is to help beginners learn Python effectively.

Guidelines:
- Use simple, clear language
- Provide code examples
- Explain concepts step-by-step
- Be encouraging and patient
- Use analogies when helpful
'''

# Parameters for teaching
PARAMETER temperature 0.7
PARAMETER top_p 0.9

# Example conversations
MESSAGE user "What is a variable?"
MESSAGE assistant "A variable is like a labeled box where you can store data. For example: name = 'Alice' stores the text 'Alice' in a variable called 'name'."
"""

st.code(python_tutor, language="dockerfile")

st.write("**Create and use:**")
st.code("""
# Terminal
ollama create python-tutor -f ./Modelfile

# Python
response = ollama.generate(
    model='python-tutor',
    prompt='How do I use loops?'
)
""", language="bash")

# Example: Code reviewer
st.subheader("🔍 Example: Code Reviewer")

code_reviewer = """
FROM codellama

SYSTEM '''
You are a senior code reviewer.
Analyze code for:
- Best practices
- Potential bugs
- Performance issues
- Security concerns
- Code style

Provide constructive feedback with examples.
'''

PARAMETER temperature 0.3
PARAMETER top_p 0.8
"""

st.code(code_reviewer, language="dockerfile")

# Example: Creative writer
st.subheader("✍️ Example: Creative Writer")

creative_writer = """
FROM llama3

SYSTEM '''
You are a creative writing assistant.
Help users with:
- Story ideas
- Character development
- Plot suggestions
- Writing style improvement

Be imaginative and inspiring!
'''

PARAMETER temperature 1.2
PARAMETER top_p 0.95
PARAMETER top_k 50
"""

st.code(creative_writer, language="dockerfile")

# Parameters guide
st.subheader("⚙️ Parameter Guide")

params = {
    "temperature": "0.0-2.0, controls randomness (0.7 default)",
    "top_p": "0.0-1.0, nucleus sampling (0.9 default)",
    "top_k": "1-100, limits token choices (40 default)",
    "repeat_penalty": "0.0-2.0, penalizes repetition (1.1 default)",
    "num_ctx": "Context window size in tokens",
    "num_predict": "Max tokens to generate"
}

for param, desc in params.items():
    st.write(f"**{param}**: {desc}")

# Managing models
st.subheader("🗂️ Managing Custom Models")

manage_code = """
# List all models (including custom)
ollama list

# Run a custom model
ollama run my-coding-assistant

# Delete a custom model
ollama rm my-coding-assistant

# Show model details
ollama show my-coding-assistant

# Copy a model
ollama cp my-coding-assistant my-assistant-v2
"""

st.code(manage_code, language="bash")

# Advanced: Templates
st.subheader("🎯 Advanced: Custom Templates")

template_example = """
FROM phi4-mini

# Custom prompt template
TEMPLATE '''
### Instruction:
{{ .System }}

### Input:
{{ .Prompt }}

### Response:
'''

SYSTEM You are a helpful assistant.

PARAMETER temperature 0.7
"""

st.code(template_example, language="dockerfile")

# Multi-model setup
st.subheader("🔄 Multi-Model Setup")

multi_model = """
# Create specialized models for different tasks

# 1. Fast responder
FROM phi
SYSTEM You provide quick, concise answers.
PARAMETER temperature 0.5

# Save as: Modelfile.quick
# Create: ollama create quick-assistant -f Modelfile.quick

# 2. Detailed explainer  
FROM llama3
SYSTEM You provide detailed, comprehensive explanations.
PARAMETER temperature 0.8

# Save as: Modelfile.detailed
# Create: ollama create detailed-assistant -f Modelfile.detailed

# 3. Code helper
FROM codellama
SYSTEM You help with coding tasks and debugging.
PARAMETER temperature 0.3

# Save as: Modelfile.code
# Create: ollama create code-helper -f Modelfile.code
"""

st.code(multi_model, language="dockerfile")

# Usage in Python
st.subheader("🐍 Using Custom Models in Python")

python_usage = """
import ollama

# Use custom model just like any other model
response = ollama.generate(
    model='my-coding-assistant',
    prompt='Explain recursion'
)

# With chat
messages = [
    {'role': 'user', 'content': 'What are decorators?'}
]

response = ollama.chat(
    model='python-tutor',
    messages=messages
)

# Check if model exists
try:
    ollama.show('my-model')
    print("Model exists!")
except Exception:
    print("Model not found")
"""

st.code(python_usage, language="python")

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Model Creation:**
- Start from appropriate base model
- Keep system prompts clear and focused
- Test parameters with different inputs
- Version your Modelfiles (use git)

**System Prompts:**
- Be specific about behavior
- Include examples if needed
- Define output format requirements
- Keep it concise but complete

**Parameters:**
- Lower temperature (0.1-0.5) for factual tasks
- Higher temperature (0.8-1.5) for creative tasks
- Adjust top_p and top_k together
- Test with your actual use cases

**Organization:**
- Name models descriptively
- Document what each model does
- Keep Modelfiles in version control
- Create models for specific use cases
""")

# Common patterns
st.subheader("📋 Common Patterns")

patterns = """
# Pattern 1: Task-specific assistant
FROM <base-model>
SYSTEM You are a <role> that <purpose>.
PARAMETER temperature <value>

# Pattern 2: Domain expert
FROM <base-model>
SYSTEM You are an expert in <domain>.
Your responses should be <style>.
Focus on <aspects>.

# Pattern 3: Constrained output
FROM <base-model>
SYSTEM Respond in <format>.
Be <constraint1> and <constraint2>.
PARAMETER temperature 0.3

# Pattern 4: Multi-turn specialist
FROM <base-model>
SYSTEM You maintain context across conversation.
Remember previous messages and build upon them.
MESSAGE user "Example question"
MESSAGE assistant "Example response"
"""

st.code(patterns, language="dockerfile")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **Iterate**: Create, test, refine your models
- **Specialize**: Make models for specific tasks
- **Document**: Keep notes on what works
- **Share**: Export and share working Modelfiles
- **Update**: Rebuild when base models update
- **Test**: Always test before deploying to production
""")

# Resources
st.subheader("📚 Resources")

st.write("**Learn more:**")
st.markdown("- [Ollama Modelfile Reference](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)")
st.markdown("- [Example Modelfiles](https://github.com/ollama/ollama/tree/main/examples)")
st.markdown("- [Community Models](https://ollama.ai/library)")
