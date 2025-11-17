import streamlit as st

st.header("📚 Dictionary Operations — Python Basics")
st.markdown("Working with dictionaries: creation, access, and common operations.")

# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "NYC"}
scores = dict(math=95, science=88, english=92)

st.write("Person dictionary:", person)
st.write("Scores dictionary:", scores)

# Accessing values
st.write("Name:", person["name"])
st.write("Math score:", scores.get("math"))

# Adding/updating
person["email"] = "alice@example.com"
person["age"] = 31

st.write("After updates:", person)

# Dictionary methods
st.write("Keys:", list(person.keys()))
st.write("Values:", list(person.values()))
st.write("Items:", list(person.items()))

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
st.write("Squared numbers:", squared)

# Merging dictionaries
defaults = {"theme": "dark", "language": "en"}
settings = {"theme": "light"}
merged = {**defaults, **settings}

st.write("Merged settings:", merged)
