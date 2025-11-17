import streamlit as st

from lib.helper_streamlit import show_code

st.header("🔄 Loops — Python Basics")
#markdown("For and while loops with examples and outputs.")
st.markdown("For and while loops with examples and outputs.")

# --- CODE START
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


# --- CODE END


# =================================================================================================
show_code(__file__)

st.subheader("Result:")

# --- CODE START: OUTPUT
st.write("For loop result:", result_for)
st.write("Countdown:", result_while)
st.write("Indexed fruits:", result_enumerate)
# --- CODE END: OUTPUT

