import streamlit as st
import pandas as pd
import numpy as np

st.header("📦 Container Elements — Streamlit Basics")
st.markdown("Using containers to organize and control layout.")

# Basic container
st.subheader("Basic Container")

container1 = st.container()
container1.write("This is inside a container")
container1.button("Container Button 1")

st.write("This is outside the container")

container1.write("This also goes in the first container!")
container1.metric("Container Metric", "42")

# Container with border
st.subheader("Container with Border")

with st.container(border=True):
    st.write("**Bordered Container**")
    st.write("This container has a visible border")
    st.slider("Value", 0, 100, 50)

# Multiple containers
st.subheader("Multiple Containers")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.write("**Container 1**")
        st.write("Left container content")
        st.checkbox("Option 1")

with col2:
    with st.container(border=True):
        st.write("**Container 2**")
        st.write("Right container content")
        st.checkbox("Option 2")

# Empty container (dynamic updates)
st.subheader("Dynamic Container Updates")

placeholder = st.empty()

if st.button("Update Content"):
    placeholder.success("✅ Content updated!")

if st.button("Show Chart"):
    with placeholder.container():
        data = pd.DataFrame(
            np.random.randn(10, 2),
            columns=['A', 'B']
        )
        st.line_chart(data)

if st.button("Clear"):
    placeholder.empty()

# Nested containers
st.subheader("Nested Containers")

with st.container(border=True):
    st.write("**Outer Container**")
    
    with st.container(border=True):
        st.write("**Inner Container 1**")
        st.write("Nested content")
    
    with st.container(border=True):
        st.write("**Inner Container 2**")
        st.write("More nested content")

# Container for grouping
st.subheader("Grouping Related Elements")

with st.container(border=True):
    st.write("**User Profile**")
    
    name = st.text_input("Name", key="profile_name")
    email = st.text_input("Email", key="profile_email")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 0, 120, 25)
    with col2:
        city = st.text_input("City")
    
    if st.button("Save Profile"):
        st.success("Profile saved!")

# Container with expander
st.subheader("Container with Expander")

with st.container(border=True):
    st.write("**Settings**")
    
    with st.expander("Advanced Options"):
        st.checkbox("Enable debugging")
        st.checkbox("Verbose logging")
        st.slider("Timeout (seconds)", 1, 60, 30)

# Sidebar container
st.sidebar.subheader("Sidebar Container")

with st.sidebar.container(border=True):
    st.write("**Quick Actions**")
    st.button("Action 1", key="sidebar_action1")
    st.button("Action 2", key="sidebar_action2")
    st.button("Action 3", key="sidebar_action3")

# Tips
st.subheader("💡 Container Tips")

st.info("""
- **Organization**: Group related widgets together
- **Border**: Use `border=True` for visual separation
- **Dynamic**: Use `st.empty()` for replaceable content
- **Nesting**: Containers can be nested for complex layouts
- **Out-of-order**: Add content to containers after creation
- **Scope**: Containers don't affect widget state/keys
""")

# Example patterns
st.subheader("📋 Common Patterns")

patterns = """
# Pattern 1: Card-like sections
with st.container(border=True):
    st.subheader("Section Title")
    st.write("Content...")

# Pattern 2: Dynamic updates
placeholder = st.empty()
# Later...
placeholder.write("New content")

# Pattern 3: Grouped form elements
with st.container(border=True):
    st.write("**Form Section**")
    # form fields...
"""

st.code(patterns, language="python")
