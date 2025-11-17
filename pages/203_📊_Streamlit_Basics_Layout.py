import streamlit as st

from lib import helper_streamlit
from lib.helper_streamlit import utils


st.header("📐 Layout — Streamlit Basics")
st.markdown("Organizing content with columns and tabs.")

st.markdown("**Columns:**")
CODE = """
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
with col3:
    st.write("Column 3")

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

col1, col2, col3 = st.columns(3)
with col1:
    st.info("Column 1")
with col2:
    st.success("Column 2")
with col3:
    st.warning("Column 3")

st.markdown("**Tabs:**")
CODE = """
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.write("Content 1")
with tab2:
    st.write("Content 2")
with tab3:
    st.write("Content 3")

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

tab1, tab2, tab3 = st.tabs(["📈 Chart", "📋 Data", "⚙️ Settings"])
with tab1:
    st.write("Chart content goes here")
    chart_data = utils.generate_chart_data()
    st.line_chart(chart_data)
with tab2:
    st.write("Data table goes here")
    st.dataframe(chart_data)
with tab3:
    st.write("Settings controls go here")
    st.checkbox("Enable feature X")
    st.checkbox("Enable feature Y")

