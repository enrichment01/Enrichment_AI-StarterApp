import streamlit as st
import time

st.header("⚡ Performance Tuning — Ollama Basics")
st.markdown("Optimizing Ollama for speed, memory, and quality.")

# Overview
st.subheader("Why Tune Performance?")

st.write("""
Performance tuning helps you balance three key factors:
- **Speed**: How fast responses are generated
- **Quality**: How good the responses are
- **Resources**: RAM, CPU/GPU usage
""")

# Key parameters
st.subheader("🎛️ Key Performance Parameters")

st.write("**1. num_ctx (Context Window)**")
st.code("""
# Smaller context = faster, less memory
ollama.generate(
    model='phi4-mini',
    prompt='...',
    options={'num_ctx': 2048}  # Default is 4096
)

# Impact:
# - 2048: ~2x faster, uses ~50% less RAM
# - 4096: Standard (default)
# - 8192: Slower, more RAM, longer context
""", language="python")

st.write("**2. num_predict (Max Output Length)**")
st.code("""
# Limit response length
ollama.generate(
    model='phi4-mini',
    prompt='...',
    options={'num_predict': 100}  # Max 100 tokens
)

# Impact:
# - Shorter = faster completion
# - Prevents overly long responses
# - Good for quick answers
""", language="python")

st.write("**3. num_thread (CPU Threads)**")
st.code("""
# Adjust CPU thread usage
ollama.generate(
    model='phi4-mini',
    prompt='...',
    options={'num_thread': 8}  # Use 8 CPU threads
)

# Impact:
# - More threads = faster (up to a point)
# - Too many = diminishing returns
# - Usually: num_cores - 1 or num_cores / 2
""", language="python")

# GPU acceleration
st.subheader("🚀 GPU Acceleration")

gpu_info = """
# Ollama automatically uses GPU if available

# Check GPU usage
# - NVIDIA: nvidia-smi
# - AMD: rocm-smi
# - Apple Silicon: Activity Monitor

# Force CPU-only (for testing)
# Set environment variable:
# CUDA_VISIBLE_DEVICES="" ollama serve

# For better GPU performance:
# - Use larger batch sizes
# - Keep model loaded (don't restart)
# - Ensure latest drivers
"""

st.code(gpu_info, language="bash")

# Memory optimization
st.subheader("💾 Memory Optimization")

st.write("**1. Model Selection**")
memory_models = {
    "phi (2.7B)": "~2 GB RAM",
    "phi4-mini (7B)": "~4 GB RAM",
    "phi4-mini (13B)": "~8 GB RAM",
    "phi4-mini (70B)": "~40 GB RAM"
}

for model, ram in memory_models.items():
    st.write(f"**{model}**: {ram}")

st.write("\n**2. Context Window Management**")
st.code("""
# Reduce context window to save memory
options = {
    'num_ctx': 2048,  # Instead of 4096
}

# Saves ~2 GB RAM for 7B models
""", language="python")

st.write("**3. Unload Models**")
st.code("""
# Models stay in memory for 5 minutes by default
# Adjust keep-alive time

# Quick unload (keep for 1 minute)
ollama.generate(
    model='phi4-mini',
    prompt='...',
    keep_alive='1m'
)

# Immediate unload
ollama.generate(
    model='phi4-mini',
    prompt='...',
    keep_alive='0'
)

# Keep forever (until restart)
ollama.generate(
    model='phi4-mini',
    prompt='...',
    keep_alive='-1'
)
""", language="python")

# Speed optimization
st.subheader("⚡ Speed Optimization Techniques")

st.write("**1. Choose Faster Models**")
speed_comparison = {
    "phi": "⚡⚡⚡⚡⚡ (fastest)",
    "mistral": "⚡⚡⚡⚡",
    "phi4-mini": "⚡⚡⚡",
    "llama3": "⚡⚡⚡",
    "codellama": "⚡⚡⚡"
}

for model, speed in speed_comparison.items():
    st.write(f"**{model}**: {speed}")

st.write("\n**2. Optimize Parameters**")
st.code("""
# Speed-optimized settings
fast_options = {
    'temperature': 0.3,     # Less sampling
    'top_p': 0.7,          # Fewer choices
    'top_k': 20,           # Limit tokens
    'num_predict': 150,    # Limit length
    'num_ctx': 2048,       # Smaller context
}

response = ollama.generate(
    model='mistral',
    prompt='Quick question...',
    options=fast_options
)
""", language="python")

st.write("\n**3. Use Streaming**")
st.code("""
# Streaming shows results immediately
# Improves perceived performance

stream = ollama.generate(
    model='phi4-mini',
    prompt='Tell me a story',
    stream=True
)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
""", language="python")

# Quality optimization
st.subheader("🎯 Quality Optimization")

st.write("**High-Quality Settings:**")
st.code("""
quality_options = {
    'temperature': 0.7,     # Balanced creativity
    'top_p': 0.9,          # More diverse
    'top_k': 40,           # Standard
    'num_ctx': 4096,       # Full context
    'repeat_penalty': 1.1   # Avoid repetition
}

# Use with better model
response = ollama.generate(
    model='llama3',
    prompt='Detailed question...',
    options=quality_options
)
""", language="python")

# Batch processing
st.subheader("📦 Batch Processing")

batch_code = """
import ollama
from concurrent.futures import ThreadPoolExecutor

def process_prompt(prompt):
    '''Process single prompt'''
    return ollama.generate(
        model='phi4-mini',
        prompt=prompt,
        options={'num_ctx': 2048}
    )

# Process multiple prompts efficiently
prompts = [
    "Question 1...",
    "Question 2...",
    "Question 3..."
]

# Sequential (slow)
results_seq = [process_prompt(p) for p in prompts]

# Parallel (faster if you have multiple cores)
with ThreadPoolExecutor(max_workers=3) as executor:
    results_parallel = list(executor.map(process_prompt, prompts))

# Note: Ollama handles queuing internally
# Multiple requests share the same model in memory
"""

st.code(batch_code, language="python")

# Caching strategies
st.subheader("💾 Caching Strategies")

caching_code = """
import streamlit as st
from functools import lru_cache

# Simple cache
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_ai_response(prompt, model='phi4-mini'):
    '''Cached AI responses'''
    response = ollama.generate(
        model=model,
        prompt=prompt
    )
    return response['response']

# Usage
answer = get_ai_response("What is Python?")
# First call: contacts Ollama
# Subsequent calls: instant (from cache)

# LRU cache for non-Streamlit apps
@lru_cache(maxsize=100)
def cached_generate(prompt):
    return ollama.generate(
        model='phi4-mini',
        prompt=prompt
    )['response']
"""

st.code(caching_code, language="python")

# Monitoring performance
st.subheader("📊 Monitoring Performance")

monitoring_code = """
import time
import ollama

def benchmark_model(model, prompt, iterations=5):
    '''Benchmark model performance'''
    
    times = []
    
    for i in range(iterations):
        start = time.time()
        
        response = ollama.generate(
            model=model,
            prompt=prompt
        )
        
        elapsed = time.time() - start
        times.append(elapsed)
        
        tokens = len(response['response'].split())
        print(f"Run {i+1}: {elapsed:.2f}s ({tokens} tokens)")
    
    avg = sum(times) / len(times)
    print(f"\\nAverage: {avg:.2f}s")
    return avg

# Compare models
benchmark_model('phi', 'Explain Python in one sentence')
benchmark_model('phi4-mini', 'Explain Python in one sentence')
"""

st.code(monitoring_code, language="python")

# Configuration examples
st.subheader("⚙️ Configuration Profiles")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**⚡ Speed Profile**")
    st.code("""
{
    'num_ctx': 2048,
    'num_predict': 100,
    'temperature': 0.3,
    'top_p': 0.7,
    'top_k': 20
}

Best for:
- Quick answers
- Real-time chat
- Simple tasks
    """)

with col2:
    st.write("**⚖️ Balanced Profile**")
    st.code("""
{
    'num_ctx': 4096,
    'num_predict': 300,
    'temperature': 0.7,
    'top_p': 0.9,
    'top_k': 40
}

Best for:
- General use
- Good quality
- Reasonable speed
    """)

with col3:
    st.write("**🎯 Quality Profile**")
    st.code("""
{
    'num_ctx': 8192,
    'num_predict': 500,
    'temperature': 0.8,
    'top_p': 0.95,
    'top_k': 50
}

Best for:
- Complex tasks
- Long responses
- Best quality
    """)

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**General Guidelines:**
- Start with defaults, optimize if needed
- Profile your specific use case
- Balance speed vs. quality for your needs
- Monitor resource usage in production

**Speed Optimization:**
- Use smaller models when possible
- Limit context window to what you need
- Set reasonable max_predict values
- Consider streaming for long responses

**Memory Optimization:**
- Choose appropriate model size
- Reduce context window if memory limited
- Unload models when not needed
- Monitor RAM usage

**Quality Optimization:**
- Use better models (llama3 > phi4-mini)
- Increase context for long conversations
- Tune temperature for your task
- Test with real-world examples
""")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **Profile first**: Measure before optimizing
- **User experience**: Streaming improves perceived speed
- **Resource monitoring**: Watch RAM/CPU/GPU usage
- **Model warmup**: First request is slower (model loading)
- **Batching**: Group requests when possible
- **Caching**: Cache identical requests
""")
