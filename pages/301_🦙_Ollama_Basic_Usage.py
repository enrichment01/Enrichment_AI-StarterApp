import streamlit as st
from lib import helper_streamlit


st.header("🔧 Basic Usage — Ollama Basics")
st.subheader("Simple Chat Completion")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Code:**")
    CODE = """
import ollama

# Simple chat
response = ollama.chat(
    model='phi4-mini',
    messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?'
        }
    ]
)

print(response['message']['content'])

"""
    st.code(CODE, language="python")
    helper_streamlit.run_code(CODE)

with col2:
    st.markdown("**Explanation:**")
    st.markdown("""
    - `ollama.chat()` is the main method for chat completions
    - `model` specifies which model to use (e.g., 'phi4-mini', 'mistral')
    - `messages` is a list of message objects
    - Each message has a `role` ('user', 'assistant', or 'system')
    - Response contains the model's reply in `response['message']['content']`
    """)
