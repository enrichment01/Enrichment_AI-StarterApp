import streamlit as st

from lib import helper_streamlit


st.header("🎨 Status Elements — Streamlit Basics")
st.markdown("Messages and notifications examples.")

st.markdown("**Output:**")
st.success("Success message! ✅")
st.info("Info message ℹ️")
st.warning("Warning message ⚠️")
st.error("Error message ❌")
