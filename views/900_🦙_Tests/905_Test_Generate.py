"""
Test: generate()

Tests text generation with Ollama models.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import generate, get_available_models
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Text Generation",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ Test: generate()")
st.markdown("Testing text generation with Ollama models")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

    stream_mode = st.checkbox("Stream Response", value=False, key="stream_mode")

# Create tabs
tabs = st.tabs(["Generate", "Summary"])

with tabs[0]:
    st.header("Test: generate(model_name, prompt, stream=False)")

# Get available models
with st.spinner("Loading available models..."):
    try:
        available_models = get_available_models()
    except Exception as e:
        st.error(f"Error loading models: {str(e)}")
        available_models = []

if available_models:
    # Prompt input
    st.subheader("📝 Prompt")
    
    prompt_examples = {
        "Haiku": "Write a haiku about programming.",
        "Story": "Write a short story about a robot learning to paint.",
        "Explanation": "Explain quantum computing in simple terms.",
        "Code": "Write a Python function to calculate fibonacci numbers.",
        "List": "List 5 benefits of reading books.",
        "Custom": ""
    }
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        prompt_type = st.selectbox(
            "Example Prompts:",
            list(prompt_examples.keys()),
            key="prompt_type"
        )
    
    with col2:
        if prompt_type == "Custom":
            prompt_value = ""
        else:
            prompt_value = prompt_examples[prompt_type]
    
    prompt = st.text_area(
        "Enter Prompt:",
        value=prompt_value,
        height=100,
        key="prompt_input"
    )
    
    # Advanced parameters
    with st.expander("⚙️ Advanced Parameters"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.1, key="temp")
            st.caption("Higher = more creative")
        
        with col2:
            top_p = st.slider("Top P", 0.0, 1.0, 0.9, 0.1, key="top_p")
            st.caption("Nucleus sampling")
        
        with col3:
            top_k = st.slider("Top K", 0, 100, 40, 5, key="top_k")
            st.caption("Token sampling")
    
    # Generate code preview
    code_preview = f"""from lib.helper_ollama import generate

result = generate(
    model_name='{selected_model}',
    prompt='''{prompt}''',
    stream={stream_mode},
    temperature={temperature},
    top_p={top_p},
    top_k={top_k}
)
"""
    
    with st.expander("👀 Code Preview"):
        st.code(code_preview, language='python')
    
    # Generate button
    if st.button("🚀 Generate Text", key="btn_generate", type="primary"):
        if not prompt:
            st.warning("Please enter a prompt")
        else:
            with st.spinner(f"Generating with {model_name}..."):
                try:
                    result = generate(
                        model_name=selected_model,
                        prompt=prompt,
                        stream=stream_mode,
                        temperature=temperature,
                        top_p=top_p,
                        top_k=top_k
                    )
                    
                    st.success("✅ Generation completed!")
                    
                    # Display response
                    st.subheader("📄 Response")
                    
                    if hasattr(result, 'response'):
                        st.markdown(result.response)
                        
                        # Metadata
                        st.divider()
                        st.subheader("📊 Metadata")
                        
                        col1, col2, col3, col4 = st.columns(4)
                        
                        with col1:
                            st.metric("Model", result.model)
                        
                        with col2:
                            if hasattr(result, 'total_duration'):
                                duration_sec = result.total_duration / 1e9
                                st.metric("Duration", f"{duration_sec:.2f}s")
                        
                        with col3:
                            if hasattr(result, 'eval_count'):
                                st.metric("Tokens", result.eval_count)
                        
                        with col4:
                            if hasattr(result, 'eval_count') and hasattr(result, 'eval_duration'):
                                tokens_per_sec = result.eval_count / (result.eval_duration / 1e9)
                                st.metric("Tokens/sec", f"{tokens_per_sec:.1f}")
                        
                        # Full response details
                        with st.expander("🔍 Full Response Details"):
                            response_dict = {
                                'model': result.model,
                                'response': result.response,
                                'created_at': result.created_at,
                                'done': result.done,
                            }
                            
                            if hasattr(result, 'total_duration'):
                                response_dict['total_duration'] = result.total_duration
                            if hasattr(result, 'load_duration'):
                                response_dict['load_duration'] = result.load_duration
                            if hasattr(result, 'prompt_eval_count'):
                                response_dict['prompt_eval_count'] = result.prompt_eval_count
                            if hasattr(result, 'prompt_eval_duration'):
                                response_dict['prompt_eval_duration'] = result.prompt_eval_duration
                            if hasattr(result, 'eval_count'):
                                response_dict['eval_count'] = result.eval_count
                            if hasattr(result, 'eval_duration'):
                                response_dict['eval_duration'] = result.eval_duration
                            
                            st.json(response_dict)
                    else:
                        st.write(result)
                        
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
    ollama pull phi3
    ```
    """)

# Summary
with tabs[1]:
    st.header("📊 Summary")
st.markdown("""
### Function Tested:
- ✅ `generate(model_name, prompt, stream=False, **kwargs)` - Generate text from a prompt

### Parameters:
- **model_name**: Name of the Ollama model to use
- **prompt**: The text prompt to generate from
- **stream**: Whether to stream the response (True/False)
- **kwargs**: Additional parameters like temperature, top_p, top_k, etc.

### Returns:
A response object containing:
- **response**: The generated text
- **model**: Model name used
- **created_at**: Timestamp
- **done**: Whether generation is complete
- **total_duration**: Total time in nanoseconds
- **eval_count**: Number of tokens generated
- **eval_duration**: Generation time in nanoseconds

### Expected Behavior:
- Generates text based on the prompt
- Supports various parameter tuning (temperature, top_p, top_k)
- Can stream responses or return complete text
- Returns detailed timing and token metrics
""")

# =================================================================================================
show_code(__file__)
