import streamlit as st
import pandas as pd
import json

st.header("📤 File Upload/Download — Streamlit Basics")
st.markdown("Uploading and downloading files in Streamlit applications.")

# File uploader
st.subheader("File Upload")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "json", "py"])

if uploaded_file is not None:
    st.success(f"✅ Uploaded: {uploaded_file.name}")
    st.write("**File details:**")
    st.write(f"- Name: {uploaded_file.name}")
    st.write(f"- Type: {uploaded_file.type}")
    st.write(f"- Size: {uploaded_file.size} bytes")
    
    # Read and display content
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        st.text_area("File content:", content, height=200)
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write("**CSV Preview:**")
        st.dataframe(df)

# Multiple file upload
st.subheader("Multiple File Upload")

uploaded_files = st.file_uploader(
    "Choose multiple files", 
    accept_multiple_files=True,
    type=["txt", "csv"]
)

if uploaded_files:
    st.write(f"**Uploaded {len(uploaded_files)} file(s):**")
    for file in uploaded_files:
        st.write(f"- {file.name}")

# Download button
st.subheader("File Download")

# Text file download
text_data = """# Sample Data
Line 1: Hello, World!
Line 2: Streamlit is awesome
Line 3: Python file download demo
"""

st.download_button(
    label="📥 Download Text File",
    data=text_data,
    file_name="sample.txt",
    mime="text/plain"
)

# CSV download
csv_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NY", "LA", "Chicago"]
})

st.download_button(
    label="📥 Download CSV",
    data=csv_data.to_csv(index=False),
    file_name="data.csv",
    mime="text/csv"
)

# JSON download

json_data = {
    "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]
}

st.download_button(
    label="📥 Download JSON",
    data=json.dumps(json_data, indent=2),
    file_name="data.json",
    mime="application/json"
)

# Tips
st.subheader("💡 Tips")

st.info("""
- **Supported types**: txt, csv, json, pdf, images, etc.
- **Size limit**: Default is 200MB (configurable)
- **Multiple files**: Set `accept_multiple_files=True`
- **File types**: Use `type` parameter to restrict
""")

