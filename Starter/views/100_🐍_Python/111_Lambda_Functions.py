import streamlit as st
from functools import reduce

st.header("λ Lambda Functions — Python Basics")
st.markdown("Anonymous functions and functional programming concepts.")

# Basic lambda
st.subheader("Basic Lambda Functions")

# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

st.write("Regular function: add(3, 5) =", add(3, 5))
st.write("Lambda function: add_lambda(3, 5) =", add_lambda(3, 5))

# Lambda with single argument
square = lambda x: x ** 2
st.write("Square of 7:", square(7))

# Lambda in sorted()
st.subheader("Lambda with Built-in Functions")

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
st.write("Sorted by grade (descending):", sorted_students)

# Lambda in map()
st.subheader("Lambda with map()")

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
st.write("Original:", numbers)
st.write("Doubled:", doubled)

# Lambda in filter()
st.subheader("Lambda with filter()")

evens = list(filter(lambda x: x % 2 == 0, numbers))
st.write("Even numbers:", evens)

# Lambda in reduce()
st.subheader("Lambda with reduce()")

product = reduce(lambda x, y: x * y, numbers)
st.write("Product of", numbers, "=", product)

# Multiple lambdas
st.subheader("Lambda Functions in Dictionary")

operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Error"
}

a, b = 10, 3
for op_name, op_func in operations.items():
    result = op_func(a, b)
    st.write(f"{op_name}({a}, {b}) = {result}")

# When to use lambda
st.subheader("💡 Best Practices")

st.info("""
**Use lambda when:**
- Function is simple (one line)
- Used only once (inline)
- Passed as argument to higher-order functions

**Use def when:**
- Function is complex
- Function is reused
- Function needs documentation
""")
