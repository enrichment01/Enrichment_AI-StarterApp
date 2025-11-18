import streamlit as st

st.header("🔧 Functions — Python Basics")
st.markdown("Defining and using functions with examples.")

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def calculate_area(length, width):
    return length * width

def get_stats(numbers):
    return {
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

st.write(greet("Alice"))
st.write(greet("Bob", "Hi"))
st.write("Area of 5x3:", calculate_area(5, 3))
st.write("Stats of [1,2,3,4,5]:", get_stats([1,2,3,4,5]))
