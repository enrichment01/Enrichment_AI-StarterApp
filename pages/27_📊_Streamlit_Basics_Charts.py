import streamlit as st

from lib import helper_streamlit
from lib.helper_streamlit import utils


st.header("📈 Charts — Streamlit Basics")
st.markdown("Line, bar and area charts examples.")

st.markdown("**Code:**")
CODE = """
# Line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Output:**")
chart_data = utils.generate_chart_data()

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
    st.line_chart(chart_data)
with tab2:
    st.bar_chart(chart_data)
with tab3:
    st.area_chart(chart_data)
