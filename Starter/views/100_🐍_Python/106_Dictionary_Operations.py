import streamlit as st

from lib.helper_streamlit import show_code

st.header("📚 Dictionary Operations — Python Basics")
st.markdown("Working with dictionaries: creation, access, and common operations.")

# --- CODE START
# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "NYC"}
scores = dict(math=95, science=88, english=92)

# Adding/updating
person["email"] = "alice@example.com"
person["age"] = 31

# Merging dictionaries
defaults = {"theme": "dark", "language": "en"}
settings = {"theme": "light"}
merged = {**defaults, **settings}

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
# --- CODE END

# =================================================================================================
show_code(__file__)
st.subheader("Result:")

# --- CODE START: OUTPUT
st.write("Person dictionary:", person)
st.write("Scores dictionary:", scores)
st.write("Name:", person["name"]) 
st.write("Math score:", scores.get("math"))
st.write("After updates:", person)
st.write("Keys:", list(person.keys()))
st.write("Values:", list(person.values()))
st.write("Items:", list(person.items()))
st.write("Squared numbers:", squared)
st.write("Merged settings:", merged)
# --- CODE END: OUTPUT
