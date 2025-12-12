"""
Test Suite Overview for helper_ollama Module

This page provides an overview of all test pages for the helper_ollama module.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_streamlit import show_code

st.set_page_config(
    page_title="Ollama Test Suite",
    page_icon="🦙",
    layout="wide"
)

st.title("🦙 Ollama Helper Test Suite")
st.markdown("Comprehensive testing suite for `lib/helper_ollama/__init__.py`")

st.markdown("---")

# Overview
st.header("📚 Test Suite Overview")

st.markdown("""
This test suite provides comprehensive coverage of all functions in the `helper_ollama` module.
Each test is in a separate page for focused testing and learning.
""")

# Test pages description
st.header("🧪 Test Pages")

tests = [
    {
        "page": "901_Test_Status_Discovery",
        "icon": "🔍",
        "title": "Status & Discovery",
        "functions": ["check_ollama_status()", "get_available_models()"],
        "description": "Tests basic Ollama status checking and model discovery"
    },
    {
        "page": "902_Test_Model_Filtering",
        "icon": "🔬",
        "title": "Model Filtering",
        "functions": ["get_local_llms(func=None)"],
        "description": "Tests filtering models by capability (embedding, vision, tools, thinking, chat)"
    },
    {
        "page": "903_Test_Model_Categorization",
        "icon": "📋",
        "title": "Model Categorization",
        "functions": ["list_models_by_capability()"],
        "description": "Tests organizing all models by their capabilities"
    },
    {
        "page": "904_Test_Model_Info",
        "icon": "ℹ",
        "title": "Model Information",
        "functions": ["get_model_info(model_name)"],
        "description": "Tests retrieving detailed information about specific models"
    },
    {
        "page": "905_Test_Generate",
        "icon": "✍️",
        "title": "Text Generation",
        "functions": ["generate(model_name, prompt, stream, **kwargs)"],
        "description": "Tests text generation with various prompts and parameters"
    },
    {
        "page": "906_Test_Chat",
        "icon": "💬",
        "title": "Chat Interface",
        "functions": ["chat(model_name, messages, stream, **kwargs)"],
        "description": "Tests multi-turn chat conversations with system prompts"
    },
    {
        "page": "907_Test_Embeddings",
        "icon": "🔢",
        "title": "Embeddings",
        "functions": ["embeddings(model_name, text, **kwargs)"],
        "description": "Tests embedding generation and similarity comparison"
    }
]

for idx, test in enumerate(tests, 1):
    with st.expander(f"{test['icon']} {idx}. {test['title']}", expanded=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**Description:** {test['description']}")
            st.markdown("**Functions Tested:**")
            for func in test['functions']:
                st.code(func, language='python')
        
        with col2:
            st.markdown(f"**Page:** `{test['page']}.py`")

st.markdown("---")

# Module Functions Summary
st.header("📋 All Functions in helper_ollama")

functions_table = """
| Function | Purpose | Returns |
|----------|---------|---------|
| `check_ollama_status()` | Check if Ollama is running | Dict with status, message, models |
| `get_available_models()` | Get list of model names | List of strings |
| `get_local_llms(func=None)` | Get models, optionally filtered | List of model dicts |
| `get_model_info(model_name)` | Get detailed model info | Model info dict |
| `list_models_by_capability()` | Organize models by capability | Dict with categorized models |
| `generate(model_name, prompt, ...)` | Generate text from prompt | Response object |
| `chat(model_name, messages, ...)` | Chat with model | Response object |
| `embeddings(model_name, text, ...)` | Generate embeddings | Response with embedding vector |
"""

st.markdown(functions_table)

st.markdown("---")

# Capability Types
st.header("🏷️ Model Capability Types")

capabilities = {
    "embedding": {
        "icon": "🔢",
        "description": "Text embedding models that convert text into vector representations",
        "examples": ["nomic-embed-text", "mxbai-embed-large", "all-minilm"],
        "use_cases": ["Semantic search", "Similarity comparison", "Clustering"]
    },
    "vision": {
        "icon": "👁️",
        "description": "Models that can process and understand images",
        "examples": ["llama3.2-vision", "llava", "moondream"],
        "use_cases": ["Image description", "Visual Q&A", "OCR"]
    },
    "tools": {
        "icon": "🔧",
        "description": "Models that support function/tool calling",
        "examples": ["llama3.1", "mistral", "qwen"],
        "use_cases": ["API integration", "Function calling", "Agents"]
    },
    "thinking": {
        "icon": "🧠",
        "description": "Models optimized for reasoning and complex problem solving",
        "examples": ["deepseek-r1", "qwen-reasoning"],
        "use_cases": ["Math problems", "Logic puzzles", "Step-by-step reasoning"]
    },
    "chat": {
        "icon": "💬",
        "description": "General-purpose conversational models",
        "examples": ["llama3.2", "mistral", "phi3"],
        "use_cases": ["Conversations", "Q&A", "Content generation"]
    }
}

for cap_name, cap_info in capabilities.items():
    with st.expander(f"{cap_info['icon']} {cap_name.title()}", expanded=False):
        st.markdown(f"**{cap_info['description']}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Example Models:**")
            for example in cap_info['examples']:
                st.code(f"ollama pull {example}")
        
        with col2:
            st.markdown("**Use Cases:**")
            for use_case in cap_info['use_cases']:
                st.write(f"- {use_case}")

st.markdown("---")

# Getting Started
st.header("🚀 Getting Started")

st.markdown("""
### Prerequisites
1. **Install Ollama:**
   ```bash
   # macOS/Linux
   curl https://ollama.ai/install.sh | sh
   
   # Or visit: https://ollama.ai/download
   ```

2. **Pull some models:**
   ```bash
   # Chat models
   ollama pull llama3.2
   ollama pull mistral
   
   # Vision model
   ollama pull llama3.2-vision
   
   # Embedding model
   ollama pull nomic-embed-text
   ```

3. **Start Ollama server:**
   ```bash
   ollama serve
   ```

### Running Tests
Navigate to each test page using the sidebar to run specific tests.
Each test page is self-contained and can be run independently.
""")

st.markdown("---")

# Footer
st.header("📖 Documentation")
st.markdown("""
- **Module Location:** `lib/helper_ollama/__init__.py`
- **Test Location:** `views/900_🦙_Tests/`
- **Ollama Documentation:** [https://ollama.ai/](https://ollama.ai/)
- **Ollama Python SDK:** [https://github.com/ollama/ollama-python](https://github.com/ollama/ollama-python)
""")

# =================================================================================================
show_code(__file__)
