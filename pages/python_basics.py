import streamlit as st
import pandas as pd
import numpy as np
from scripts import python_utils

def show():
    st.header("🐍 Python Basics")
    st.markdown("Learn fundamental Python concepts through interactive examples.")
    
    # Data Types Section
    with st.expander("📦 Data Types", expanded=True):
        st.subheader("Basic Data Types")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
# Numbers
integer_num = 42
float_num = 3.14

# Strings
text = "Hello, Python!"

# Boolean
is_active = True

# List
fruits = ["apple", "banana", "cherry"]

# Dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Tuple
coordinates = (10, 20)
            """, language="python")
        
        with col2:
            st.markdown("**Output:**")
            data_types = python_utils.demonstrate_data_types()
            
            st.write("Integer:", data_types["integer_num"], type(data_types["integer_num"]))
            st.write("Float:", data_types["float_num"], type(data_types["float_num"]))
            st.write("String:", data_types["text"], type(data_types["text"]))
            st.write("Boolean:", data_types["is_active"], type(data_types["is_active"]))
            st.write("List:", data_types["fruits"])
            st.write("Dictionary:", data_types["person"])
            st.write("Tuple:", data_types["coordinates"])
    
    # Lists and Operations
    with st.expander("📝 Lists and Operations"):
        st.subheader("Working with Lists")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
# Creating a list
numbers = [1, 2, 3, 4, 5]

# Append
numbers.append(6)

# List comprehension
squares = [x**2 for x in numbers]

# Slicing
first_three = numbers[:3]

# Filter
evens = [x for x in numbers if x % 2 == 0]
            """, language="python")
        
        with col2:
            st.markdown("**Output:**")
            list_ops = python_utils.demonstrate_list_operations()
            
            st.write("Original list:", list_ops["numbers"][:5])  # Show first 5 before append
            st.write("After append:", list_ops["numbers"])
            st.write("Squares:", list_ops["squares"])
            st.write("First three:", list_ops["first_three"])
            st.write("Even numbers:", list_ops["evens"])
    
    # Functions
    with st.expander("🔧 Functions"):
        st.subheader("Defining and Using Functions")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
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
            """, language="python")
        
        with col2:
            st.markdown("**Output:**")
            
            st.write(python_utils.greet("Alice"))
            st.write(python_utils.greet("Bob", "Hi"))
            st.write("Area of 5x3:", python_utils.calculate_area(5, 3))
            st.write("Stats of [1,2,3,4,5]:", python_utils.get_stats([1,2,3,4,5]))
    
    # Loops
    with st.expander("🔄 Loops"):
        st.subheader("For and While Loops")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
# For loop
result = []
for i in range(5):
    result.append(i * 2)

# While loop
countdown = []
count = 5
while count > 0:
    countdown.append(count)
    count -= 1

# Enumerate
fruits = ["apple", "banana", "cherry"]
indexed_fruits = []
for idx, fruit in enumerate(fruits):
    indexed_fruits.append(f"{idx}: {fruit}")
            """, language="python")
        
        with col2:
            st.markdown("**Output:**")
            
            loop_results = python_utils.demonstrate_loops()
            st.write("For loop result:", loop_results["for_result"])
            st.write("Countdown:", loop_results["countdown"])
            st.write("Indexed fruits:", loop_results["indexed_fruits"])
    
    # Classes
    with st.expander("🏗️ Classes and Objects"):
        st.subheader("Object-Oriented Programming")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            st.code("""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! Now {self.age}"

# Create instance
person = Person("Alice", 25)
            """, language="python")
        
        with col2:
            st.markdown("**Output:**")
            
            person = python_utils.Person("Alice", 25)
            st.write(person.introduce())
            st.write(person.have_birthday())
            st.write(person.introduce())
    
    # Interactive Example
    st.markdown("---")
    st.subheader("🎮 Interactive Example: Temperature Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        temp_celsius = st.number_input("Enter temperature in Celsius:", value=25.0)
        
        if st.button("Convert to Fahrenheit"):
            temp_fahrenheit = python_utils.celsius_to_fahrenheit(temp_celsius)
            st.success(f"{temp_celsius}°C = {temp_fahrenheit}°F")
    
    with col2:
        st.code("""
# Temperature Converter
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
        """, language="python")
