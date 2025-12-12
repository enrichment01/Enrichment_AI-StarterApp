"""
Test: get_model_info()

Tests retrieving detailed information about a specific model.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import get_model_info, get_available_models
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Model Information",
    page_icon="ℹ",
    layout="wide"
)

st.title("ℹ️ Test: get_model_info()")
st.markdown("Testing detailed model information retrieval")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

# Create tabs
tabs = st.tabs(["Test with Selector", "Test Manual Input", "Summary"])

with tabs[0]:
    st.header("Test: get_model_info(model_name)")

# Get available models
with st.spinner("Loading available models..."):
    try:
        available_models = get_available_models()
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        available_models = []

if available_models:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        model_name = st.selectbox(
            "Select Model:",
            available_models,
            key="model_select"
        )
    
    with col2:
        st.info(f"Selected: `{model_name}`")
    
    st.code(f"from lib.helper_ollama import get_model_info\ninfo = get_model_info('{model_name}')")
    
    if st.button(f"Get Info for '{model_name}'", key="btn_get_info"):
        with st.spinner(f"Getting detailed information for {model_name}..."):
            try:
                result = get_model_info(model_name)
                
                st.success("✅ Model information retrieved successfully")
                
                # Basic Information
                st.subheader("📋 Basic Information")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Name:** `{result['name']}`")
                    if result['capabilities']:
                        st.write("**Capabilities:**")
                        for cap in result['capabilities']:
                            st.write(f"  - {cap}")
                
                with col2:
                    if result.get('details'):
                        details = result['details']
                        if isinstance(details, dict):
                            st.write("**Model Details:**")
                            for key, value in details.items():
                                st.write(f"  - {key}: {value}")
                
                st.divider()
                
                # Details Section
                if result.get('details'):
                    with st.expander("🔍 Model Details", expanded=True):
                        st.json(result['details'])
                
                # Parameters Section
                if result.get('parameters'):
                    with st.expander("⚙️ Parameters", expanded=False):
                        st.code(result['parameters'], language='text')
                
                # Template Section
                if result.get('template'):
                    with st.expander("📝 Prompt Template", expanded=False):
                        st.code(result['template'], language='text')
                        st.caption("This template defines how prompts are formatted for the model")
                
                # System Prompt Section
                if result.get('system'):
                    with st.expander("🤖 System Prompt", expanded=False):
                        st.code(result['system'], language='text')
                        st.caption("Default system prompt for the model")
                
                # Modelfile Section
                if result.get('modelfile'):
                    with st.expander("📄 Modelfile", expanded=False):
                        st.code(result['modelfile'], language='text')
                        st.caption("Complete Modelfile configuration")
                
                st.divider()
                
                # Full Response
                with st.expander("📦 Complete Response (JSON)"):
                    st.json(result)
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                import traceback
                with st.expander("Error Details"):
                    st.code(traceback.format_exc())
else:
    st.warning("⚠️ No models available")
    st.markdown("""
    Please install Ollama models first:
    ```bash
    ollama pull llama3.2
    ollama pull mistral
    ollama pull nomic-embed-text
    ```
    """)

# Test with manual input
with tabs[1]:
    st.header("Test with Manual Input")
st.markdown("Test with a model name that may not be in the list")

manual_model = st.text_input(
    "Enter Model Name:",
    value="llama3.2",
    key="manual_model"
)

if st.button(f"Get Info for '{manual_model}'", key="btn_manual"):
    with st.spinner(f"Getting information for {manual_model}..."):
        try:
            result = get_model_info(manual_model)
            st.success("✅ Success!")
            
            with st.expander("Model Information", expanded=True):
                st.json(result)
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Make sure the model is installed: `ollama pull " + manual_model + "`")

# Summary
with tabs[2]:
    st.header("📊 Summary")
st.markdown("""
### Function Tested:
- ✅ `get_model_info(model_name)` - Get detailed information about a specific model

### Returns:
A dictionary containing:
- **name**: Model name
- **capabilities**: List of detected capabilities (embedding, vision, tools, thinking, chat)
- **details**: Model metadata (format, family, parameter size, etc.)
- **modelfile**: Complete Modelfile configuration
- **parameters**: Model parameters (temperature, context length, etc.)
- **template**: Prompt template used by the model
- **system**: Default system prompt

### Expected Behavior:
- Returns comprehensive information about the model
- Detects capabilities based on model name
- Provides template and configuration details
- Raises exception if model is not found
""")

# =================================================================================================
show_code(__file__)
