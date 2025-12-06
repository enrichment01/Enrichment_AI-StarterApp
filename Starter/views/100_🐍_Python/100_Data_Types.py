import streamlit as st

from lib.helper_streamlit import show_code

st.header("📦 Data Types — Python Basics")

# --- CODE START
integer_num = 42
float_num = 3.14
text = "Hello, Python!"
is_active = True
fruits = ["apple", "banana", "cherry"]
person = {"name": "John", "age": 30, "city": "New York"}
coordinates = (10, 20)
# --- CODE END

# =================================================================================================
show_code(__file__)

st.subheader("Result:")

# --- CODE START: OUTPUT
st.write("Integer:", integer_num)
st.write("Float:", float_num)
st.write("String:", text)
st.write("Boolean:", is_active)
st.write("List:", fruits)
st.write("Dictionary:", person)
st.write("Tuple:", coordinates)
# --- CODE END: OUTPUT
