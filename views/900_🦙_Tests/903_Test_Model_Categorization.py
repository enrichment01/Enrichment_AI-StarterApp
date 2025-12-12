"""
Test: list_models_by_capability()

Tests the capability categorization function.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import list_models_by_capability
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Model Categorization",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Test: list_models_by_capability()")
st.markdown("Testing model categorization by capability")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

# Create tabs
tabs = st.tabs(["Test Function", "Summary"])

with tabs[0]:
    st.header("Test: list_models_by_capability()")
st.code("from lib.helper_ollama import list_models_by_capability\ncategorized = list_models_by_capability()")

if st.button("Run list_models_by_capability()", key="btn_categorize"):
    with st.spinner("Categorizing models by capability..."):
        try:
            result = list_models_by_capability()
            
            # Display summary metrics
            if 'summary' in result:
                st.success("✅ Models categorized successfully")
                
                st.subheader("📊 Summary Statistics")
                
                cols = st.columns(6)
                summary = result['summary']
                
                cols[0].metric("Total Models", summary['total_models'])
                cols[1].metric("Embedding", summary['embedding_count'], help="Text embedding models")
                cols[2].metric("Vision", summary['vision_count'], help="Image processing models")
                cols[3].metric("Tools", summary['tools_count'], help="Function calling models")
                cols[4].metric("Thinking", summary['thinking_count'], help="Reasoning models")
                cols[5].metric("Chat", summary['chat_count'], help="Chat models")
                
                st.divider()
                
                # Display models by category
                st.subheader("🗂️ Models by Capability")
                
                capability_icons = {
                    "embedding": "🔢",
                    "vision": "👁️",
                    "tools": "🔧",
                    "thinking": "🧠",
                    "chat": "💬"
                }
                
                capability_descriptions = {
                    "embedding": "Text embedding models for vector representations",
                    "vision": "Vision/image processing models",
                    "tools": "Tool/function calling models",
                    "thinking": "Reasoning/thinking models",
                    "chat": "General chat/conversation models"
                }
                
                for capability in ["embedding", "vision", "tools", "thinking", "chat"]:
                    icon = capability_icons.get(capability, "📦")
                    count = len(result[capability])
                    
                    with st.expander(f"{icon} {capability.title()} Models ({count})", expanded=(count > 0)):
                        st.markdown(f"*{capability_descriptions[capability]}*")
                        
                        if result[capability]:
                            for model in result[capability]:
                                col1, col2 = st.columns([3, 1])
                                
                                with col1:
                                    st.write(f"**{model['name']}**")
                                    all_caps = ', '.join(model['capabilities'])
                                    st.caption(f"All capabilities: {all_caps}")
                                
                                with col2:
                                    size_mb = model['size'] / (1024 * 1024)
                                    st.caption(f"Size: {size_mb:.1f} MB")
                                
                                st.markdown("---")
                        else:
                            st.info(f"No {capability} models found")
                            
                            # Installation suggestions
                            if capability == "embedding":
                                st.code("ollama pull nomic-embed-text")
                            elif capability == "vision":
                                st.code("ollama pull llama3.2-vision")
                            elif capability == "thinking":
                                st.code("ollama pull deepseek-r1")
                
                st.divider()
                
                # Full JSON view
                with st.expander("📄 Full Response (JSON)"):
                    st.json(result)
                    
            else:
                st.warning("No summary found in response")
                st.json(result)
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            import traceback
            with st.expander("Error Details"):
                st.code(traceback.format_exc())

# Summary
with tabs[1]:
    st.header("📊 Summary")
st.markdown("""
### Function Tested:
- ✅ `list_models_by_capability()` - Organize all models by capability

### Returns:
A dictionary with:
- **embedding**: List of embedding models
- **vision**: List of vision models
- **tools**: List of tool-calling models
- **thinking**: List of reasoning models
- **chat**: List of chat models
- **summary**: Dictionary with counts for each category

### Expected Behavior:
- Scans all local models and categorizes them
- A model can appear in multiple categories if it has multiple capabilities
- Provides summary statistics
- Graceful error handling if Ollama is not accessible
""")

# =================================================================================================
show_code(__file__)
