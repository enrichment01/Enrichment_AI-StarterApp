import streamlit as st

from lib import helper_streamlit


st.header("📝 Text Elements — Streamlit Basics")
st.markdown("Displaying various text elements in Streamlit.")

st.markdown("**Code:**")
CODE = """
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is plain text")
st.markdown("This is **markdown** with *formatting*")
st.caption("This is a caption")

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

st.markdown("**Output:**")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is plain text")
st.markdown("This is **markdown** with *formatting*")
st.caption("This is a caption")
