import streamlit as st

st.header("⚠️ Exception Handling — Python Basics")
st.markdown("Try, except, and error handling in Python.")

# Basic try-except
st.subheader("Basic Exception Handling")

try:
    result = 10 / 2
    st.write("✅ Division successful:", result)
except ZeroDivisionError:
    st.error("Cannot divide by zero!")

# Multiple exceptions
st.subheader("Multiple Exception Types")

def safe_conversion(value):
    try:
        number = int(value)
        result = 100 / number
        return result
    except ValueError:
        return "Error: Not a valid number"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

st.write("Convert '5':", safe_conversion("5"))
st.write("Convert 'abc':", safe_conversion("abc"))
st.write("Convert '0':", safe_conversion("0"))

# Try-except-else-finally
st.subheader("Complete Exception Handling")

code_example = """
try:
    # Code that might raise an exception
    file = open('data.txt', 'r')
    data = file.read()
except FileNotFoundError:
    # Handle specific exception
    print("File not found!")
else:
    # Runs if no exception occurred
    print("File read successfully!")
finally:
    # Always runs (cleanup)
    file.close()
"""

st.code(code_example, language="python")

# Custom exceptions
st.subheader("Raising Exceptions")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Valid age: {age}"

try:
    st.write(validate_age(25))
    st.write(validate_age(-5))
except ValueError as e:
    st.error(f"❌ {e}")

# Common exceptions
st.subheader("Common Exception Types")

exceptions = {
    "ValueError": "Invalid value type",
    "TypeError": "Wrong type",
    "KeyError": "Missing dictionary key",
    "IndexError": "List index out of range",
    "FileNotFoundError": "File doesn't exist",
    "ZeroDivisionError": "Division by zero"
}

for exc, desc in exceptions.items():
    st.write(f"**{exc}**: {desc}")
