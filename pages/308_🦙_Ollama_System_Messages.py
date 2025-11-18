import streamlit as st

from lib import helper_streamlit


st.header("💬 System Messages — Ollama Basics")
st.subheader("Setting Model Behavior")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Code:**")
    CODE = """
import ollama

response = ollama.chat(
    model='phi4-mini',
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

"""
    st.code(CODE, language="python")
    helper_streamlit.run_code(CODE)

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
