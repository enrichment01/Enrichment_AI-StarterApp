import streamlit as st
import math
import random
import datetime
import json
from collections import Counter



st.header("📦 Modules and Imports — Python Basics")
st.markdown("Understanding Python modules, packages, and import statements.")

# Standard library imports
st.subheader("Standard Library Modules")

st.write("π (pi):", math.pi)
st.write("Square root of 16:", math.sqrt(16))
st.write("Random number (1-10):", random.randint(1, 10))
st.write("Current datetime:", datetime.datetime.now())

# Different import styles
st.subheader("Import Styles")

code_examples = """
# Import entire module
import math
print(math.sqrt(16))

# Import specific function
from math import sqrt
print(sqrt(16))

# Import with alias
import numpy as np
array = np.array([1, 2, 3])

# Import multiple items
from datetime import datetime, timedelta

# Import all (not recommended)
from math import *
"""

st.code(code_examples, language="python")

# Commonly used standard library modules
st.subheader("Common Standard Library Modules")

modules = {
    "math": "Mathematical functions",
    "random": "Random number generation",
    "datetime": "Date and time operations",
    "os": "Operating system interface",
    "sys": "System-specific parameters",
    "json": "JSON encoding and decoding",
    "re": "Regular expressions",
    "pathlib": "Object-oriented filesystem paths",
    "collections": "Specialized container datatypes",
    "itertools": "Iterator functions"
}

for module, description in modules.items():
    st.write(f"**{module}**: {description}")

# Example: Using multiple modules
st.subheader("Practical Example")

# Sample data
data = {
    "name": "Python Tutorial",
    "topics": ["variables", "functions", "classes", "modules"],
    "difficulty": "beginner"
}

# JSON operations
json_string = json.dumps(data, indent=2)
st.write("**JSON representation:**")
st.code(json_string, language="json")

# Counter example
words = ["python", "java", "python", "c++", "python", "java"]
word_count = Counter(words)
st.write("**Word frequency:**", dict(word_count))

# Module attributes
st.subheader("Module Information")

st.write("Math module location:", math.__file__)
st.write("Math module name:", math.__name__)
st.write("Available in math:", dir(math)[:10], "...")
