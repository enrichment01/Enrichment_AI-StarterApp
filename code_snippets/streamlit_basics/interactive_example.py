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
