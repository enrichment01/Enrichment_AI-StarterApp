import streamlit as st
import pandas as pd
import numpy as np
import time

st.header("⚡ Caching Data — Streamlit Basics")
st.markdown("Optimize performance with Streamlit's caching mechanisms.")

# st.cache_data example
st.subheader("@st.cache_data Decorator")

@st.cache_data
def load_data(rows=100):
    """Simulate loading data - expensive operation"""
    time.sleep(2)  # Simulate slow data loading
    return pd.DataFrame(
        np.random.randn(rows, 5),
        columns=['A', 'B', 'C', 'D', 'E']
    )

st.write("**Loading data (cached):**")
start_time = time.time()

if st.button("Load Data"):
    data = load_data()
    elapsed = time.time() - start_time
    
    st.success(f"✅ Data loaded in {elapsed:.2f} seconds")
    st.write("On first run, this takes 2 seconds. On subsequent runs, it's instant!")
    st.dataframe(data.head())

# st.cache_resource example
st.subheader("@st.cache_resource Decorator")

@st.cache_resource
def get_database_connection():
    """Simulate database connection - should persist"""
    time.sleep(1)
    return {"status": "connected", "timestamp": time.time()}

if st.button("Get DB Connection"):
    conn = get_database_connection()
    st.write("Connection:", conn)
    st.info("Database connections should use @st.cache_resource")

# Cache with TTL (time to live)
st.subheader("Cache with TTL")

@st.cache_data(ttl=10)  # Cache expires after 10 seconds
def get_current_time():
    return time.strftime("%H:%M:%S")

st.write("**Cached time (10s TTL):**", get_current_time())
st.info("This timestamp updates every 10 seconds")

# Cache with parameters
st.subheader("Cache with Parameters")

@st.cache_data
def compute_expensive_operation(n, operation="sum"):
    """Cached based on parameters"""
    time.sleep(1)
    data = list(range(n))
    
    if operation == "sum":
        return sum(data)
    elif operation == "product":
        result = 1
        for x in data:
            if x > 0:
                result *= x
        return result
    return 0

col1, col2 = st.columns(2)

with col1:
    n = st.number_input("Number", 1, 100, 10)

with col2:
    operation = st.selectbox("Operation", ["sum", "product"])

if st.button("Compute"):
    result = compute_expensive_operation(n, operation)
    st.metric("Result", result)
    st.info("Same parameters = cached result (instant)")

# Clear cache
st.subheader("Cache Management")

col1, col2 = st.columns(2)

with col1:
    if st.button("Clear All Cache"):
        st.cache_data.clear()
        st.success("✅ All cache cleared!")

with col2:
    if st.button("Clear Specific Cache"):
        load_data.clear()
        st.success("✅ load_data cache cleared!")

# Cache statistics
st.subheader("Cache Example with Stats")

@st.cache_data
def generate_random_data(size):
    """Generate random data"""
    return np.random.randn(size)

size = st.slider("Data size", 100, 10000, 1000)

if st.button("Generate"):
    with st.spinner("Generating..."):
        data = generate_random_data(size)
        st.success(f"Generated {len(data)} data points")
        st.line_chart(data[:100])  # Show first 100 points

# Cache key comparison
st.subheader("Understanding Cache Keys")

cache_info = """
Cache keys are based on:
1. Function name
2. Function code
3. Parameter values
4. Parameter types

Example:
- compute(5, "sum") → cached separately
- compute(5, "product") → different cache entry
- compute(10, "sum") → different cache entry
"""

st.code(cache_info)

# Best practices
st.subheader("💡 Caching Best Practices")

practices = {
    "Use @st.cache_data for": [
        "Loading CSV, JSON data",
        "Database queries",
        "API calls",
        "Expensive computations",
        "DataFrame transformations"
    ],
    "Use @st.cache_resource for": [
        "Database connections",
        "ML models",
        "Thread pools",
        "Global resources"
    ],
    "Don't cache": [
        "Random number generation",
        "Current time/date",
        "User-specific data (unless keyed by user)",
        "Frequently changing data"
    ]
}

for category, items in practices.items():
    with st.expander(category):
        for item in items:
            st.write(f"- {item}")

# Performance comparison
st.subheader("Performance Comparison")

st.info("""
**Without caching:**
- Every rerun = full computation
- Slow user experience
- Wastes resources

**With caching:**
- First run = normal speed
- Subsequent runs = instant
- Better user experience
- Efficient resource usage
""")

# Common patterns
st.subheader("📋 Common Patterns")

patterns = """
# Pattern 1: Load CSV file
@st.cache_data
def load_csv(file_path):
    return pd.read_csv(file_path)

# Pattern 2: API call
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_api_data(url):
    response = requests.get(url)
    return response.json()

# Pattern 3: ML model
@st.cache_resource
def load_model():
    return joblib.load('model.pkl')

# Pattern 4: Database query
@st.cache_data
def run_query(query):
    return pd.read_sql(query, connection)
"""

st.code(patterns, language="python")
