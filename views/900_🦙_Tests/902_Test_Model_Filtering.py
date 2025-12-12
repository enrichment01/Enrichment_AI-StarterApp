"""
Test: get_local_llms() - Model Filtering

Tests the model filtering function with different capability types.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import get_local_llms
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Model Filtering",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Test: get_local_llms() - Model Filtering")
st.markdown("Testing `get_local_llms()` with different capability filters")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

# Create tabs
tabs = st.tabs(["All Models", "Filter by Capability", "Error Handling", "Summary"])

# Test 1: Get all models
with tabs[0]:
    st.header("Test: get_local_llms() - All Models")
st.code("from lib.helper_ollama import get_local_llms\nmodels = get_local_llms()")

if st.button("Run get_local_llms() - Get All Models", key="btn_all"):
    with st.spinner("Getting all local LLMs..."):
        try:
            models = get_local_llms()
            
            st.success(f"✅ Found {len(models)} models")
            
            if models:
                st.subheader("All Local Models:")
                
                for model in models:
                    with st.expander(f"📦 {model['name']}", expanded=False):
                        col1, col2 = st.columns([2, 1])
                        
                        with col1:
                            st.write(f"**Capabilities:** {', '.join(model['capabilities'])}")
                            st.write(f"**Digest:** `{model['digest'][:32]}...`")
                        
                        with col2:
                            size_mb = model['size'] / (1024 * 1024)
                            st.metric("Size", f"{size_mb:.1f} MB")
                        
                        if model.get('details'):
                            with st.expander("Model Details"):
                                st.json(model['details'])
            else:
                st.warning("No models found")
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Test 2: Filter by capability
with tabs[1]:
    st.header("Test: get_local_llms(func=...) - Filter by Capability")

capability_descriptions = {
    "embedding": "Text embedding models (vector representations)",
    "vision": "Vision/image processing models",
    "tools": "Tool/function calling models",
    "thinking": "Reasoning/thinking models",
    "chat": "General chat/conversation models"
}

col1, col2 = st.columns([1, 2])

with col1:
    func_type = st.selectbox(
        "Select Capability:",
        ["embedding", "vision", "tools", "thinking", "chat"],
        key="func_select"
    )

with col2:
    st.info(f"**{func_type.title()}:** {capability_descriptions[func_type]}")

st.code(f"from lib.helper_ollama import get_local_llms\nmodels = get_local_llms(func='{func_type}')")

if st.button(f"Run get_local_llms(func='{func_type}')", key="btn_filtered"):
    with st.spinner(f"Getting {func_type} models..."):
        try:
            models = get_local_llms(func=func_type)
            
            if models:
                st.success(f"✅ Found {len(models)} {func_type} models")
                
                st.subheader(f"{func_type.title()} Models:")
                
                for idx, model in enumerate(models, 1):
                    st.write(f"{idx}. **{model['name']}**")
                    st.write(f"   - Capabilities: {', '.join(model['capabilities'])}")
                    st.write(f"   - Size: {model['size'] / (1024*1024):.1f} MB")
                    st.write("")
            else:
                st.info(f"ℹ️ No {func_type} models found")
                
                # Suggestions
                if func_type == "embedding":
                    st.code("ollama pull nomic-embed-text")
                elif func_type == "vision":
                    st.code("ollama pull llama3.2-vision")
                elif func_type == "thinking":
                    st.code("ollama pull deepseek-r1")
                else:
                    st.code("ollama pull llama3.2")
                    
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Test 3: Test invalid input
with tabs[2]:
    st.header("Test: Error Handling - Invalid Function Type")
st.code("models = get_local_llms(func='invalid')")

if st.button("Test Invalid Function Type", key="btn_invalid"):
    try:
        models = get_local_llms(func='invalid')
        st.error("❌ Should have raised ValueError!")
    except ValueError as e:
        st.success(f"✅ Correctly raised ValueError: {str(e)}")
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")

# Summary
with tabs[3]:
    st.header("📊 Summary")
st.markdown("""
### Function Tested:
- ✅ `get_local_llms(func=None)` - Get all models or filter by capability

### Capability Types:
- `embedding` - Text embedding models
- `vision` - Vision/image processing models
- `tools` - Tool/function calling models
- `thinking` - Reasoning/thinking models
- `chat` - General chat/conversation models

### Expected Behavior:
- Returns list of model dictionaries with name, size, capabilities, etc.
- When `func=None`, returns all models with detected capabilities
- When `func` is specified, returns only models supporting that capability
- Raises `ValueError` for invalid function types
""")

# =================================================================================================
show_code(__file__)
