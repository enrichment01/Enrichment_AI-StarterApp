"""
Streamlit Test Page for helper_ollama Module

This page tests all functions from lib/helper_ollama/__init__.py
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.helper_ollama import (
    check_ollama_status,
    get_available_models,
    get_local_llms,
    get_model_info,
    list_models_by_capability,
    generate,
    chat,
    embeddings
)

st.set_page_config(
    page_title="Ollama Helper Test Suite",
    page_icon="🦙",
    layout="wide"
)

st.title("🦙 Ollama Helper Module Test Suite")
st.markdown("Comprehensive testing of all functions in `helper_ollama/__init__.py`")

# Sidebar for test selection
st.sidebar.header("Test Selection")
test_category = st.sidebar.radio(
    "Choose Test Category:",
    [
        "Status & Discovery",
        "Model Filtering",
        "Model Information",
        "Text Generation",
        "Chat Interface",
        "Embeddings",
        "All Tests"
    ]
)

# Initialize session state
if 'test_results' not in st.session_state:
    st.session_state.test_results = {}

def test_function(func_name, test_func):
    """Helper to run and display test results."""
    try:
        result = test_func()
        st.session_state.test_results[func_name] = {
            'status': 'success',
            'result': result
        }
        return True, result
    except Exception as e:
        st.session_state.test_results[func_name] = {
            'status': 'error',
            'error': str(e)
        }
        return False, str(e)

# Test 1: Status & Discovery Tests
if test_category in ["Status & Discovery", "All Tests"]:
    st.header("1️⃣ Status & Discovery Tests")
    
    with st.expander("Test: check_ollama_status()", expanded=True):
        st.code("check_ollama_status()")
        
        if st.button("Run check_ollama_status()", key="btn_status"):
            with st.spinner("Checking Ollama status..."):
                success, result = test_function("check_ollama_status", check_ollama_status)
                
                if success:
                    st.success(f"✅ Status: {result['status']}")
                    st.info(result['message'])
                    if result['models']:
                        st.write(f"**Found {len(result['models'])} models**")
                        st.json(result)
                else:
                    st.error(f"❌ Error: {result}")
    
    with st.expander("Test: get_available_models()", expanded=True):
        st.code("get_available_models()")
        
        if st.button("Run get_available_models()", key="btn_available"):
            with st.spinner("Getting available models..."):
                success, result = test_function("get_available_models", get_available_models)
                
                if success:
                    st.success(f"✅ Found {len(result)} models")
                    if result:
                        st.write("**Available Models:**")
                        for idx, model in enumerate(result, 1):
                            st.write(f"{idx}. `{model}`")
                    else:
                        st.warning("No models found")
                else:
                    st.error(f"❌ Error: {result}")

# Test 2: Model Filtering Tests
if test_category in ["Model Filtering", "All Tests"]:
    st.header("2️⃣ Model Filtering Tests")
    
    with st.expander("Test: get_local_llms() - All Models", expanded=True):
        st.code("get_local_llms()")
        
        if st.button("Run get_local_llms() - All", key="btn_all_models"):
            with st.spinner("Getting all local LLMs..."):
                success, result = test_function("get_local_llms_all", 
                                               lambda: get_local_llms())
                
                if success:
                    st.success(f"✅ Found {len(result)} models")
                    if result:
                        for model in result:
                            with st.container():
                                col1, col2 = st.columns([3, 1])
                                with col1:
                                    st.write(f"**{model['name']}**")
                                    st.write(f"Capabilities: {', '.join(model['capabilities'])}")
                                with col2:
                                    size_mb = model['size'] / (1024 * 1024)
                                    st.metric("Size", f"{size_mb:.1f} MB")
                                st.divider()
                else:
                    st.error(f"❌ Error: {result}")
    
    with st.expander("Test: get_local_llms() - By Function", expanded=True):
        st.code("get_local_llms(func='...')")
        
        func_type = st.selectbox(
            "Select Function Type:",
            ["embedding", "vision", "tools", "thinking", "chat"],
            key="func_select"
        )
        
        if st.button(f"Run get_local_llms(func='{func_type}')", key="btn_filtered"):
            with st.spinner(f"Getting {func_type} models..."):
                success, result = test_function(f"get_local_llms_{func_type}",
                                               lambda: get_local_llms(func=func_type))
                
                if success:
                    st.success(f"✅ Found {len(result)} {func_type} models")
                    if result:
                        for model in result:
                            st.write(f"- **{model['name']}** ({', '.join(model['capabilities'])})")
                    else:
                        st.info(f"No {func_type} models found")
                else:
                    st.error(f"❌ Error: {result}")
    
    with st.expander("Test: list_models_by_capability()", expanded=True):
        st.code("list_models_by_capability()")
        
        if st.button("Run list_models_by_capability()", key="btn_by_capability"):
            with st.spinner("Categorizing models by capability..."):
                success, result = test_function("list_models_by_capability",
                                               list_models_by_capability)
                
                if success:
                    st.success("✅ Models categorized successfully")
                    
                    # Display summary
                    if 'summary' in result:
                        st.subheader("Summary")
                        cols = st.columns(6)
                        summary = result['summary']
                        cols[0].metric("Total", summary['total_models'])
                        cols[1].metric("Embedding", summary['embedding_count'])
                        cols[2].metric("Vision", summary['vision_count'])
                        cols[3].metric("Tools", summary['tools_count'])
                        cols[4].metric("Thinking", summary['thinking_count'])
                        cols[5].metric("Chat", summary['chat_count'])
                    
                    # Display by category
                    st.subheader("Models by Capability")
                    for capability in ["embedding", "vision", "tools", "thinking", "chat"]:
                        with st.expander(f"{capability.title()} Models ({len(result[capability])})"):
                            if result[capability]:
                                for model in result[capability]:
                                    st.write(f"- {model['name']}")
                            else:
                                st.info(f"No {capability} models found")
                else:
                    st.error(f"❌ Error: {result}")

# Test 3: Model Information Tests
if test_category in ["Model Information", "All Tests"]:
    st.header("3️⃣ Model Information Tests")
    
    with st.expander("Test: get_model_info()", expanded=True):
        st.code("get_model_info(model_name)")
        
        # Get available models for selection
        available_models = get_available_models()
        
        if available_models:
            model_name = st.selectbox(
                "Select Model:",
                available_models,
                key="model_info_select"
            )
            
            if st.button(f"Get Info for '{model_name}'", key="btn_model_info"):
                with st.spinner(f"Getting info for {model_name}..."):
                    success, result = test_function(f"get_model_info_{model_name}",
                                                   lambda: get_model_info(model_name))
                    
                    if success:
                        st.success("✅ Model info retrieved")
                        
                        st.subheader("Model Details")
                        st.write(f"**Name:** {result['name']}")
                        st.write(f"**Capabilities:** {', '.join(result['capabilities'])}")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            if result.get('details'):
                                st.write("**Details:**")
                                st.json(result['details'])
                        
                        with col2:
                            if result.get('parameters'):
                                st.write("**Parameters:**")
                                st.code(result['parameters'])
                        
                        if result.get('template'):
                            st.write("**Template:**")
                            st.code(result['template'], language='text')
                        
                        if result.get('system'):
                            st.write("**System Prompt:**")
                            st.code(result['system'], language='text')
                    else:
                        st.error(f"❌ Error: {result}")
        else:
            st.warning("No models available. Please install Ollama models first.")

# Test 4: Text Generation Tests
if test_category in ["Text Generation", "All Tests"]:
    st.header("4️⃣ Text Generation Tests")
    
    with st.expander("Test: generate()", expanded=True):
        st.code("generate(model_name, prompt, stream=False)")
        
        available_models = get_available_models()
        
        if available_models:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                gen_model = st.selectbox(
                    "Select Model:",
                    available_models,
                    key="gen_model_select"
                )
            
            with col2:
                stream_gen = st.checkbox("Stream Response", value=False, key="stream_gen")
            
            gen_prompt = st.text_area(
                "Enter Prompt:",
                value="Write a haiku about programming.",
                height=100,
                key="gen_prompt"
            )
            
            if st.button("Generate Text", key="btn_generate"):
                with st.spinner(f"Generating with {gen_model}..."):
                    def run_generate():
                        return generate(gen_model, gen_prompt, stream=stream_gen)
                    
                    success, result = test_function(f"generate_{gen_model}", run_generate)
                    
                    if success:
                        st.success("✅ Generation completed")
                        
                        if hasattr(result, 'response'):
                            st.subheader("Response:")
                            st.markdown(result.response)
                            
                            with st.expander("Full Response Details"):
                                st.json({
                                    'model': result.model,
                                    'created_at': result.created_at,
                                    'done': result.done,
                                    'total_duration': getattr(result, 'total_duration', 'N/A'),
                                })
                        else:
                            st.write(result)
                    else:
                        st.error(f"❌ Error: {result}")
        else:
            st.warning("No models available.")

# Test 5: Chat Interface Tests
if test_category in ["Chat Interface", "All Tests"]:
    st.header("5️⃣ Chat Interface Tests")
    
    with st.expander("Test: chat()", expanded=True):
        st.code("chat(model_name, messages, stream=False)")
        
        available_models = get_available_models()
        
        if available_models:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                chat_model = st.selectbox(
                    "Select Model:",
                    available_models,
                    key="chat_model_select"
                )
            
            with col2:
                stream_chat = st.checkbox("Stream Response", value=False, key="stream_chat")
            
            chat_prompt = st.text_area(
                "Enter Message:",
                value="What is the meaning of life?",
                height=100,
                key="chat_prompt"
            )
            
            system_prompt = st.text_input(
                "System Prompt (optional):",
                value="You are a helpful assistant.",
                key="system_prompt"
            )
            
            if st.button("Send Chat Message", key="btn_chat"):
                with st.spinner(f"Chatting with {chat_model}..."):
                    messages = []
                    
                    if system_prompt:
                        messages.append({"role": "system", "content": system_prompt})
                    
                    messages.append({"role": "user", "content": chat_prompt})
                    
                    def run_chat():
                        return chat(chat_model, messages, stream=stream_chat)
                    
                    success, result = test_function(f"chat_{chat_model}", run_chat)
                    
                    if success:
                        st.success("✅ Chat completed")
                        
                        if hasattr(result, 'message'):
                            st.subheader("Response:")
                            st.markdown(result.message.content)
                            
                            with st.expander("Message Details"):
                                st.json({
                                    'role': result.message.role,
                                    'model': result.model,
                                    'created_at': result.created_at,
                                    'done': result.done,
                                })
                        else:
                            st.write(result)
                    else:
                        st.error(f"❌ Error: {result}")
        else:
            st.warning("No models available.")

# Test 6: Embeddings Tests
if test_category in ["Embeddings", "All Tests"]:
    st.header("6️⃣ Embeddings Tests")
    
    with st.expander("Test: embeddings()", expanded=True):
        st.code("embeddings(model_name, text)")
        
        # Get embedding models
        try:
            embed_models = get_local_llms(func="embedding")
            embed_model_names = [m['name'] for m in embed_models]
        except Exception:
            embed_model_names = []
        
        if embed_model_names:
            embed_model = st.selectbox(
                "Select Embedding Model:",
                embed_model_names,
                key="embed_model_select"
            )
            
            embed_text = st.text_area(
                "Enter Text:",
                value="Artificial intelligence is transforming the world.",
                height=100,
                key="embed_text"
            )
            
            if st.button("Generate Embeddings", key="btn_embeddings"):
                with st.spinner(f"Generating embeddings with {embed_model}..."):
                    def run_embeddings():
                        return embeddings(embed_model, embed_text)
                    
                    success, result = test_function(f"embeddings_{embed_model}", run_embeddings)
                    
                    if success:
                        st.success("✅ Embeddings generated")
                        
                        if hasattr(result, 'embedding'):
                            embedding_vector = result.embedding
                            st.write(f"**Embedding Dimension:** {len(embedding_vector)}")
                            st.write(f"**First 10 values:** {embedding_vector[:10]}")
                            
                            with st.expander("Full Embedding Vector"):
                                st.code(str(embedding_vector))
                        else:
                            st.write(result)
                    else:
                        st.error(f"❌ Error: {result}")
        else:
            st.warning("No embedding models found. Please install an embedding model like 'nomic-embed-text'.")
            st.code("ollama pull nomic-embed-text")

# Test Results Summary
st.sidebar.markdown("---")
st.sidebar.header("Test Results Summary")

if st.session_state.test_results:
    success_count = sum(1 for r in st.session_state.test_results.values() if r['status'] == 'success')
    error_count = sum(1 for r in st.session_state.test_results.values() if r['status'] == 'error')
    
    st.sidebar.metric("Total Tests Run", len(st.session_state.test_results))
    st.sidebar.metric("Successful", success_count)
    st.sidebar.metric("Errors", error_count)
    
    if st.sidebar.button("Clear Results"):
        st.session_state.test_results = {}
        st.rerun()
else:
    st.sidebar.info("No tests run yet")

# Footer
st.markdown("---")
st.markdown("""
### 📚 Tested Functions:
- `check_ollama_status()` - Check Ollama service status
- `get_available_models()` - List all available models
- `get_local_llms(func=None)` - Get models with optional filtering
- `get_model_info(model_name)` - Get detailed model information
- `list_models_by_capability()` - Organize models by capability
- `generate(model_name, prompt)` - Generate text
- `chat(model_name, messages)` - Chat with model
- `embeddings(model_name, text)` - Generate embeddings
""")
