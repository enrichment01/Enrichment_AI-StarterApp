import streamlit as st
import time

st.header("🎨 Decorators Basics — Python Basics")
st.markdown("Understanding function decorators and their applications.")

# Basic decorator
st.subheader("Basic Decorator Example")

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"

st.write("Decorated function result:", greet())

# Decorator with arguments
st.subheader("Decorator with Arguments")

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    return f"Hello, {name}!"

st.write("Repeated 3 times:", say_hello("Alice"))

# Timing decorator
st.subheader("Practical Example: Timing Decorator")

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        st.info(f"⏱️ Function '{func.__name__}' took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(0.1)
    return "Task completed"

if st.button("Run Timed Function"):
    result = slow_function()
    st.write("Result:", result)

# Multiple decorators
st.subheader("Multiple Decorators")

code_example = """
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def text():
    return "Decorated Text"

# Result: <b><i>Decorated Text</i></b>
"""

st.code(code_example, language="python")

# Common use cases
st.subheader("Common Decorator Use Cases")

use_cases = {
    "Logging": "Track function calls and arguments",
    "Timing": "Measure execution time",
    "Caching": "Store results for repeated calls",
    "Authentication": "Check permissions before execution",
    "Validation": "Validate input arguments",
    "Retry logic": "Retry failed operations"
}

for use_case, description in use_cases.items():
    st.write(f"**{use_case}**: {description}")

# Decorator template
st.subheader("Decorator Template")

template = """
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Code before function call
        result = func(*args, **kwargs)
        # Code after function call
        return result
    return wrapper

@my_decorator
def my_function():
    return "Hello"
"""

st.code(template, language="python")
