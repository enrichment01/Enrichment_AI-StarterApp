# Text input
name = st.text_input("Enter your name")

# Number input
age = st.number_input("Enter your age", 0, 100)

# Slider
value = st.slider("Select a value", 0, 100)

# Select box
option = st.selectbox("Choose", ["A", "B", "C"])

# Checkbox
agree = st.checkbox("I agree")

# Button
if st.button("Click me"):
    st.write("Button clicked!")
