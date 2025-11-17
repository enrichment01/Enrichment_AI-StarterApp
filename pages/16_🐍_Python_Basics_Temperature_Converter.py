import streamlit as st

st.header("🌡️ Temperature Converter — Python Basics")
st.markdown("Convert Celsius to Fahrenheit and view the example code.")

celsius = st.number_input("Enter temperature in Celsius:", value=25.0)

if st.button("Convert to Fahrenheit"):
    fahrenheit = (celsius * 9 / 5) + 32

    st.success(f"{celsius}°C = {fahrenheit}°F")
