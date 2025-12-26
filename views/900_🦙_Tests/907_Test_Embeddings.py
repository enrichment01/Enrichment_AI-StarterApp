"""
Test: embeddings()

Tests embedding generation with Ollama embedding models.
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_ollama import embeddings as ollama_embeddings, get_local_llms
from lib.helper_streamlit import show_code, add_select_model

st.set_page_config(
    page_title="Test: Embeddings",
    page_icon="🔢",
    layout="wide"
)

st.title("🔢 Test: embeddings()")
st.markdown("Testing embedding generation with Ollama embedding models")

# Sidebar
with st.sidebar:
    st.header("Configuration")
    selected_model = add_select_model()
    st.info(f"Selected model: `{selected_model}`")

# Create tabs
tabs = st.tabs(["Generate Embeddings", "Compare Embeddings", "Summary"])

with tabs[0]:
    st.header("Test: embeddings(model_name, text)")

    # Get embedding models
    with st.spinner("Loading embedding models..."):
        try:
            embed_models = get_local_llms(func="embedding")
            embed_model_names = [m['name'] for m in embed_models]
        except Exception as e:
            st.error(f"Error loading models: {str(e)}")
            embed_model_names = []

    if embed_model_names:
        # Model selection
        col1, col2 = st.columns([2, 1])
        
        with col1:
            model_name = st.selectbox(
                "Select Embedding Model:",
                embed_model_names,
                key="model_select"
            )
        
        with col2:
            st.info(f"Model: `{model_name}`")
        
        # Text input
        st.subheader("📝 Input Text")
        
        text_examples = {
            "Short": "Artificial intelligence is transforming the world.",
            "Medium": "Machine learning algorithms can identify patterns in large datasets. Neural networks are particularly effective for complex tasks like image recognition and natural language processing.",
            "Technical": "The transformer architecture uses self-attention mechanisms to process sequential data in parallel, enabling efficient training of large language models.",
            "Question": "What is the capital of France?",
            "Code": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
            "Custom": ""
        }
        
        col1, col2 = st.columns([1, 3])
        
        with col1:
            text_type = st.selectbox(
                "Example Texts:",
                list(text_examples.keys()),
                key="text_type"
            )
        
        with col2:
            text_value = "" if text_type == "Custom" else text_examples[text_type]
        
        input_text = st.text_area(
            "Enter Text:",
            value=text_value,
            height=150,
            key="input_text"
        )
        
        # Code preview
        code_preview = f"""from lib.helper_ollama import embeddings

    result = embeddings(
        model_name='{model_name}',
        text='''{input_text}'''
    )

    embedding_vector = result.embedding
    print(f"Dimension: {{len(embedding_vector)}}")
    """
        
        with st.expander("👀 Code Preview"):
            st.code(code_preview, language='python')
        
        # Generate embeddings button
        if st.button("🚀 Generate Embeddings", key="btn_embed", type="primary"):
            if not input_text:
                st.warning("Please enter text")
            else:
                with st.spinner(f"Generating embeddings with {model_name}..."):
                    try:
                        result = ollama_embeddings(
                            model_name=model_name,
                            text=input_text
                        )
                        
                        st.success("✅ Embeddings generated successfully!")
                        
                        if hasattr(result, 'embedding'):
                            embedding_vector = result.embedding
                            
                            # Display basic info
                            st.subheader("📊 Embedding Information")
                            
                            col1, col2, col3, col4 = st.columns(4)
                            
                            with col1:
                                st.metric("Dimension", len(embedding_vector))
                            
                            with col2:
                                min_val = min(embedding_vector)
                                st.metric("Min Value", f"{min_val:.4f}")
                            
                            with col3:
                                max_val = max(embedding_vector)
                                st.metric("Max Value", f"{max_val:.4f}")
                            
                            with col4:
                                mean_val = sum(embedding_vector) / len(embedding_vector)
                                st.metric("Mean", f"{mean_val:.4f}")
                            
                            # Visualize first values
                            st.subheader("🔍 First 20 Values")
                            first_20 = embedding_vector[:20]
                            
                            col1, col2 = st.columns([1, 2])
                            
                            with col1:
                                for i, val in enumerate(first_20):
                                    st.text(f"[{i:2d}] {val:8.5f}")
                            
                            with col2:
                                # Simple bar chart
                                st.bar_chart(first_20)
                            
                            # Statistics
                            st.subheader("📈 Statistics")
                            
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.write("**Basic Statistics:**")
                                stats = {
                                    "Dimension": len(embedding_vector),
                                    "Min": min(embedding_vector),
                                    "Max": max(embedding_vector),
                                    "Mean": sum(embedding_vector) / len(embedding_vector),
                                    "Sum": sum(embedding_vector),
                                }
                                
                                # Calculate std dev
                                mean = stats["Mean"]
                                variance = sum((x - mean) ** 2 for x in embedding_vector) / len(embedding_vector)
                                stats["Std Dev"] = variance ** 0.5
                                
                                # Calculate L2 norm
                                l2_norm = sum(x**2 for x in embedding_vector) ** 0.5
                                stats["L2 Norm"] = l2_norm
                                
                                for key, value in stats.items():
                                    if isinstance(value, (int, float)):
                                        st.write(f"- {key}: `{value:.6f}`")
                                    else:
                                        st.write(f"- {key}: `{value}`")
                            
                            with col2:
                                st.write("**Value Distribution:**")
                                
                                # Count values in ranges
                                ranges = [
                                    ("< -0.5", lambda x: x < -0.5),
                                    ("-0.5 to -0.1", lambda x: -0.5 <= x < -0.1),
                                    ("-0.1 to 0", lambda x: -0.1 <= x < 0),
                                    ("0 to 0.1", lambda x: 0 <= x < 0.1),
                                    ("0.1 to 0.5", lambda x: 0.1 <= x < 0.5),
                                    (">= 0.5", lambda x: x >= 0.5)
                                ]
                                
                                for label, condition in ranges:
                                    count = sum(1 for x in embedding_vector if condition(x))
                                    percentage = (count / len(embedding_vector)) * 100
                                    st.write(f"- {label}: {count} ({percentage:.1f}%)")
                            
                            # Full vector
                            with st.expander("📄 Full Embedding Vector"):
                                st.text(f"Dimension: {len(embedding_vector)}")
                                st.code(str(embedding_vector), language='python')
                            
                            # Response details
                            with st.expander("🔍 Response Details"):
                                response_dict = {}
                                
                                if hasattr(result, 'model'):
                                    response_dict['model'] = result.model
                                
                                response_dict['embedding_dimension'] = len(embedding_vector)
                                response_dict['embedding_preview'] = embedding_vector[:10]
                                
                                if hasattr(result, 'total_duration'):
                                    response_dict['total_duration'] = result.total_duration
                                if hasattr(result, 'load_duration'):
                                    response_dict['load_duration'] = result.load_duration
                                if hasattr(result, 'prompt_eval_count'):
                                    response_dict['prompt_eval_count'] = result.prompt_eval_count
                                
                                st.json(response_dict)
                        else:
                            st.write(result)
                            
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        import traceback
                        with st.expander("Error Details"):
                            st.code(traceback.format_exc())
        
        # Similarity comparison

    else:
        st.warning("⚠️ No embedding models found")
        st.markdown("""
        Please install an embedding model first:
        ```bash
        ollama pull nomic-embed-text
        ollama pull mxbai-embed-large
        ollama pull all-minilm
        ```
        """)

with tabs[1]:
    st.header("Similarity Comparison")
    st.markdown("Compare embeddings of two different texts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        text1 = st.text_area(
            "Text 1:",
            value="The cat sat on the mat.",
            height=100,
            key="text1"
        )
    
    with col2:
        text2 = st.text_area(
            "Text 2:",
            value="A feline rested on the rug.",
            height=100,
            key="text2"
        )
    
    if st.button("Compare Embeddings", key="btn_compare"):
        if not text1 or not text2:
            st.warning("Please enter both texts")
        else:
            with st.spinner("Generating embeddings for comparison..."):
                try:
                    # Generate embeddings for both texts
                    result1 = ollama_embeddings(model_name=model_name, text=text1)
                    result2 = ollama_embeddings(model_name=model_name, text=text2)
                    
                    if hasattr(result1, 'embedding') and hasattr(result2, 'embedding'):
                        vec1 = result1.embedding
                        vec2 = result2.embedding
                        
                        # Calculate cosine similarity
                        dot_product = sum(a * b for a, b in zip(vec1, vec2))
                        norm1 = sum(x**2 for x in vec1) ** 0.5
                        norm2 = sum(x**2 for x in vec2) ** 0.5
                        cosine_sim = dot_product / (norm1 * norm2)
                        
                        st.success("✅ Similarity calculated!")
                        
                        st.subheader("📊 Similarity Score")
                        
                        col1, col2, col3 = st.columns([2, 1, 1])
                        
                        with col1:
                            st.metric("Cosine Similarity", f"{cosine_sim:.6f}")
                            
                            # Interpretation
                            if cosine_sim > 0.9:
                                interpretation = "🟢 Very Similar"
                            elif cosine_sim > 0.7:
                                interpretation = "🟡 Similar"
                            elif cosine_sim > 0.5:
                                interpretation = "🟠 Somewhat Similar"
                            else:
                                interpretation = "🔴 Different"
                            
                            st.write(f"**Interpretation:** {interpretation}")
                        
                        with col2:
                            st.metric("Vector 1 Norm", f"{norm1:.4f}")
                        
                        with col3:
                            st.metric("Vector 2 Norm", f"{norm2:.4f}")
                        
                        # Show calculation
                        with st.expander("📐 Calculation Details"):
                            st.code(f"""
Cosine Similarity = dot(vec1, vec2) / (||vec1|| * ||vec2||)
                  = {dot_product:.6f} / ({norm1:.6f} * {norm2:.6f})
                  = {cosine_sim:.6f}

Where:
- dot(vec1, vec2) = sum of element-wise products
- ||vec|| = L2 norm (Euclidean length) of vector
                            """)
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")


# Summary
with tabs[2]:
    st.header("📊 Summary")
st.markdown("""
### Function Tested:
- ✅ `embeddings(model_name, text, **kwargs)` - Generate embeddings for text

### Parameters:
- **model_name**: Name of the embedding model (e.g., 'nomic-embed-text')
- **text**: Input text to embed
- **kwargs**: Additional parameters

### Returns:
A response object containing:
- **embedding**: List of float values representing the text embedding
- **model**: Model name used
- **total_duration**: Processing time

### Embedding Properties:
- **Dimension**: Number of values in the vector (model-dependent)
- **Range**: Typically between -1 and 1
- **Cosine Similarity**: Measure of similarity between vectors (0-1)
  - 1.0 = Identical
  - 0.0 = Orthogonal (unrelated)
  - -1.0 = Opposite

### Use Cases:
- Semantic search
- Text similarity comparison
- Document clustering
- Recommendation systems
- Information retrieval
""")

# =================================================================================================
show_code(__file__)
