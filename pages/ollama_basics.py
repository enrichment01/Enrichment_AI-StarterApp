import streamlit as st
import json

def show():
    st.header("🦙 Ollama Python SDK Basics")
    st.markdown("Learn how to use the Ollama Python SDK to interact with local LLMs.")
    
    # Installation
    with st.expander("📦 Installation", expanded=True):
        st.subheader("Getting Started with Ollama")
        
        st.markdown("**1. Install Ollama:**")
        st.code("# Visit https://ollama.ai to download and install Ollama", language="bash")
        
        st.markdown("**2. Install Python SDK:**")
        st.code("pip install ollama", language="bash")
        
        st.markdown("**3. Pull a model:**")
        st.code("ollama pull llama2", language="bash")
        
        st.info("💡 Make sure Ollama is running before using the SDK!")
    
    # Basic Usage
    with st.expander("🔧 Basic Usage"):
        st.subheader("Simple Chat Completion")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
import ollama

# Simple chat
response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?'
        }
    ]
)

print(response['message']['content'])
            """, language="python")
        
        with col2:
            st.markdown("**Explanation:**")
            st.markdown("""
            - `ollama.chat()` is the main method for chat completions
            - `model` specifies which model to use (e.g., 'llama2', 'mistral')
            - `messages` is a list of message objects
            - Each message has a `role` ('user', 'assistant', or 'system')
            - Response contains the model's reply in `response['message']['content']`
            """)
    
    # Streaming
    with st.expander("📡 Streaming Responses"):
        st.subheader("Real-time Response Streaming")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
import ollama

# Streaming chat
stream = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'user',
            'content': 'Tell me a story'
        }
    ],
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='')
            """, language="python")
        
        with col2:
            st.markdown("**Explanation:**")
            st.markdown("""
            - Set `stream=True` to enable streaming
            - Returns an iterator of response chunks
            - Each chunk contains partial content
            - Useful for displaying responses as they're generated
            - Better user experience for long responses
            """)
    
    # Generate
    with st.expander("✨ Generate API"):
        st.subheader("Text Generation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
import ollama

# Generate text
response = ollama.generate(
    model='llama2',
    prompt='Write a haiku about coding'
)

print(response['response'])
            """, language="python")
        
        with col2:
            st.markdown("**Explanation:**")
            st.markdown("""
            - `ollama.generate()` for simple text generation
            - Simpler than chat for single prompts
            - Good for completions without conversation context
            - Returns the generated text in `response['response']`
            """)
    
    # Model Management
    with st.expander("🗂️ Model Management"):
        st.subheader("Working with Models")
        
        st.markdown("**List Available Models:**")
        st.code("""
import ollama

# List all models
models = ollama.list()

for model in models['models']:
    print(f"Name: {model['name']}")
    print(f"Size: {model['size']}")
    print(f"Modified: {model['modified_at']}")
    print("---")
        """, language="python")
        
        st.markdown("**Pull a Model:**")
        st.code("""
import ollama

# Pull a specific model
ollama.pull('mistral')
        """, language="python")
        
        st.markdown("**Delete a Model:**")
        st.code("""
import ollama

# Delete a model
ollama.delete('model_name')
        """, language="python")
    
    # Advanced Parameters
    with st.expander("⚙️ Advanced Parameters"):
        st.subheader("Customizing Model Behavior")
        
        st.markdown("**Temperature, Top-P, and More:**")
        st.code("""
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
        """, language="python")
        
        st.markdown("**Parameter Meanings:**")
        st.markdown("""
        - **temperature** (0.0-2.0): Controls randomness. Lower = more focused, Higher = more creative
        - **top_p** (0.0-1.0): Nucleus sampling threshold
        - **top_k**: Limits vocabulary to top k tokens
        - **num_predict**: Maximum number of tokens to generate
        - **repeat_penalty**: Penalizes repetition (default: 1.1)
        """)
    
    # System Messages
    with st.expander("💬 System Messages"):
        st.subheader("Setting Model Behavior")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
import ollama

response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful coding assistant.'
        },
        {
            'role': 'user',
            'content': 'How do I reverse a string in Python?'
        }
    ]
)
            """, language="python")
        
        with col2:
            st.markdown("**Explanation:**")
            st.markdown("""
            - System messages define the model's role/behavior
            - Should be the first message in the conversation
            - Influences all subsequent responses
            - Examples:
              - "You are a helpful assistant"
              - "You are a Python expert"
              - "You speak like a pirate"
            """)
    
    # Error Handling
    with st.expander("🛡️ Error Handling"):
        st.subheader("Handling Errors Gracefully")
        
        st.code("""
import ollama

try:
    response = ollama.chat(
        model='llama2',
        messages=[
            {
                'role': 'user',
                'content': 'Hello!'
            }
        ]
    )
    print(response['message']['content'])
    
except ollama.ResponseError as e:
    print(f"Error: {e.error}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
        """, language="python")
        
        st.markdown("**Common Errors:**")
        st.markdown("""
        - Model not found: Model hasn't been pulled
        - Connection error: Ollama service not running
        - Response error: Invalid parameters or model error
        """)
    
    # Interactive Example
    st.markdown("---")
    st.subheader("🎮 Interactive Example: Check Ollama Connection")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Test your Ollama setup:**")
        
        if st.button("Check Ollama Status", key="check_ollama"):
            try:
                import ollama
                
                with st.spinner("Checking Ollama..."):
                    # Try to list models
                    models = ollama.list()
                    
                    st.success("✅ Ollama is running!")
                    st.write(f"Available models: {len(models.get('models', []))}")
                    
                    if models.get('models'):
                        st.markdown("**Your Models:**")
                        for model in models['models']:
                            st.write(f"- {model['name']}")
                    else:
                        st.info("No models found. Run `ollama pull llama2` to get started!")
                        
            except ImportError:
                st.error("❌ Ollama Python SDK not installed. Run: `pip install ollama`")
            except Exception as e:
                st.error(f"❌ Cannot connect to Ollama: {str(e)}")
                st.info("Make sure Ollama is running. Visit https://ollama.ai for installation.")
    
    with col2:
        st.markdown("**Code:**")
        st.code("""
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
        """, language="python")
    
    # Resources
    st.markdown("---")
    st.subheader("📚 Resources")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Official Docs**")
        st.markdown("[Ollama Documentation](https://github.com/ollama/ollama)")
        st.markdown("[Python SDK](https://github.com/ollama/ollama-python)")
    
    with col2:
        st.markdown("**Popular Models**")
        st.markdown("- llama2")
        st.markdown("- mistral")
        st.markdown("- codellama")
        st.markdown("- phi")
    
    with col3:
        st.markdown("**Quick Commands**")
        st.code("ollama list", language="bash")
        st.code("ollama pull <model>", language="bash")
        st.code("ollama run <model>", language="bash")
