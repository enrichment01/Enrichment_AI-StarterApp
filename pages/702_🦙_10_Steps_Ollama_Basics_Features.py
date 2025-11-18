import streamlit as st
import time

st.set_page_config(page_title="10 Steps: Ollama Basics & Features", page_icon="🦙", layout="wide")

st.title("🦙 10 Steps to Master Ollama Basics and Features")
st.markdown("A comprehensive guide to learn Ollama's capabilities and integration with Python.")

# Create tabs for each step
tabs = st.tabs([
    "Installation",
    "Basic Generation",
    "Streaming",
    "Models",
    "Temperature",
    "System Messages",
    "Context",
    "Conversations",
    "Error Handling",
    "Complete Example"
])

# Step 1: Installation and Setup
with tabs[0]:
    st.header("Step 1: Installation and Setup")
    st.markdown("Get started with Ollama installation and configuration.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Installation Steps:")
        
        st.markdown("**1. Install Ollama:**")
        st.info("Visit [https://ollama.ai](https://ollama.ai) to download Ollama for your operating system.")
        
        st.markdown("**2. Verify Installation:**")
        st.code("ollama --version", language="bash")
        
        st.markdown("**3. Pull a Model:**")
        st.code("ollama pull llama2", language="bash")
        
        st.markdown("**4. List Models:**")
        st.code("ollama list", language="bash")
        
        st.markdown("**5. Install Python SDK:**")
        st.code("pip install ollama", language="bash")
        
        st.markdown("**6. Test Connection:**")
        if st.button("Test Ollama Connection", key="test_connection"):
            try:
                import ollama
                models = ollama.list()
                st.success(f"✅ Ollama is running! Found {len(models.get('models', []))} model(s)")
                for model in models.get('models', []):
                    st.write(f"- {model.get('name', 'unknown')}")
            except ImportError:
                st.error("❌ Ollama Python SDK not installed. Run: pip install ollama")
            except Exception as e:
                st.error(f"❌ Connection error: {str(e)}")
                st.info("Make sure Ollama is running in the background.")
    
    with col2:
        st.markdown("### Python Code:")
        code = """
import ollama

# Check if Ollama is running
try:
    # List available models
    models = ollama.list()
    
    print("✅ Ollama is running!")
    print(f"Available models: {len(models['models'])}")
    
    for model in models['models']:
        print(f"  - {model['name']}")
        print(f"    Size: {model['size']}")
        print(f"    Modified: {model['modified_at']}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure Ollama is running!")
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Ollama must be running in the background before using the Python SDK.")

# Step 2: Basic Text Generation
with tabs[1]:
    st.header("Step 2: Basic Text Generation")
    st.markdown("Generate text using Ollama's generate API.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Interactive Example:")
        
        prompt_basic = st.text_area(
            "Enter your prompt:",
            "Write a haiku about programming",
            height=100,
            key="basic_prompt"
        )
        
        if st.button("Generate", key="basic_generate"):
            with st.spinner("Generating..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt_basic
                    )
                    st.success("✅ Generated!")
                    st.markdown("**Response:**")
                    st.write(response['response'])
                except ImportError:
                    st.error("❌ Ollama not installed. Run: pip install ollama")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

# Generate text
response = ollama.generate(
    model='llama2',
    prompt='Write a haiku about programming'
)

# Access the response
print(response['response'])

# Additional information
print(f"Total duration: {response['total_duration']}")
print(f"Load duration: {response['load_duration']}")
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** The generate() function returns a dictionary with 'response' and metadata.")

# Step 3: Streaming Responses
with tabs[2]:
    st.header("Step 3: Streaming Responses")
    st.markdown("Stream responses in real-time for better user experience.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Streaming Example:")
        
        prompt_stream = st.text_input(
            "Enter prompt for streaming:",
            "Tell me a short story about a robot",
            key="stream_prompt"
        )
        
        if st.button("Generate with Streaming", key="stream_generate"):
            st.markdown("**Streaming Response:**")
            response_placeholder = st.empty()
            full_response = ""
            
            try:
                import ollama
                stream = ollama.generate(
                    model='llama2',
                    prompt=prompt_stream,
                    stream=True
                )
                
                for chunk in stream:
                    if 'response' in chunk:
                        full_response += chunk['response']
                        response_placeholder.markdown(full_response + "▌")
                
                response_placeholder.markdown(full_response)
                st.success("✅ Streaming complete!")
            except ImportError:
                st.error("❌ Ollama not installed")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

# Stream the response
stream = ollama.generate(
    model='llama2',
    prompt='Tell me a short story about a robot',
    stream=True
)

# Process each chunk
full_response = ""
for chunk in stream:
    if 'response' in chunk:
        full_response += chunk['response']
        print(chunk['response'], end='', flush=True)

print()  # New line at the end
print(f"\\nComplete response length: {len(full_response)}")
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Streaming provides immediate feedback and better UX for long responses.")

# Step 4: Model Selection
with tabs[3]:
    st.header("Step 4: Model Selection and Management")
    st.markdown("Choose the right model for your task.")
    
    st.markdown("### Available Ollama Models:")
    
    models_data = {
        "Model": ["llama2", "mistral", "codellama", "phi", "llama2:13b"],
        "Size": ["3.8GB", "4.1GB", "3.8GB", "1.6GB", "7.3GB"],
        "Best For": [
            "General purpose, conversation",
            "Fast responses, efficient",
            "Code generation, debugging",
            "Lightweight, quick tasks",
            "Advanced reasoning"
        ],
        "Speed": ["Medium", "Fast", "Medium", "Very Fast", "Slow"],
        "Quality": ["High", "High", "High", "Medium", "Very High"]
    }
    
    import pandas as pd
    st.dataframe(pd.DataFrame(models_data), use_container_width=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Model Commands:")
        st.code("# Pull a model\nollama pull llama2", language="bash")
        st.code("# Pull specific version\nollama pull llama2:13b", language="bash")
        st.code("# List installed models\nollama list", language="bash")
        st.code("# Remove a model\nollama rm llama2", language="bash")
    
    with col2:
        st.markdown("### Python Code:")
        code = """
import ollama

# List all models
models = ollama.list()
for model in models['models']:
    print(f"Model: {model['name']}")
    print(f"Size: {model['size']}")

# Generate with specific model
response = ollama.generate(
    model='mistral',  # Use different model
    prompt='Explain quantum computing'
)

print(response['response'])
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** Start with llama2 or mistral for general tasks, use codellama for coding.")

# Step 5: Temperature and Parameters
with tabs[4]:
    st.header("Step 5: Temperature and Parameters")
    st.markdown("Control generation behavior with parameters.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Interactive Parameters:")
        
        param_prompt = st.text_input(
            "Prompt:",
            "Write a creative opening line for a story",
            key="param_prompt"
        )
        
        temperature = st.slider(
            "Temperature (creativity):",
            0.0, 2.0, 0.7, 0.1,
            help="Higher = more creative/random, Lower = more focused/deterministic",
            key="param_temp"
        )
        
        top_k = st.slider(
            "Top K:",
            1, 100, 40,
            help="Number of highest probability vocabulary tokens to keep",
            key="param_topk"
        )
        
        top_p = st.slider(
            "Top P:",
            0.0, 1.0, 0.9, 0.05,
            help="Nucleus sampling threshold",
            key="param_topp"
        )
        
        if st.button("Generate with Parameters", key="param_generate"):
            with st.spinner("Generating..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=param_prompt,
                        options={
                            'temperature': temperature,
                            'top_k': top_k,
                            'top_p': top_p
                        }
                    )
                    st.success("✅ Generated!")
                    st.write(response['response'])
                    
                    with st.expander("Show parameters used"):
                        st.json({
                            'temperature': temperature,
                            'top_k': top_k,
                            'top_p': top_p
                        })
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

response = ollama.generate(
    model='llama2',
    prompt='Write a creative opening line',
    options={
        'temperature': 0.8,  # More creative
        'top_k': 40,         # Vocabulary breadth
        'top_p': 0.9,        # Nucleus sampling
        'num_predict': 100,  # Max tokens
        'stop': ['\\n\\n']    # Stop sequences
    }
)

print(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Parameter Guide:")
        st.markdown("""
        - **Temperature (0.0-2.0)**:
          - 0.0-0.3: Deterministic, factual
          - 0.4-0.7: Balanced
          - 0.8-2.0: Creative, varied
        
        - **Top K**: Number of tokens to consider
        - **Top P**: Cumulative probability threshold
        - **Num Predict**: Maximum output length
        """)
    
    st.success("✅ **Key Point:** Adjust temperature for creativity, use lower values for factual tasks.")

# Step 6: System Messages
with tabs[5]:
    st.header("Step 6: System Messages and Roles")
    st.markdown("Define AI behavior with system messages.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### System Message Example:")
        
        system_msg = st.text_area(
            "System Message:",
            "You are a helpful coding assistant who explains concepts simply.",
            height=100,
            key="system_msg"
        )
        
        user_msg = st.text_input(
            "User Message:",
            "What is a list comprehension?",
            key="user_msg"
        )
        
        if st.button("Chat with System Message", key="system_generate"):
            with st.spinner("Generating..."):
                try:
                    import ollama
                    response = ollama.chat(
                        model='llama2',
                        messages=[
                            {
                                'role': 'system',
                                'content': system_msg
                            },
                            {
                                'role': 'user',
                                'content': user_msg
                            }
                        ]
                    )
                    st.success("✅ Response received!")
                    st.markdown("**AI Response:**")
                    st.write(response['message']['content'])
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

# Chat with system message
response = ollama.chat(
    model='llama2',
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful coding assistant who explains concepts simply.'
        },
        {
            'role': 'user',
            'content': 'What is a list comprehension?'
        }
    ]
)

print(response['message']['content'])
"""
        st.code(code, language="python")
        
        st.markdown("### Common System Messages:")
        st.markdown("""
        - **Teacher**: "Explain concepts clearly with examples"
        - **Critic**: "Provide constructive feedback"
        - **Creative**: "Be imaginative and original"
        - **Technical**: "Be precise and use technical terms"
        - **Friendly**: "Be casual and conversational"
        """)
    
    st.info("💡 **Tip:** System messages set the tone and behavior for the entire conversation.")

# Step 7: Context Management
with tabs[6]:
    st.header("Step 7: Context Window Management")
    st.markdown("Manage conversation context efficiently.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Context Example:")
        
        st.markdown("""
        Context allows the model to remember previous interactions.
        Without context, each message is independent.
        """)
        
        if 'context' not in st.session_state:
            st.session_state.context = None
        
        context_prompt = st.text_input(
            "Your message:",
            "What is the capital of France?",
            key="context_prompt"
        )
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("Send (with context)", key="with_context"):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=context_prompt,
                        context=st.session_state.context
                    )
                    st.session_state.context = response['context']
                    st.success("✅ Response:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        with col_b:
            if st.button("Clear Context", key="clear_context"):
                st.session_state.context = None
                st.success("✅ Context cleared!")
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

# Initialize context
context = None

# First message
response1 = ollama.generate(
    model='llama2',
    prompt='What is the capital of France?',
    context=context
)
print(response1['response'])

# Save context
context = response1['context']

# Follow-up with context
response2 = ollama.generate(
    model='llama2',
    prompt='What is its population?',
    context=context  # Model remembers Paris
)
print(response2['response'])
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Context enables follow-up questions and maintains conversation flow.")

# Step 8: Multi-turn Conversations
with tabs[7]:
    st.header("Step 8: Multi-turn Conversations")
    st.markdown("Build interactive chat experiences.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Chat Example:")
        
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        
        # Display chat history
        for msg in st.session_state.chat_history:
            if msg['role'] == 'user':
                st.markdown(f"**You:** {msg['content']}")
            else:
                st.markdown(f"**AI:** {msg['content']}")
        
        # Input
        chat_input = st.text_input("Your message:", key="chat_input")
        
        col_send, col_clear = st.columns(2)
        
        with col_send:
            if st.button("Send", key="chat_send") and chat_input:
                st.session_state.chat_history.append({
                    'role': 'user',
                    'content': chat_input
                })
                
                try:
                    import ollama
                    response = ollama.chat(
                        model='llama2',
                        messages=st.session_state.chat_history
                    )
                    
                    st.session_state.chat_history.append({
                        'role': 'assistant',
                        'content': response['message']['content']
                    })
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        with col_clear:
            if st.button("Clear Chat", key="chat_clear"):
                st.session_state.chat_history = []
                st.rerun()
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

# Conversation history
messages = []

def chat(user_message):
    # Add user message
    messages.append({
        'role': 'user',
        'content': user_message
    })
    
    # Get response
    response = ollama.chat(
        model='llama2',
        messages=messages
    )
    
    # Add assistant response
    messages.append({
        'role': 'assistant',
        'content': response['message']['content']
    })
    
    return response['message']['content']

# Example conversation
print(chat("Hello, how are you?"))
print(chat("What's the weather like?"))
print(chat("Thanks!"))
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** Maintain message history for context-aware conversations.")

# Step 9: Error Handling
with tabs[8]:
    st.header("Step 9: Error Handling and Best Practices")
    st.markdown("Handle errors gracefully and follow best practices.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Common Errors:")
        
        st.markdown("**1. Connection Error:**")
        st.code("ConnectionError: Ollama server not running", language="text")
        st.markdown("*Solution:* Start Ollama service")
        
        st.markdown("**2. Model Not Found:**")
        st.code("Error: model 'llama2' not found", language="text")
        st.markdown("*Solution:* Run `ollama pull llama2`")
        
        st.markdown("**3. Import Error:**")
        st.code("ModuleNotFoundError: No module named 'ollama'", language="text")
        st.markdown("*Solution:* Run `pip install ollama`")
        
        st.markdown("### Test Error Handling:")
        if st.button("Test Error Handling", key="test_error"):
            try:
                import ollama
                # Try to use non-existent model
                try:
                    response = ollama.generate(
                        model='nonexistent_model',
                        prompt='test'
                    )
                except Exception as e:
                    st.warning(f"⚠️ Caught error: {str(e)}")
                    st.info("Using fallback model...")
                    
                    # Fallback to default model
                    response = ollama.generate(
                        model='llama2',
                        prompt='Say hello'
                    )
                    st.success(f"✅ Fallback successful: {response['response']}")
            except ImportError:
                st.error("❌ Ollama not installed")
    
    with col2:
        st.markdown("### Code:")
        code = """
import ollama

def safe_generate(prompt, model='llama2'):
    '''Generate text with error handling'''
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        return response['response']
        
    except ConnectionError:
        return "Error: Ollama not running"
        
    except Exception as e:
        if 'not found' in str(e):
            print(f"Model {model} not found, using llama2")
            # Retry with default model
            response = ollama.generate(
                model='llama2',
                prompt=prompt
            )
            return response['response']
        else:
            return f"Error: {str(e)}"

# Usage
result = safe_generate("Hello", model="mistral")
print(result)
"""
        st.code(code, language="python")
        
        st.markdown("### Best Practices:")
        st.markdown("""
        1. ✅ Always handle exceptions
        2. ✅ Provide fallback options
        3. ✅ Validate model availability
        4. ✅ Set reasonable timeouts
        5. ✅ Log errors for debugging
        """)
    
    st.success("✅ **Key Point:** Robust error handling ensures better user experience.")

# Step 10: Complete Example
with tabs[9]:
    st.header("Step 10: Complete Ollama Application")
    st.markdown("Combine all concepts into a full-featured application.")
    
    st.markdown("### AI Writing Assistant")
    st.markdown("A complete application demonstrating all Ollama features.")
    
    # Configuration
    with st.sidebar:
        st.markdown("### Configuration")
        selected_model = st.selectbox(
            "Model:",
            ["llama2", "mistral", "codellama", "phi"],
            key="complete_model"
        )
        temp_setting = st.slider(
            "Temperature:",
            0.0, 2.0, 0.7, 0.1,
            key="complete_temp"
        )
        system_role = st.text_area(
            "System Message:",
            "You are a helpful writing assistant.",
            key="complete_system"
        )
    
    # Main interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        task_type = st.selectbox(
            "Task:",
            ["Creative Writing", "Technical Explanation", "Code Generation", "Summarization"],
            key="complete_task"
        )
        
        prompt_input = st.text_area(
            "Your prompt:",
            placeholder="Enter your prompt here...",
            height=150,
            key="complete_prompt"
        )
        
        use_streaming = st.checkbox("Use streaming", value=True, key="complete_stream")
        
        if st.button("✨ Generate", type="primary", key="complete_generate"):
            if not prompt_input:
                st.warning("Please enter a prompt")
            else:
                try:
                    import ollama
                    
                    # Adjust system message based on task
                    task_systems = {
                        "Creative Writing": "You are a creative writer with a vivid imagination.",
                        "Technical Explanation": "You are a technical expert who explains clearly.",
                        "Code Generation": "You are an expert programmer.",
                        "Summarization": "You are skilled at creating concise summaries."
                    }
                    
                    messages = [
                        {
                            'role': 'system',
                            'content': task_systems.get(task_type, system_role)
                        },
                        {
                            'role': 'user',
                            'content': prompt_input
                        }
                    ]
                    
                    st.markdown("### Generated Content:")
                    
                    if use_streaming:
                        response_placeholder = st.empty()
                        full_response = ""
                        
                        stream = ollama.chat(
                            model=selected_model,
                            messages=messages,
                            stream=True,
                            options={'temperature': temp_setting}
                        )
                        
                        for chunk in stream:
                            if 'message' in chunk and 'content' in chunk['message']:
                                full_response += chunk['message']['content']
                                response_placeholder.markdown(full_response + "▌")
                        
                        response_placeholder.markdown(full_response)
                    else:
                        with st.spinner(f"Generating with {selected_model}..."):
                            response = ollama.chat(
                                model=selected_model,
                                messages=messages,
                                options={'temperature': temp_setting}
                            )
                            st.markdown(response['message']['content'])
                    
                    st.success("✅ Generation complete!")
                    
                except ImportError:
                    st.error("❌ Ollama not installed. Run: pip install ollama")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("Make sure Ollama is running and the selected model is available.")
    
    with col2:
        st.markdown("### Features Used:")
        st.markdown("""
        ✅ Model selection
        ✅ Temperature control
        ✅ System messages
        ✅ Task-specific prompts
        ✅ Streaming responses
        ✅ Error handling
        ✅ User configuration
        """)
        
        st.markdown("### Quick Tips:")
        st.info("""
        **For better results:**
        - Be specific in prompts
        - Choose appropriate temperature
        - Use task-specific system messages
        - Enable streaming for long outputs
        """)
    
    st.markdown("---")
    st.markdown("### Complete Application Code:")
    code = """
import streamlit as st
import ollama

st.title("AI Writing Assistant")

# Sidebar configuration
with st.sidebar:
    model = st.selectbox("Model:", ["llama2", "mistral"])
    temperature = st.slider("Temperature:", 0.0, 2.0, 0.7)
    system_msg = st.text_area("System:", "You are a helpful assistant.")

# Main interface
task = st.selectbox("Task:", ["Creative Writing", "Technical", "Code"])
prompt = st.text_area("Prompt:")

if st.button("Generate"):
    messages = [
        {'role': 'system', 'content': system_msg},
        {'role': 'user', 'content': prompt}
    ]
    
    # Stream response
    full_response = ""
    placeholder = st.empty()
    
    stream = ollama.chat(
        model=model,
        messages=messages,
        stream=True,
        options={'temperature': temperature}
    )
    
    for chunk in stream:
        if 'message' in chunk:
            full_response += chunk['message']['content']
            placeholder.markdown(full_response + "▌")
    
    placeholder.markdown(full_response)
    st.success("Complete!")
"""
    st.code(code, language="python")
    
    st.success("🎉 **Congratulations!** You've mastered Ollama basics and features!")

# Summary
st.markdown("---")
st.markdown("## 📝 Summary")

summary_cols = st.columns(2)

with summary_cols[0]:
    st.markdown("""
    ### Core Concepts:
    1. ✅ Installation and setup
    2. ✅ Basic text generation
    3. ✅ Streaming responses
    4. ✅ Model selection
    5. ✅ Temperature and parameters
    """)

with summary_cols[1]:
    st.markdown("""
    ### Advanced Features:
    6. ✅ System messages and roles
    7. ✅ Context management
    8. ✅ Multi-turn conversations
    9. ✅ Error handling
    10. ✅ Complete applications
    """)

st.info("💡 **Next Steps:** Build your own AI-powered applications using Ollama!")
