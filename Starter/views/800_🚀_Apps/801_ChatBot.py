import streamlit as st

from lib import helper_streamlit
from lib.helper_chat import utils

import lib.helper_text.generator as text_generator
import lib.helper_text.analyzer as text_analyzer

st.header("🚀 Ollama AI MiniApps")
st.markdown("Complete mini-applications powered by Ollama.")


st.subheader("💬 AI Chatbot")
st.markdown("Have a conversation with an AI assistant.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chatbot_model" not in st.session_state:
    st.session_state.chatbot_model = "phi4-mini"

# Sidebar settings
with st.sidebar:
    st.markdown("### ⚙️ Chatbot Settings")
    
    st.session_state.chatbot_model = st.selectbox(
        "Model:",
        ["phi4-mini", "mistral", "codellama", "phi"],
        index=0,
        key="chatbot_model_select"
    )
    
    system_prompt = st.text_area(
        "System Prompt:",
        value="You are a helpful AI assistant.",
        height=100,
        key="system_prompt"
    )
    
    temperature = st.slider(
        "Temperature:",
        0.0, 2.0, 0.7, 0.1,
        key="chatbot_temp"
    )
    
    if st.button("🗑️ Clear Chat", key="clear_chat"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Prepare messages
        messages = utils.prepare_chat_messages(
            st.session_state.messages,
            system_prompt
        )
        
        # Stream response
        stream = utils.generate_chat_response(
            model=st.session_state.chatbot_model,
            messages=messages,
            temperature=temperature,
            stream=True
        )
        
        for chunk in stream:
            if 'message' in chunk and 'content' in chunk['message']:
                full_response += chunk['message']['content']
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Instructions
if len(st.session_state.messages) == 0:
    st.info("""
    👋 Welcome to the AI Chatbot!
    
    **How to use:**
    1. Type your message in the input box below
    2. Press Enter to send
    3. Wait for the AI to respond
    4. Continue the conversation!
    
    **Customize:**
    - Change the model in the sidebar
    - Adjust the system prompt to change behavior
    - Modify temperature for creativity
    - Clear chat to start fresh
    """)
