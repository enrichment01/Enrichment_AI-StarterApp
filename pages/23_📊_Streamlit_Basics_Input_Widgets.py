import streamlit as st

st.header("🎛️ Input Widgets — Streamlit Basics")
st.markdown("Interactive input widgets and examples.")

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
