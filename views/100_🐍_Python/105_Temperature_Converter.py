import streamlit as st

from lib.helper_streamlit import show_code


st.header("🌡️ Temperature Converter — Python Basics")
st.markdown("Convert Celsius to Fahrenheit and view the example code.")

# --- CODE START
celsius = st.number_input("Enter temperature in Celsius:", value=25.0)

if st.button("Convert to Fahrenheit"):
    fahrenheit = (celsius * 9 / 5) + 32

    st.success(f"{celsius}°C = {fahrenheit}°F")
# --- CODE END

# =================================================================================================
show_code(__file__)

# --- CODE START: OUTPUT
st.subheader("Result:")
# --- CODE END: OUTPUT

