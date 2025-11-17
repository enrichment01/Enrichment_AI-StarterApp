import streamlit as st



st.header("✂️ String Manipulation — Python Basics")
st.markdown("Common string operations and methods in Python.")

# Basic string operations
text = "  Hello, Python!  "

st.write("Original:", repr(text))
st.write("Stripped:", text.strip())
st.write("Lower case:", text.lower())
st.write("Upper case:", text.upper())
st.write("Title case:", text.title())

# String methods
message = "Python is awesome"

st.write("Replace:", message.replace("awesome", "amazing"))
st.write("Split:", message.split())
st.write("Starts with 'Python':", message.startswith("Python"))
st.write("Contains 'is':", "is" in message)

# String formatting
name = "Alice"
age = 30

st.write("f-string:", f"Name: {name}, Age: {age}")
st.write("format():", "Name: {}, Age: {}".format(name, age))
st.write("%-formatting:", "Name: %s, Age: %d" % (name, age))

# String slicing
text = "Programming"

st.write("First 4 chars:", text[:4])
st.write("Last 4 chars:", text[-4:])
st.write("Every 2nd char:", text[::2])
st.write("Reversed:", text[::-1])

# Joining strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)

st.write("Joined:", sentence)

