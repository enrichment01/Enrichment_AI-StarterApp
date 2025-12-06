import streamlit as st


st.header("📦 Installation — Ollama Basics")
st.subheader("Getting Started with Ollama")

st.markdown("**1. Install Ollama:**")
st.code("# Visit https://ollama.ai to download and install Ollama", language="bash")

st.markdown("**2. Install Python SDK:**")
st.code("pip install ollama", language="bash")

st.markdown("**3. Pull a model:**")
st.code("ollama pull phi4-mini", language="bash")

st.info("💡 Make sure Ollama is running before using the SDK!")
