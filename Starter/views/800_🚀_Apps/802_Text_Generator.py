import streamlit as st

from lib import helper_streamlit
from lib.helper_chat import utils

import lib.helper_text.generator as text_generator
import lib.helper_text.analyzer as text_analyzer

st.header("🚀 Ollama AI MiniApps")
st.markdown("Complete mini-applications powered by Ollama.")

st.subheader("📝 AI Text Generator")
st.markdown("Generate creative text using Ollama models.")

col1, col2 = st.columns([2, 1])

with col1:
    # User inputs
    prompt = st.text_area(
        "Enter your prompt:",
        placeholder="Write a short story about a robot learning to paint...",
        height=100
    )
    
    col_a, col_b = st.columns(2)
    with col_a:
        model = st.selectbox(
            "Select Model:",
            ["phi4-mini", "mistral", "codellama", "phi"],
            key="gen_model"
        )
    
    with col_b:
        temperature = st.slider(
            "Creativity (Temperature):",
            0.0, 2.0, 0.7, 0.1,
            key="gen_temp"
        )
    
    max_tokens = st.slider(
        "Max Length (tokens):",
        50, 500, 200,
        key="gen_tokens"
    )
    
    if st.button("✨ Generate", key="generate_btn", type="primary"):
        if not prompt:
            st.warning("Please enter a prompt!")
        else:
            with st.spinner(f"Generating with {model}..."):
                result = text_generator.generate_text(
                    model=model,
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                
                if result['status'] == 'success':
                    st.success("✅ Generated!")
                    st.markdown("### Result:")
                    st.write(result['response'])
                    
                    # Show stats
                    with st.expander("📊 Generation Stats"):
                        for key, value in result['stats'].items():
                            st.write(f"**{key.replace('_', ' ').title()}:** {value}")
                else:
                    st.error(f"❌ {result['message']}")

with col2:
    st.markdown("### 💡 Tips")
    st.info("""
    **Prompt Tips:**
    - Be specific and clear
    - Provide context
    - Use examples if needed
    
    **Temperature:**
    - 0.0-0.3: Focused, deterministic
    - 0.4-0.7: Balanced
    - 0.8-2.0: Creative, random
    
    **Models:**
    - phi4-mini: General purpose
    - mistral: Fast, efficient
    - codellama: For code
    - phi: Lightweight
    """)

