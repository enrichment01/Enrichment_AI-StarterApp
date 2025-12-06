import streamlit as st

st.header("🔢 Embeddings API — Ollama Basics")
st.markdown("Converting text to vector embeddings for semantic search and similarity.")

# Overview
st.subheader("What are Embeddings?")

st.write("""
Embeddings are numerical representations of text that capture semantic meaning. 
Similar texts have similar embeddings, making them useful for search, 
clustering, and recommendations.
""")

# Visual representation
st.subheader("📊 Text → Vector")

example_text = "The cat sat on the mat"
st.write(f"**Text:** `{example_text}`")
st.write("**Embedding:** `[0.21, -0.34, 0.56, 0.12, -0.89, ...]` (768-4096 dimensions)")

# Basic usage
st.subheader("🚀 Basic Usage")

basic_code = """
import ollama

# Generate embedding for a single text
response = ollama.embeddings(
    model='phi4-mini',
    prompt='The quick brown fox'
)

# Access the embedding
embedding = response['embedding']

print(f"Embedding dimension: {len(embedding)}")
print(f"First 5 values: {embedding[:5]}")

# Output:
# Embedding dimension: 4096
# First 5 values: [0.234, -0.567, 0.123, 0.890, -0.234]
"""

st.code(basic_code, language="python")

# Use cases
st.subheader("💼 Common Use Cases")

use_cases = {
    "Semantic Search": "Find documents similar to a query",
    "Text Clustering": "Group similar texts together",
    "Recommendation": "Find similar items/content",
    "Duplicate Detection": "Identify similar or duplicate texts",
    "Question Answering": "Match questions to relevant answers",
    "Classification": "Categorize text based on similarity"
}

for use_case, description in use_cases.items():
    st.write(f"**{use_case}**: {description}")

# Similarity calculation
st.subheader("📐 Calculating Similarity")

similarity_code = """
import numpy as np

def cosine_similarity(vec1, vec2):
    '''Calculate cosine similarity between two vectors'''
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot_product / (norm1 * norm2)

# Generate embeddings for two texts
response1 = ollama.embeddings(
    model='phi4-mini',
    prompt='I love programming'
)

response2 = ollama.embeddings(
    model='phi4-mini',
    prompt='I enjoy coding'
)

embedding1 = response1['embedding']
embedding2 = response2['embedding']

# Calculate similarity
similarity = cosine_similarity(embedding1, embedding2)

print(f"Similarity: {similarity:.4f}")
# Output: 0.8934 (very similar!)

# Compare with different text
response3 = ollama.embeddings(
    model='phi4-mini',
    prompt='The weather is nice'
)

similarity2 = cosine_similarity(embedding1, response3['embedding'])
print(f"Similarity: {similarity2:.4f}")
# Output: 0.2145 (not similar)
"""

st.code(similarity_code, language="python")

# Semantic search example
st.subheader("🔍 Semantic Search Example")

search_code = """
import ollama
import numpy as np

# Document database
documents = [
    "Python is a programming language",
    "Machine learning uses neural networks",
    "Cats are domesticated animals",
    "JavaScript runs in web browsers",
    "Deep learning is a subset of ML"
]

# Generate embeddings for all documents
doc_embeddings = []
for doc in documents:
    response = ollama.embeddings(model='phi4-mini', prompt=doc)
    doc_embeddings.append(response['embedding'])

# Search query
query = "Tell me about coding languages"
query_response = ollama.embeddings(model='phi4-mini', prompt=query)
query_embedding = query_response['embedding']

# Calculate similarities
similarities = []
for i, doc_emb in enumerate(doc_embeddings):
    sim = cosine_similarity(query_embedding, doc_emb)
    similarities.append((i, sim, documents[i]))

# Sort by similarity
similarities.sort(key=lambda x: x[1], reverse=True)

# Show top results
print("Top 3 results:")
for idx, sim, doc in similarities[:3]:
    print(f"{sim:.4f} - {doc}")

# Output:
# 0.8234 - Python is a programming language
# 0.7891 - JavaScript runs in web browsers
# 0.3456 - Machine learning uses neural networks
"""

st.code(search_code, language="python")

# Interactive demo
st.subheader("🎮 Similarity Demo")

text1 = st.text_input("Text 1:", "I love Python programming")
text2 = st.text_input("Text 2:", "I enjoy coding in Python")

if st.button("Calculate Similarity"):
    st.info("In a real app, this would use Ollama embeddings")
    
    # Simulated similarity (random for demo)
    import random
    similarity = random.uniform(0.6, 0.95)
    
    st.metric("Similarity Score", f"{similarity:.4f}")
    
    if similarity > 0.8:
        st.success("✅ Very similar texts!")
    elif similarity > 0.5:
        st.warning("⚠️ Somewhat similar")
    else:
        st.error("❌ Not very similar")

# Vector database integration
st.subheader("🗄️ Vector Database Integration")

vector_db_code = """
# Using a simple in-memory vector store
class VectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = []
    
    def add(self, text):
        '''Add document to store'''
        response = ollama.embeddings(model='phi4-mini', prompt=text)
        self.documents.append(text)
        self.embeddings.append(response['embedding'])
    
    def search(self, query, top_k=5):
        '''Search for similar documents'''
        # Get query embedding
        response = ollama.embeddings(model='phi4-mini', prompt=query)
        query_emb = response['embedding']
        
        # Calculate similarities
        results = []
        for i, doc_emb in enumerate(self.embeddings):
            sim = cosine_similarity(query_emb, doc_emb)
            results.append((sim, self.documents[i]))
        
        # Sort and return top k
        results.sort(reverse=True)
        return results[:top_k]

# Usage
store = VectorStore()
store.add("Python is great for data science")
store.add("JavaScript is used for web development")
store.add("Machine learning models need training data")

results = store.search("data analysis tools")
for score, doc in results:
    print(f"{score:.4f}: {doc}")
"""

st.code(vector_db_code, language="python")

# Caching embeddings
st.subheader("⚡ Caching Embeddings")

caching_code = """
import pickle
import os

def get_embedding_cached(text, cache_file='embeddings.pkl'):
    '''Get embedding with caching'''
    
    # Load cache
    cache = {}
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as f:
            cache = pickle.load(f)
    
    # Check cache
    if text in cache:
        return cache[text]
    
    # Generate embedding
    response = ollama.embeddings(model='phi4-mini', prompt=text)
    embedding = response['embedding']
    
    # Save to cache
    cache[text] = embedding
    with open(cache_file, 'wb') as f:
        pickle.dump(cache, f)
    
    return embedding

# Usage
embedding = get_embedding_cached("My text")
# First call: generates embedding
# Second call: instant (from cache)
"""

st.code(caching_code, language="python")

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Performance:**
- Cache embeddings for repeated texts
- Batch process multiple documents
- Use appropriate model for your data
- Consider embedding dimension vs. accuracy trade-off

**Accuracy:**
- Use same model for query and documents
- Normalize text before embedding
- Handle empty/short texts appropriately
- Consider text length limitations

**Storage:**
- Store embeddings in vector databases
- Use efficient formats (numpy, pickle)
- Index for fast similarity search
- Compress if storage is limited
""")

# Models for embeddings
st.subheader("📚 Models for Embeddings")

models = {
    "phi4-mini": "General purpose, 4096 dims",
    "mistral": "Fast, 4096 dims",
    "nomic-embed-text": "Optimized for embeddings, 768 dims",
    "mxbai-embed-large": "High quality, 1024 dims"
}

for model, desc in models.items():
    st.write(f"**{model}**: {desc}")

st.info("Some models are specifically designed for embeddings and may perform better than general LLMs.")

# Advanced example
st.subheader("📋 Complete Example: Document Clustering")

clustering_code = """
import ollama
import numpy as np
from sklearn.cluster import KMeans

# Documents to cluster
docs = [
    "Python programming tutorial",
    "Java coding basics",
    "Machine learning introduction",
    "Deep learning with PyTorch",
    "C++ programming guide",
    "Neural networks explained"
]

# Generate embeddings
embeddings = []
for doc in docs:
    response = ollama.embeddings(model='phi4-mini', prompt=doc)
    embeddings.append(response['embedding'])

# Convert to numpy array
X = np.array(embeddings)

# Cluster into 2 groups
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X)

# Show results
for i, (doc, cluster) in enumerate(zip(docs, clusters)):
    print(f"Cluster {cluster}: {doc}")

# Output:
# Cluster 0: Python programming tutorial
# Cluster 0: Java coding basics
# Cluster 0: C++ programming guide
# Cluster 1: Machine learning introduction
# Cluster 1: Deep learning with PyTorch
# Cluster 1: Neural networks explained
"""

st.code(clustering_code, language="python")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **Embeddings are cached by Ollama** for identical inputs
- **Similarity range**: Cosine similarity is -1 to 1 (typically 0 to 1)
- **Threshold**: > 0.8 usually means very similar
- **Batch processing**: Process multiple texts at once when possible
- **Model choice**: Use embedding-specific models for best results
""")
