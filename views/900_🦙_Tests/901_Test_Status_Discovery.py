"""
Test: check_ollama_status() and get_available_models()

Tests the status and discovery functions from helper_ollama module.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import check_ollama_status, get_available_models
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Status & Discovery",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Test: Status & Discovery Functions")
st.markdown("Testing `check_ollama_status()` and `get_available_models()`")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

# Create tabs
tabs = st.tabs(["check_ollama_status()", "get_available_models()", "Summary"])

# Test 1: check_ollama_status()
with tabs[0]:
    st.header("Test: check_ollama_status()")
st.code("from lib.helper_ollama import check_ollama_status\nresult = check_ollama_status()")

if st.button("Run check_ollama_status()", key="btn_status"):
    with st.spinner("Checking Ollama status..."):
        try:
            result = check_ollama_status()
            
            st.success(f"✅ Status: {result['status']}")
            st.info(result['message'])
            
            if result['models']:
                st.write(f"**Found {len(result['models'])} models**")
                
                # Display model information
                for idx, model in enumerate(result['models'], 1):
                    with st.expander(f"Model {idx}: {model.model}"):
                        st.write(f"**Name:** {model.model}")
                        st.write(f"**Size:** {model.size / (1024*1024):.1f} MB")
                        st.write(f"**Modified:** {model.modified_at}")
                        if hasattr(model, 'details'):
                            st.json(model.details)
            
            with st.expander("Full Response"):
                st.json({
                    'status': result['status'],
                    'message': result['message'],
                    'model_count': len(result['models'])
                })
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Test 2: get_available_models()
with tabs[1]:
    st.header("Test: get_available_models()")
st.code("from lib.helper_ollama import get_available_models\nmodels = get_available_models()")

if st.button("Run get_available_models()", key="btn_available"):
    with st.spinner("Getting available models..."):
        try:
            models = get_available_models()
            
            if models:
                st.success(f"✅ Found {len(models)} models")
                
                st.subheader("Available Models:")
                for idx, model in enumerate(models, 1):
                    st.write(f"{idx}. `{model}`")
                
                with st.expander("Model List as JSON"):
                    st.json(models)
            else:
                st.warning("⚠️ No models found. Please install Ollama models first.")
                st.code("ollama pull llama3.2")
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Summary
with tabs[2]:
    st.header("📊 Summary")
st.markdown("""
### Functions Tested:
- ✅ `check_ollama_status()` - Checks if Ollama is running and returns model list
- ✅ `get_available_models()` - Returns list of model names

### Expected Behavior:
- Both functions should return data when Ollama is running
- `check_ollama_status()` returns a dict with status, message, and models
- `get_available_models()` returns a list of model name strings
- Graceful error handling when Ollama is not running
""")

# =================================================================================================
show_code(__file__)
