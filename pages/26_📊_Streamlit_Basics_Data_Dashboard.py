import streamlit as st

from lib import helper_streamlit
from lib.helper_streamlit import utils


st.header("🎮 Data Dashboard — Streamlit Basics")
st.markdown("Interactive dashboard demo: generate random data and visualize it.")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("**Generate Random Data:**")
    num_rows = st.slider("Number of rows", 10, 100, 50)
    num_cols = st.slider("Number of columns", 1, 5, 3)
    
    if st.button("Generate Data", key="generate_data_dashboard"):
        random_data = utils.generate_random_data(num_rows, num_cols)
        
        st.write(f"Generated {num_rows} rows × {num_cols} columns:")
        st.dataframe(random_data)
        
        st.line_chart(random_data)
        
        st.write("Statistics:")
        st.dataframe(random_data.describe())

with col2:
    st.markdown("**Code:**")
    CODE = """
num_rows = 50
num_cols = 3

data = pd.DataFrame(
    np.random.randn(
        num_rows, 
        num_cols
    ),
    columns=[
        f'Col {i+1}' 
        for i in range(num_cols)
    ]
)

st.dataframe(data)
st.line_chart(data)
st.dataframe(data.describe())

"""
    st.code(CODE, language="python")
    helper_streamlit.run_code(CODE)
