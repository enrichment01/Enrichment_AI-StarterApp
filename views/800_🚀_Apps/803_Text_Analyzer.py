import streamlit as st

from lib import helper_streamlit
from lib.helper_chat import utils

import lib.helper_text.generator as text_generator
import lib.helper_text.analyzer as text_analyzer

st.header("🚀 Ollama AI MiniApps")
st.markdown("Complete mini-applications powered by Ollama.")

st.subheader("🔍 AI Text Analyzer")
st.markdown("Analyze text with AI-powered insights.")

col1, col2 = st.columns([2, 1])

with col1:
    text_to_analyze = st.text_area(
        "Enter text to analyze:",
        placeholder="Paste any text here...",
        height=200,
        key="analyze_text"
    )
    
    analysis_type = st.selectbox(
        "Analysis Type:",
        [
            "Summarize",
            "Extract Key Points",
            "Sentiment Analysis",
            "Find Main Topics",
            "Translate to Simple Language",
            "Grammar Check"
        ],
        key="analysis_type"
    )
    
    model = st.selectbox(
        "Model:",
        ["phi4-mini", "mistral", "phi"],
        key="analyze_model"
    )
    
    if st.button("🔍 Analyze", key="analyze_btn", type="primary"):
        if not text_to_analyze:
            st.warning("Please enter text to analyze!")
        else:
            with st.spinner(f"Analyzing with {model}..."):
                result = text_analyzer.analyze_text(
                    model=model,
                    text=text_to_analyze,
                    analysis_type=analysis_type
                )
                
                if result['status'] == 'success':
                    st.success("✅ Analysis Complete!")
                    st.markdown("### Result:")
                    st.write(result['response'])
                    
                    # Show stats
                    with st.expander("📊 Analysis Stats"):
                        for key, value in result['stats'].items():
                            st.write(f"**{key.replace('_', ' ').title()}:** {value}")
                else:
                    st.error(f"❌ {result['message']}")

with col2:
    st.markdown("### 📝 Sample Texts")
    
    for title in text_analyzer.SAMPLE_TEXTS.keys():
        if st.button(f"Load: {title}", key=f"sample_{title}"):
            st.session_state.analyze_text = text_analyzer.get_sample_text(title)
            st.rerun()
