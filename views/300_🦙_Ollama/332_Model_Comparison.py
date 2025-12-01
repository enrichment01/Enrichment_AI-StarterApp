import streamlit as st

st.header("⚖️ Model Comparison — Ollama Basics")
st.markdown("Comparing different Ollama models for various tasks.")

# Overview
st.subheader("Why Compare Models?")

st.write("""
Different models have different strengths, speeds, and resource requirements. 
Choosing the right model for your task can significantly impact performance 
and user experience.
""")

# Model characteristics
st.subheader("📊 Popular Ollama Models")

models_table = {
    "Model": ["phi4-mini", "llama3", "mistral", "codellama", "phi", "gemma"],
    "Size": ["7B", "8B", "7B", "7B", "2.7B", "7B"],
    "Speed": ["Medium", "Medium", "Fast", "Medium", "Very Fast", "Fast"],
    "Quality": ["Good", "Very Good", "Good", "Good", "Fair", "Good"],
    "Best For": ["General", "General", "Chat", "Code", "Quick tasks", "General"]
}

import pandas as pd
df = pd.DataFrame(models_table)
st.dataframe(df, use_container_width=True, hide_index=True)

# Detailed comparison
st.subheader("🔍 Detailed Comparison")

with st.expander("🦙 Llama 2 (7B)"):
    st.write("**Strengths:**")
    st.write("- Well-rounded for general tasks")
    st.write("- Good instruction following")
    st.write("- Stable and reliable")
    st.write("\n**Weaknesses:**")
    st.write("- Slower than newer models")
    st.write("- Medium quality responses")
    st.write("\n**Use Cases:** General chatbot, Q&A, content generation")

with st.expander("🦙 Llama 3 (8B)"):
    st.write("**Strengths:**")
    st.write("- Best overall quality")
    st.write("- Excellent reasoning")
    st.write("- Latest architecture")
    st.write("\n**Weaknesses:**")
    st.write("- Slightly larger size")
    st.write("- May be overkill for simple tasks")
    st.write("\n**Use Cases:** Complex reasoning, high-quality content, analysis")

with st.expander("⚡ Mistral (7B)"):
    st.write("**Strengths:**")
    st.write("- Fast inference")
    st.write("- Good chat capabilities")
    st.write("- Efficient resource usage")
    st.write("\n**Weaknesses:**")
    st.write("- Less detailed than Llama 3")
    st.write("- Better at chat than analysis")
    st.write("\n**Use Cases:** Interactive chat, quick responses, customer service")

with st.expander("💻 CodeLlama (7B)"):
    st.write("**Strengths:**")
    st.write("- Excellent for code")
    st.write("- Understands many languages")
    st.write("- Good at debugging")
    st.write("\n**Weaknesses:**")
    st.write("- Focused on code (less general)")
    st.write("- May struggle with non-code tasks")
    st.write("\n**Use Cases:** Code generation, debugging, technical documentation")

with st.expander("🚀 Phi (2.7B)"):
    st.write("**Strengths:**")
    st.write("- Very fast")
    st.write("- Small resource footprint")
    st.write("- Good for simple tasks")
    st.write("\n**Weaknesses:**")
    st.write("- Lower quality for complex tasks")
    st.write("- Limited knowledge")
    st.write("\n**Use Cases:** Quick answers, simple tasks, resource-constrained environments")

with st.expander("💎 Gemma (7B)"):
    st.write("**Strengths:**")
    st.write("- Good balance of speed/quality")
    st.write("- Open source from Google")
    st.write("- Efficient architecture")
    st.write("\n**Weaknesses:**")
    st.write("- Newer, less tested")
    st.write("- Community still growing")
    st.write("\n**Use Cases:** General purpose, experimentation, balanced workloads")

# Performance comparison
st.subheader("⚡ Performance Metrics")

st.write("**Approximate Response Times (for ~100 token response):**")

perf_data = {
    "Model": ["phi", "mistral", "gemma", "phi4-mini", "llama3", "codellama"],
    "Speed (tokens/sec)": [40, 30, 25, 20, 18, 20],
    "RAM Usage (GB)": [2, 4, 4, 4, 5, 4]
}

perf_df = pd.DataFrame(perf_data)
st.bar_chart(perf_df.set_index("Model")["Speed (tokens/sec)"])

st.write("**RAM Usage:**")
st.bar_chart(perf_df.set_index("Model")["RAM Usage (GB)"])

# Quality comparison
st.subheader("🎯 Quality Comparison")

st.write("**Response Quality by Task Type:**")

quality_matrix = {
    "Task": ["General Chat", "Code Generation", "Analysis", "Creative Writing", "Simple Q&A"],
    "phi4-mini": ["⭐⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐"],
    "llama3": ["⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐"],
    "mistral": ["⭐⭐⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐"],
    "codellama": ["⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐"],
    "phi": ["⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐⭐"]
}

quality_df = pd.DataFrame(quality_matrix)
st.dataframe(quality_df, use_container_width=True, hide_index=True)

# Selection guide
st.subheader("🎯 Model Selection Guide")

selection_guide = """
Choose your model based on:

**1. Task Type:**
   - General conversation → llama3, mistral
   - Code tasks → codellama
   - Quick answers → phi, mistral
   - Analysis → llama3
   - Creative writing → llama3, phi4-mini

**2. Resources:**
   - Limited RAM (< 4GB) → phi
   - Standard (4-8GB) → mistral, phi4-mini
   - High-end (8GB+) → llama3

**3. Speed Requirements:**
   - Real-time chat → phi, mistral
   - Can wait a bit → llama3
   - Code generation → codellama

**4. Quality Needs:**
   - Highest quality → llama3
   - Good balance → mistral, gemma
   - Fast > quality → phi
"""

st.code(selection_guide)

# Testing code
st.subheader("🧪 Testing Multiple Models")

test_code = """
import ollama
import time

def test_models(prompt, models=['phi4-mini', 'mistral', 'phi']):
    '''Test prompt across multiple models'''
    
    results = []
    
    for model in models:
        print(f"\\nTesting {model}...")
        
        start = time.time()
        try:
            response = ollama.generate(
                model=model,
                prompt=prompt
            )
            elapsed = time.time() - start
            
            results.append({
                'model': model,
                'response': response['response'][:200] + '...',
                'time': f"{elapsed:.2f}s",
                'tokens': len(response['response'].split())
            })
            
        except Exception as e:
            results.append({
                'model': model,
                'response': f"Error: {e}",
                'time': 'N/A',
                'tokens': 0
            })
    
    return results

# Run comparison
prompt = "Explain what Python is in 2 sentences."
results = test_models(prompt)

for r in results:
    print(f"\\n{r['model']} ({r['time']}):")
    print(r['response'])
"""

st.code(test_code, language="python")

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Model Selection:**
- Start with mistral for general use
- Use codellama specifically for code
- Try llama3 when quality matters most
- Use phi for prototyping/testing

**Testing:**
- Test your specific prompts with multiple models
- Measure actual speed on your hardware
- Compare quality subjectively for your use case
- Consider total cost (time × resources)

**Production:**
- Choose 2-3 models for different scenarios
- Have a fallback model
- Monitor performance in production
- Be ready to switch based on results
""")

# Interactive comparison
st.subheader("🎮 Try Different Models")

task = st.selectbox(
    "Select a task type:",
    ["General Chat", "Code Generation", "Data Analysis", "Creative Writing", "Quick Q&A"]
)

recommendations = {
    "General Chat": ["mistral", "llama3", "phi4-mini"],
    "Code Generation": ["codellama", "llama3"],
    "Data Analysis": ["llama3", "phi4-mini"],
    "Creative Writing": ["llama3", "phi4-mini"],
    "Quick Q&A": ["phi", "mistral"]
}

st.write(f"**Recommended models for {task}:**")
for i, model in enumerate(recommendations[task], 1):
    st.write(f"{i}. **{model}**")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **No single best**: Each model excels at different things
- **Test locally**: Performance varies by hardware
- **Update regularly**: New models released frequently
- **Mix and match**: Use different models for different features
- **User feedback**: Let quality guide your choice, not just specs
""")
