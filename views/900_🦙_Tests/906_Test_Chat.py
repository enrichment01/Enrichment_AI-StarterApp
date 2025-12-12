"""
Test: chat()

Tests chat interface with Ollama models.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import chat, get_available_models
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Chat Interface",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Test: chat()")
st.markdown("Testing chat interface with Ollama models")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

# Create tabs
tabs = st.tabs(["Chat", "Summary"])

with tabs[0]:
    st.header("Test: chat(model_name, messages, stream=False)")

# Get available models
with st.spinner("Loading available models..."):
    try:
        available_models = get_available_models()
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        available_models = []

if available_models:
    # Model selection
    col1, col2 = st.columns([3, 1])
    
    with col1:
        model_name = st.selectbox(
            "Select Model:",
            available_models,
            key="model_select"
        )
    
    with col2:
        stream_mode = st.checkbox("Stream Response", value=False, key="stream_mode")
    
    # System prompt
    st.subheader("🤖 System Prompt")
    
    system_examples = {
        "Helpful Assistant": "You are a helpful assistant.",
        "Creative Writer": "You are a creative writer who loves crafting engaging stories.",
        "Code Expert": "You are an expert programmer who provides clear, well-documented code.",
        "Teacher": "You are a patient teacher who explains concepts in simple terms.",
        "Concise": "You are a concise assistant who provides brief, direct answers.",
        "Custom": ""
    }
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        system_type = st.selectbox(
            "System Role:",
            list(system_examples.keys()),
            key="system_type"
        )
    
    with col2:
        system_value = "" if system_type == "Custom" else system_examples[system_type]
    
    system_prompt = st.text_input(
        "System Prompt:",
        value=system_value,
        key="system_prompt"
    )
    
    # User message
    st.subheader("👤 User Message")
    
    message_examples = {
        "Question": "What is the meaning of life?",
        "Explanation": "Explain how neural networks work.",
        "Creative": "Tell me a story about a time-traveling cat.",
        "Code": "Write a Python function to reverse a string.",
        "Advice": "How can I improve my productivity?",
        "Custom": ""
    }
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        message_type = st.selectbox(
            "Message Type:",
            list(message_examples.keys()),
            key="message_type"
        )
    
    with col2:
        message_value = "" if message_type == "Custom" else message_examples[message_type]
    
    user_message = st.text_area(
        "User Message:",
        value=message_value,
        height=100,
        key="user_message"
    )
    
    # Advanced parameters
    with st.expander("⚙️ Advanced Parameters"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1, key="temp")
        
        with col2:
            top_p = st.slider("Top P", 0.0, 1.0, 0.9, 0.1, key="top_p")
        
        with col3:
            top_k = st.slider("Top K", 0, 100, 40, 5, key="top_k")
    
    # Message history
    st.subheader("📜 Message History")
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    include_history = st.checkbox("Include previous messages", value=False, key="include_history")
    
    if include_history and st.session_state.chat_history:
        st.write(f"**Previous messages:** {len(st.session_state.chat_history)}")
        with st.expander("View History"):
            for idx, msg in enumerate(st.session_state.chat_history, 1):
                st.write(f"{idx}. **{msg['role'].title()}:** {msg['content'][:100]}...")
    
    # Code preview
    messages_code = []
    if system_prompt:
        messages_code.append({"role": "system", "content": system_prompt})
    if include_history:
        messages_code.extend(st.session_state.chat_history)
    messages_code.append({"role": "user", "content": user_message})
    
    code_preview = f"""from lib.helper_ollama import chat

messages = {messages_code}

result = chat(
    model_name='{selected_model}',
    messages=messages,
    stream={stream_mode},
    temperature={temperature},
    top_p={top_p},
    top_k={top_k}
)
"""
    
    with st.expander("👀 Code Preview"):
        st.code(code_preview, language='python')
    
    # Chat button
    col1, col2 = st.columns([3, 1])
    
    with col1:
        chat_button = st.button("💬 Send Message", key="btn_chat", type="primary")
    
    with col2:
        if st.button("🗑️ Clear History", key="btn_clear"):
            st.session_state.chat_history = []
            st.rerun()
    
    if chat_button:
        if not user_message:
            st.warning("Please enter a message")
        else:
            with st.spinner(f"Chatting with {model_name}..."):
                try:
                    # Build messages
                    messages = []
                    
                    if system_prompt:
                        messages.append({"role": "system", "content": system_prompt})
                    
                    if include_history:
                        messages.extend(st.session_state.chat_history)
                    
                    messages.append({"role": "user", "content": user_message})
                    
                    # Make chat request
                    result = chat(
                        model_name=selected_model,
                        messages=messages,
                        stream=stream_mode,
                        temperature=temperature,
                        top_p=top_p,
                        top_k=top_k
                    )
                    
                    st.success("✅ Chat completed!")
                    
                    # Display response
                    st.subheader("🤖 Assistant Response")
                    
                    if hasattr(result, 'message'):
                        response_content = result.message.content
                        st.markdown(response_content)
                        
                        # Update history
                        st.session_state.chat_history.append({"role": "user", "content": user_message})
                        st.session_state.chat_history.append({"role": "assistant", "content": response_content})
                        
                        # Metadata
                        st.divider()
                        st.subheader("📊 Metadata")
                        
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            st.metric("Model", result.model)
                        
                        with col2:
                            if hasattr(result, 'total_duration'):
                                duration_sec = result.total_duration / 1e9
                                st.metric("Duration", f"{duration_sec:.2f}s")
                        
                        with col3:
                            if hasattr(result, 'eval_count'):
                                st.metric("Tokens", result.eval_count)
                        
                        with col4:
                            if hasattr(result, 'eval_count') and hasattr(result, 'eval_duration'):
                                tokens_per_sec = result.eval_count / (result.eval_duration / 1e9)
                                st.metric("Tokens/sec", f"{tokens_per_sec:.1f}")
                        
                        # Full response details
                        with st.expander("🔍 Full Response Details"):
                            response_dict = {
                                'role': result.message.role,
                                'content': result.message.content,
                                'model': result.model,
                                'created_at': result.created_at,
                                'done': result.done,
                            }
                            
                            if hasattr(result, 'total_duration'):
                                response_dict['total_duration'] = result.total_duration
                            if hasattr(result, 'eval_count'):
                                response_dict['eval_count'] = result.eval_count
                            
                            st.json(response_dict)
                    else:
                        st.write(result)
                        
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    import traceback
                    with st.expander("Error Details"):
                        st.code(traceback.format_exc())
else:
    st.warning("⚠️ No models available")
    st.markdown("""
    Please install Ollama models first:
    ```bash
    ollama pull llama3.2
    ollama pull mistral
    ollama pull phi3
    ```
    """)

# Summary
with tabs[1]:
    st.header("📊 Summary")
st.markdown("""
### Function Tested:
- ✅ `chat(model_name, messages, stream=False, **kwargs)` - Chat with a model

### Parameters:
- **model_name**: Name of the Ollama model to use
- **messages**: List of message dictionaries with 'role' and 'content'
  - Roles: 'system', 'user', 'assistant'
- **stream**: Whether to stream the response
- **kwargs**: Additional parameters (temperature, top_p, top_k)

### Message Format:
```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi! How can I help?"},
    {"role": "user", "content": "Tell me a joke."}
]
```

### Returns:
A response object containing:
- **message**: The assistant's message (role and content)
- **model**: Model name used
- **created_at**: Timestamp
- **done**: Whether chat is complete
- **total_duration**: Total time
- **eval_count**: Tokens generated

### Expected Behavior:
- Supports multi-turn conversations
- System messages set the assistant's behavior
- Maintains conversation context
- Returns structured message responses
""")

# =================================================================================================
show_code(__file__)
