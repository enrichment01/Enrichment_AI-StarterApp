import streamlit as st

st.title("⚡ Streamlit Hello")

st.subheader("Welcome to Streamlit")

st.write(
    """
    Streamlit is an open-source app framework built specifically for
    machine learning and data science projects.

    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!

    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
      forums](https://discuss.streamlit.io)

    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
      Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
)

# Preload Python modules that take a while to compile in a new venv.
# Otherwise, when users switch to another page, it seems that Streamlit
# is slow, when in reality this is just an artifact of loading/compiling
# large modules from zero.
with st.spinner("Preloading Python modules for other pages..."):
    import numpy  # noqa: ICN001 F401
    import pandas  # noqa: ICN001 F401