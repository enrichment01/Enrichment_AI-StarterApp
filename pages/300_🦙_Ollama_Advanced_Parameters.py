import streamlit as st

from lib import helper_streamlit


st.header("⚙️ Advanced Parameters — Ollama Basics")
st.subheader("Customizing Model Behavior")

st.markdown("**Temperature, Top-P, and More:**")
CODE = """
import ollama

response = ollama.chat(
    model='phi4-mini',
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

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Parameter Meanings:**")
st.markdown("""
- **temperature** (0.0-2.0): Controls randomness. Lower = more focused, Higher = more creative
- **top_p** (0.0-1.0): Nucleus sampling threshold
- **top_k**: Limits vocabulary to top k tokens
- **num_predict**: Maximum number of tokens to generate
- **repeat_penalty**: Penalizes repetition (default: 1.1)
""")
