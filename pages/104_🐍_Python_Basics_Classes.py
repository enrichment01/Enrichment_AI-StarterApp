import streamlit as st

from lib.helper_streamlit import show_code

st.header("�️ Classes — Python Basics")
st.markdown("Defining classes, instances, and basic OOP patterns.")

# --- CODE START
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
# --- CODE END

# =================================================================================================
show_code(__file__)

st.subheader("Result:")

# --- CODE START: OUTPUT
st.write(person.introduce())
st.write(person.have_birthday())
st.write(person.introduce())
# --- CODE END: OUTPUT
