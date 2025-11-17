import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Starter App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🤖 Streamlit/Ollama Starter App")

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("---")

# Page selection
page = st.sidebar.radio(
    "Select a Page:",
    [
        "🏠 Home",
        "🐍 Python Basics",
        "📊 Streamlit Basics",
        "🦙 Ollama Python SDK Basics",
        "🚀 Ollama AI MiniApps"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "This is a starter application showcasing Python, Streamlit, "
    "and Ollama integration examples."
)

# Home Page
if page == "🏠 Home":
    st.header("Welcome to the AI Starter App!")
    
    st.markdown("""
    This application provides interactive samples and mini-apps to help you learn:
    
    ### 📚 What You'll Learn
    
    1. **🐍 Python Basics** - Core Python programming concepts and examples
    2. **📊 Streamlit Basics** - Building interactive web apps with Streamlit
    3. **🦙 Ollama Python SDK Basics** - Working with Ollama's Python SDK for AI models
    4. **🚀 Ollama AI MiniApps** - Complete mini-applications using Ollama
    
    ### 🚀 Getting Started
    
    Use the sidebar to navigate through different sections. Each page contains:
    - Interactive examples
    - Code snippets
    - Hands-on demonstrations
    
    ### 📋 Prerequisites
    
    - Python 3.8 or higher
    - Streamlit installed
    - Ollama installed and running (for Ollama-related pages)
    
    ### 💡 Tip
    
    Start with the Python and Streamlit basics if you're new to these technologies,
    then move on to Ollama integration!
    """)
    
    # Quick stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pages", "4", "Interactive")
    with col2:
        st.metric("Examples", "20+", "Code Samples")
    with col3:
        st.metric("Mini Apps", "3", "Full Apps")

# Python Basics Page
elif page == "🐍 Python Basics":
    from pages import python_basics
    python_basics.show()

# Streamlit Basics Page
elif page == "📊 Streamlit Basics":
    from pages import streamlit_basics
    streamlit_basics.show()

# Ollama Python SDK Basics Page
elif page == "🦙 Ollama Python SDK Basics":
    from pages import ollama_basics
    ollama_basics.show()

# Ollama AI MiniApps Page
elif page == "🚀 Ollama AI MiniApps":
    from pages import ollama_miniapps
    ollama_miniapps.show()
