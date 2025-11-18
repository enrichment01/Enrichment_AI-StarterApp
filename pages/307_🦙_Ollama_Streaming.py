import streamlit as st

from lib import helper_streamlit


st.header("📡 Streaming Responses — Ollama Basics")
st.subheader("Real-time Response Streaming")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Code:**")
    CODE = """
import ollama

# Streaming chat
stream = ollama.chat(
    model='phi4-mini',
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

"""
    st.code(CODE, language="python")
    helper_streamlit.run_code(CODE)

with col2:
    st.markdown("**Explanation:**")
    st.markdown("""
    - Set `stream=True` to enable streaming
    - Returns an iterator of response chunks
    - Each chunk contains partial content
    - Useful for displaying responses as they're generated
    - Better user experience for long responses
    """)
