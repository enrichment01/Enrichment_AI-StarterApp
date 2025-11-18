import streamlit as st

from lib import helper_ollama
from lib import helper_streamlit


st.header("🦙 Ollama Python SDK Basics")
st.markdown("Learn how to use the Ollama Python SDK to interact with local LLMs.")
st.markdown("Use the sidebar to navigate to the individual Ollama lessons (Installation, Basic Usage, Streaming, Generate, Model Management, Advanced Parameters, System Messages, Error Handling).")

# Interactive Example
st.markdown("---")
st.subheader("🎮 Interactive Example: Check Ollama Connection")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("**Test your Ollama setup:**")
    
    if st.button("Check Ollama Status", key="check_ollama"):
        with st.spinner("Checking Ollama..."):
            state = helper_ollama.check_ollama_status()
        
            print(state)


            if state['status'] == 'success':
                st.success(f"✅ {state['message']}")
                st.write(f"Available models: {len(state['models'])}")
                
                if state['models']:
                    st.markdown("**Your Models:**")
                    for model in state['models']:
                        st.write(f"- {model['model']}")
                else:
                    st.info("No models found. Run `ollama pull phi4-mini` to get started!")
            else:
                st.error(f"❌ {state['message']}")
                if 'SDK not installed' not in state['message']:
                    st.info("Make sure Ollama is running. Visit https://ollama.ai for installation.")

with col2:
    st.markdown("**Code:**")
    CODE = """
import ollama

try:
    # List available models
    models = ollama.list()
    
    print("✅ Ollama is running!")
    print(f"Models: {len(models['models'])}")
    
    for model in models['models']:
        print(f"- {model['name']}")
        
except Exception as e:
    print(f"❌ Error: {e}")

"""
    st.code(CODE, language="python")
    helper_streamlit.run_code(CODE)

# Resources
st.markdown("---")
st.subheader("📚 Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Official Docs**")
    st.markdown("[Ollama Documentation](https://github.com/ollama/ollama)")
    st.markdown("[Python SDK](https://github.com/ollama/ollama-python)")

with col2:
    st.markdown("**Popular Models**")
    st.markdown("- phi4-mini")
    st.markdown("- mistral")
    st.markdown("- codellama")
    st.markdown("- phi")

with col3:
    st.markdown("**Quick Commands**")
    st.code("ollama list", language="bash")
    st.code("ollama pull <model>", language="bash")
    st.code("ollama run <model>", language="bash")
