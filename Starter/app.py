import streamlit as st

from lib.helper_streamlit import build_navigation

# Page configuration
st.set_page_config(
    page_title="AI Starter App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🤖 Streamlit/Ollama Starter App")

pages = build_navigation()

st.navigation(pages).run()
