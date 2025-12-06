import streamlit as st

from lib import helper_streamlit


st.header("🛡️ Error Handling — Ollama Basics")
st.subheader("Handling Errors Gracefully")

CODE = """
import ollama

try:
	response = ollama.chat(
		model='phi4-mini',
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

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Common Errors:**")
st.markdown("""
- Model not found: Model hasn't been pulled
- Connection error: Ollama service not running
- Response error: Invalid parameters or model error
""")
