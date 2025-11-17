import streamlit as st

st.header("🏗️ Classes and Objects — Python Basics")
st.markdown("A short introduction to classes and objects in Python.")

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

st.write(person.introduce())
st.write(person.have_birthday())
st.write(person.introduce())
