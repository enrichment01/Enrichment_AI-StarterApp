import streamlit as st
import pandas as pd
import numpy as np
import time
from scripts import streamlit_utils, code_utils

def show():
    st.header("📊 Streamlit Basics")
    st.markdown("Learn how to build interactive web apps with Streamlit.")
    
    # Text Elements
    with st.expander("📝 Text Elements", expanded=True):
        st.subheader("Displaying Text")
        
        st.markdown("**Code:**")
        CODE = code_utils.get_code("streamlit_basics/text_elements.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        st.markdown("**Output:**")
        st.title("This is a title")
        st.header("This is a header")
        st.subheader("This is a subheader")
        st.text("This is plain text")
        st.markdown("This is **markdown** with *formatting*")
        st.caption("This is a caption")
    
    # Data Display
    with st.expander("📊 Data Display"):
        st.subheader("Displaying Data")
        
        st.markdown("**Code:**")
        CODE = code_utils.get_code("streamlit_basics/data_display.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        st.markdown("**Output:**")
        df = streamlit_utils.generate_sample_dataframe()
        st.dataframe(df)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Temperature", "25°C", "2°C")
        with col2:
            st.metric("Humidity", "65%", "-5%")
        with col3:
            st.metric("Wind Speed", "15 km/h", "3 km/h")
        
        st.json({'name': 'Alice', 'age': 25, 'city': 'New York'})
    
    # Input Widgets
    with st.expander("🎛️ Input Widgets"):
        st.subheader("Interactive Widgets")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Code:**")
            CODE = code_utils.get_code("streamlit_basics/input_widgets.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
        with col2:
            st.markdown("**Try it:**")
            name = st.text_input("Enter your name", key="name_input")
            if name:
                st.write(f"Hello, {name}!")
            
            age = st.number_input("Enter your age", 0, 100, key="age_input")
            if age > 0:
                st.write(f"You are {age} years old")
            
            value = st.slider("Select a value", 0, 100, key="slider_input")
            st.write(f"Selected: {value}")
            
            option = st.selectbox("Choose an option", ["Option A", "Option B", "Option C"], key="select_input")
            st.write(f"You chose: {option}")
            
            agree = st.checkbox("I agree to terms", key="checkbox_input")
            if agree:
                st.write("✅ Agreed!")
            
            if st.button("Click me", key="button_input"):
                st.success("Button clicked! 🎉")
    
    # Layout
    with st.expander("📐 Layout"):
        st.subheader("Organizing Content")
        
        st.markdown("**Columns:**")
        CODE = code_utils.get_code("streamlit_basics/layout_columns.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("Column 1")
        with col2:
            st.success("Column 2")
        with col3:
            st.warning("Column 3")
        
        st.markdown("**Tabs:**")
        CODE = code_utils.get_code("streamlit_basics/layout_tabs.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        tab1, tab2, tab3 = st.tabs(["📈 Chart", "📋 Data", "⚙️ Settings"])
        with tab1:
            st.write("Chart content goes here")
            chart_data = streamlit_utils.generate_chart_data()
            st.line_chart(chart_data)
        with tab2:
            st.write("Data table goes here")
            st.dataframe(chart_data)
        with tab3:
            st.write("Settings controls go here")
            st.checkbox("Enable feature X")
            st.checkbox("Enable feature Y")
    
    # Charts
    with st.expander("📈 Charts"):
        st.subheader("Visualizations")
        
        st.markdown("**Code:**")
        CODE = code_utils.get_code("streamlit_basics/charts.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        st.markdown("**Output:**")
        chart_data = streamlit_utils.generate_chart_data()
        
        tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
        with tab1:
            st.line_chart(chart_data)
        with tab2:
            st.bar_chart(chart_data)
        with tab3:
            st.area_chart(chart_data)
    
    # Status Elements
    with st.expander("🎨 Status Elements"):
        st.subheader("Messages and Notifications")
        
        st.markdown("**Code:**")
        CODE = code_utils.get_code("streamlit_basics/status_elements.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        st.markdown("**Output:**")
        st.success("Success message! ✅")
        st.info("Info message ℹ️")
        st.warning("Warning message ⚠️")
        st.error("Error message ❌")
    
    # Progress and Spinners
    with st.expander("⏳ Progress Indicators"):
        st.subheader("Progress and Spinners")
        
        st.markdown("**Code:**")
        CODE = code_utils.get_code("streamlit_basics/progress_indicators.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
        
        if st.button("Run Progress Demo", key="progress_demo"):
            progress = st.progress(0)
            status_text = st.empty()
            for i in range(100):
                progress.progress(i + 1)
                status_text.text(f"Progress: {i + 1}%")
                time.sleep(0.02)
            status_text.text("Complete!")
            st.success("Done! 🎉")
    
    # Interactive Example
    st.markdown("---")
    st.subheader("🎮 Interactive Example: Data Dashboard")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**Generate Random Data:**")
        num_rows = st.slider("Number of rows", 10, 100, 50)
        num_cols = st.slider("Number of columns", 1, 5, 3)
        
        if st.button("Generate Data", key="generate_data"):
            random_data = streamlit_utils.generate_random_data(num_rows, num_cols)
            
            st.write(f"Generated {num_rows} rows × {num_cols} columns:")
            st.dataframe(random_data)
            
            st.line_chart(random_data)
            
            st.write("Statistics:")
            st.dataframe(random_data.describe())
    
    with col2:
        st.markdown("**Code:**")
        CODE = code_utils.get_code("streamlit_basics/interactive_example.py")
        st.code(CODE, language="python")
        code_utils.run_code(CODE)
