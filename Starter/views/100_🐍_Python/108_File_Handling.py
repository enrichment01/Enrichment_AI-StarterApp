import streamlit as st
import tempfile
import os



st.header("📁 File Handling — Python Basics")
st.markdown("Reading and writing files in Python.")

# Writing to a file
st.subheader("Writing Files")

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    temp_file = f.name
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python File I/O\n")
    f.write("Line 3: Streamlit Demo\n")

st.write("✅ Created temporary file:", temp_file)

# Reading from a file
st.subheader("Reading Files")

# Read entire file
with open(temp_file, 'r') as f:
    content = f.read()

st.write("**Full content:**")
st.code(content)

# Read line by line
with open(temp_file, 'r') as f:
    lines = f.readlines()

st.write("**Lines as list:**", lines)

# Using with statement
st.subheader("Best Practice: Context Manager")

code_example = """
# Automatically closes file
with open('file.txt', 'r') as f:
    data = f.read()
    # Process data
# File is closed here
"""

st.code(code_example, language="python")

# File modes
st.subheader("File Modes")

modes = {
    "'r'": "Read (default)",
    "'w'": "Write (overwrites)",
    "'a'": "Append",
    "'r+'": "Read and write",
    "'b'": "Binary mode (e.g., 'rb', 'wb')"
}

for mode, desc in modes.items():
    st.write(f"**{mode}**: {desc}")

# Cleanup
os.unlink(temp_file)
st.info("💡 Temporary file cleaned up")
