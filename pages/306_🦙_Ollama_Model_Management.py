import streamlit as st

from lib import helper_streamlit


st.header("🗂️ Model Management — Ollama Basics")
st.subheader("Working with Models")

st.markdown("**List Available Models:**")
CODE = """
import ollama

# List all models
models = ollama.list()

for model in models['models']:
	print(f"Name: {model['name']}")
	print(f"Size: {model['size']}")
	print(f"Modified: {model['modified_at']}")
	print("---")

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Pull a Model:**")
CODE = """
import ollama

# Pull a specific model
ollama.pull('mistral')

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Delete a Model:**")
CODE = """
import ollama

# Delete a model
ollama.delete('model_name')

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)
