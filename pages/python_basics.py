import streamlit as st
import pandas as pd
import numpy as np

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
            integer_num = 42
            float_num = 3.14
            text = "Hello, Python!"
            is_active = True
            fruits = ["apple", "banana", "cherry"]
            person = {"name": "John", "age": 30, "city": "New York"}
            coordinates = (10, 20)
            
            st.write("Integer:", integer_num, type(integer_num))
            st.write("Float:", float_num, type(float_num))
            st.write("String:", text, type(text))
            st.write("Boolean:", is_active, type(is_active))
            st.write("List:", fruits)
            st.write("Dictionary:", person)
            st.write("Tuple:", coordinates)
    
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
            numbers = [1, 2, 3, 4, 5]
            st.write("Original list:", numbers)
            numbers.append(6)
            st.write("After append:", numbers)
            squares = [x**2 for x in numbers]
            st.write("Squares:", squares)
            first_three = numbers[:3]
            st.write("First three:", first_three)
            evens = [x for x in numbers if x % 2 == 0]
            st.write("Even numbers:", evens)
    
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
            
            result = []
            for i in range(5):
                result.append(i * 2)
            st.write("For loop result:", result)
            
            countdown = []
            count = 5
            while count > 0:
                countdown.append(count)
                count -= 1
            st.write("Countdown:", countdown)
            
            fruits = ["apple", "banana", "cherry"]
            indexed_fruits = []
            for idx, fruit in enumerate(fruits):
                indexed_fruits.append(f"{idx}: {fruit}")
            st.write("Indexed fruits:", indexed_fruits)
    
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
            
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age
                
                def introduce(self):
                    return f"Hi, I'm {self.name} and I'm {self.age} years old"
                
                def have_birthday(self):
                    self.age += 1
                    return f"Happy birthday! Now {self.age}"
            
            person = Person("Alice", 25)
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
            temp_fahrenheit = (temp_celsius * 9/5) + 32
            st.success(f"{temp_celsius}°C = {temp_fahrenheit}°F")
    
    with col2:
        st.code("""
# Temperature Converter
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
        """, language="python")
