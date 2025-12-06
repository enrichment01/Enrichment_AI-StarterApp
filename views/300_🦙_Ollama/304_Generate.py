import streamlit as st

from lib import helper_streamlit


st.header("✨ Generate API — Ollama Basics")
st.subheader("Text Generation")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Code:**")
    CODE = """
import ollama

# Generate text
response = ollama.generate(
    model='phi4-mini',
    prompt='Write a haiku about coding'
)

print(response['response'])

"""
    st.code(CODE, language="python")
    helper_streamlit.run_code(CODE)

with col2:
    st.markdown("**Explanation:**")
    st.markdown("""
    - `ollama.generate()` for simple text generation
    - Simpler than chat for single prompts
    - Good for completions without conversation context
    - Returns the generated text in `response['response']`
    """)
