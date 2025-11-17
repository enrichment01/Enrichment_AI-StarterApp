import streamlit as st
import pandas as pd
import numpy as np
from scripts import python_utils, code_utils

def show():
    st.header("🐍 Python Basics")
    st.markdown("Learn fundamental Python concepts through interactive examples.")
    
    # Data Types Section
    with st.expander("📦 Data Types", expanded=True):
        st.subheader("Basic Data Types")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            CODE = code_utils.get_code("python_basics/data_types.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
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
            CODE = code_utils.get_code("python_basics/list_operations.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
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
            CODE = code_utils.get_code("python_basics/functions.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
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
            CODE = code_utils.get_code("python_basics/loops.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
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
            CODE = code_utils.get_code("python_basics/classes.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
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
        CODE = code_utils.get_code("python_basics/temperature_converter.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
