import streamlit as st

from lib import helper_streamlit
from lib.helper_python import utils


st.header("🔄 Loops — Python Basics")
st.markdown("For and while loops with examples and outputs.")

# For loop
result_for = []
for i in range(5):
    result_for.append(i * 2)

# While loop
result_while = []
count = 5
while count > 0:
    result_while.append(count)
    count -= 1

# Enumerate
fruits = ["apple", "banana", "cherry"]
result_enumerate = []
for idx, fruit in enumerate(fruits):
    result_enumerate.append(f"{idx}: {fruit}")


loop_results = utils.demonstrate_loops()
st.write("For loop result:", result_for)
st.write("Countdown:", result_while)
st.write("Indexed fruits:", result_enumerate)
