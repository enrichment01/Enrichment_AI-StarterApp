import streamlit as st

st.set_page_config(page_title="Streamlit Hello", page_icon="⚡", layout="wide")

streamlit_hello = [
    st.Page("views/streamlit_hello/1_Animation_Demo.py", title="🏠 Animation"),
    st.Page("views/streamlit_hello/2_Dataframe_Demo.py", title="🗺️ DataFrame"),
    st.Page("views/streamlit_hello/3_Mapping_Demo.py", title="📹 Mapping"),
    st.Page("views/streamlit_hello/4_Plotting_Demo.py", title="📊 Plotting"),
]

navigation = st.navigation(
    pages={
        "🏠 Start": [st.Page("views/Start.py", title="Übersicht")],
        "🔷 Demo": streamlit_hello,
    },
    expanded=False
)
navigation.run()
