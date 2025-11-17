import streamlit as st

from lib.helper_streamlit import get_code_and_output, show_code


st.header("📝 Lists and Operations — Python Basics")
st.markdown("Working with lists: creation, manipulation and common operations.")

# --- CODE START
# Creating a list
numbers = [1, 2, 3, 4, 5]

# Append
numbers.append(6)

# List comprehension
squares = [x**2 for x in numbers]

# Slicing
first_three = numbers[:3]

# Even Numbers
evens = [x for x in numbers if x % 2 == 0]
# --- CODE END

# =================================================================================================
show_code(__file__)

st.subheader("Result:")

# --- CODE START: OUTPUT
st.write("Show first 5 elements of the list:", numbers[:5])
st.write("After append:", numbers)
st.write("Squares:", squares)
st.write("First three:", first_three)
st.write("Even numbers:", evens)
# --- CODE END: OUTPUT
