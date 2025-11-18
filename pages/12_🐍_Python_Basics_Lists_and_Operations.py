import streamlit as st

from lib import helper_streamlit
from lib.helper_python import utils


st.header("📝 Lists and Operations — Python Basics")
st.markdown("Working with lists: creation, manipulation and common operations.")

# Creating a list
numbers = [1, 2, 3, 4, 5]

st.write("Show first 5 elements of the list:", numbers[:5])

# Append
numbers.append(6)

st.write("After append:", numbers)

# List comprehension
squares = [x**2 for x in numbers]

st.write("Squares:", squares)

# Slicing
first_three = numbers[:3]

st.write("First three:", first_three)

# Filter
evens = [x for x in numbers if x % 2 == 0]

st.write("Even numbers:", evens)
