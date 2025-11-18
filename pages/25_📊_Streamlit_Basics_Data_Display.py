import streamlit as st

from lib import helper_streamlit
from lib.helper_streamlit import utils


st.header("📊 Data Display — Streamlit Basics")
st.markdown("Showing dataframes, metrics and JSON in Streamlit.")

st.markdown("**Code:**")
CODE = """
import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

st.code('df.head()', language='python')
st.code('st.dataframe(df)')

df = df
st.dataframe(df)

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Output:**")
df = utils.generate_sample_dataframe()
st.dataframe(df)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Temperature", "25°C", "2°C")
with col2:
    st.metric("Humidity", "65%", "-5%")
with col3:
    st.metric("Wind Speed", "15 km/h", "3 km/h")

st.json({'name': 'Alice', 'age': 25, 'city': 'New York'})
