import streamlit as st
import time

from lib import helper_streamlit


st.header("⏳ Progress Indicators — Streamlit Basics")
st.markdown("Progress bars and spinners with demo code.")

st.markdown("**Code:**")
CODE = """
# Progress bar
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.01)

# Spinner
with st.spinner("Loading..."):
    time.sleep(2)
st.success("Done!")

"""
st.code(CODE, language="python")
helper_streamlit.run_code(CODE)

if st.button("Run Progress Demo", key="progress_demo"):
    progress = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        progress.progress(i + 1)
        status_text.text(f"Progress: {i + 1}%")
        time.sleep(0.02)
    status_text.text("Complete!")
    st.success("Done! 🎉")
