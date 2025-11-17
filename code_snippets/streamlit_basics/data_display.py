# DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
})
st.dataframe(df)

# Metrics
st.metric("Temperature", "25°C", "2°C")

# JSON
st.json({'name': 'Alice', 'age': 25})
