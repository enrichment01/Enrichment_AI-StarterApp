import streamlit as st

st.header("🎯 List Comprehensions Advanced — Python Basics")
st.markdown("Advanced list comprehension patterns and techniques.")

# Nested list comprehensions
st.subheader("Nested List Comprehensions")

matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
st.write("Multiplication table (3x3):", matrix)

# Flatten nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in nested for num in row]
st.write("Flattened:", flattened)

# Conditional list comprehensions
st.subheader("Conditional Comprehensions")

numbers = list(range(1, 21))

# Filter: only even numbers
evens = [n for n in numbers if n % 2 == 0]
st.write("Even numbers:", evens)

# Transform with condition
squared_evens = [n**2 for n in numbers if n % 2 == 0]
st.write("Squared evens:", squared_evens)

# If-else in comprehension
labels = ["even" if n % 2 == 0 else "odd" for n in range(10)]
st.write("Labels:", labels)

# Dictionary comprehensions
st.subheader("Dictionary Comprehensions")

# Square numbers
squares_dict = {n: n**2 for n in range(1, 6)}
st.write("Squares:", squares_dict)

# Filter dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
high_scores = {name: score for name, score in scores.items() if score >= 85}
st.write("High scores (>=85):", high_scores)

# Swap keys and values
swapped = {v: k for k, v in scores.items()}
st.write("Swapped (score: name):", swapped)

# Set comprehensions
st.subheader("Set Comprehensions")

# Unique remainders
remainders = {n % 5 for n in range(20)}
st.write("Unique remainders (mod 5):", remainders)

# Complex example: Pythagorean triples
st.subheader("Complex Example: Pythagorean Triples")

triples = [(a, b, c) for a in range(1, 15) 
            for b in range(a, 15) 
            for c in range(b, 15) 
            if a**2 + b**2 == c**2]

st.write("Pythagorean triples (a² + b² = c²):")
for triple in triples[:5]:  # Show first 5
    st.write(f"{triple[0]}² + {triple[1]}² = {triple[2]}²")
