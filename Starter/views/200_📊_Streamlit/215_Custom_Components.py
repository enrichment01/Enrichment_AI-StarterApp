import streamlit as st
import pandas as pd
import numpy as np

st.header("🎨 Custom Components — Streamlit Basics")
st.markdown("Extending Streamlit with custom HTML, CSS, and JavaScript.")

# HTML rendering
st.subheader("Custom HTML")

html_code = """
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <h2 style="color: #ff4b4b;">Custom HTML Content</h2>
    <p>This is custom HTML rendered in Streamlit!</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)

# CSS styling
st.subheader("Custom CSS Styling")

st.markdown("""
<style>
.custom-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    margin: 10px 0;
}
.custom-box h3 {
    margin: 0;
    font-size: 24px;
}
</style>

<div class="custom-box">
    <h3>Styled with CSS</h3>
    <p>Beautiful gradient background!</p>
</div>
""", unsafe_allow_html=True)

# Colored metrics
st.subheader("Custom Styled Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background-color: #d4edda; padding: 15px; border-radius: 5px; border-left: 5px solid #28a745;">
        <h4 style="margin: 0; color: #155724;">Success Rate</h4>
        <h2 style="margin: 5px 0; color: #155724;">98.5%</h2>
        <p style="margin: 0; color: #155724;">↑ 2.3%</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color: #fff3cd; padding: 15px; border-radius: 5px; border-left: 5px solid #ffc107;">
        <h4 style="margin: 0; color: #856404;">Pending</h4>
        <h2 style="margin: 5px 0; color: #856404;">23</h2>
        <p style="margin: 0; color: #856404;">↓ 5</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="background-color: #f8d7da; padding: 15px; border-radius: 5px; border-left: 5px solid #dc3545;">
        <h4 style="margin: 0; color: #721c24;">Errors</h4>
        <h2 style="margin: 5px 0; color: #721c24;">3</h2>
        <p style="margin: 0; color: #721c24;">↓ 2</p>
    </div>
    """, unsafe_allow_html=True)

# Progress bars
st.subheader("Custom Progress Bars")

progress_html = """
<style>
.progress-container {
    width: 100%;
    background-color: #f0f2f6;
    border-radius: 10px;
    margin: 10px 0;
}
.progress-bar {
    height: 30px;
    background: linear-gradient(90deg, #11998e 0%, #38ef7d 100%);
    border-radius: 10px;
    text-align: center;
    line-height: 30px;
    color: white;
    font-weight: bold;
}
</style>

<div class="progress-container">
    <div class="progress-bar" style="width: 75%;">75%</div>
</div>

<div class="progress-container">
    <div class="progress-bar" style="width: 50%; background: linear-gradient(90deg, #3f51b5 0%, #2196f3 100%);">50%</div>
</div>

<div class="progress-container">
    <div class="progress-bar" style="width: 90%; background: linear-gradient(90deg, #f093fb 0%, #f5576c 100%);">90%</div>
</div>
"""

st.markdown(progress_html, unsafe_allow_html=True)

# Cards layout
st.subheader("Card Layout")

st.markdown("""
<style>
.card {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin: 10px 0;
}
.card h3 {
    color: #333;
    margin-top: 0;
}
.card p {
    color: #666;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🚀 Feature 1</h3>
        <p>Fast and efficient processing with optimized algorithms.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>💡 Feature 2</h3>
        <p>Intelligent insights powered by machine learning.</p>
    </div>
    """, unsafe_allow_html=True)

# Badges and tags
st.subheader("Badges and Tags")

st.markdown("""
<style>
.badge {
    display: inline-block;
    padding: 5px 10px;
    margin: 3px;
    border-radius: 15px;
    font-size: 12px;
    font-weight: bold;
}
.badge-primary { background-color: #007bff; color: white; }
.badge-success { background-color: #28a745; color: white; }
.badge-warning { background-color: #ffc107; color: black; }
.badge-danger { background-color: #dc3545; color: white; }
</style>

<div>
    <span class="badge badge-primary">Python</span>
    <span class="badge badge-success">Active</span>
    <span class="badge badge-warning">Beta</span>
    <span class="badge badge-danger">Important</span>
</div>
""", unsafe_allow_html=True)

# Interactive example
st.subheader("🎮 Try It Yourself")

bg_color = st.color_picker("Choose background color", "#667eea")
text_color = st.color_picker("Choose text color", "#ffffff")
border_radius = st.slider("Border radius (px)", 0, 50, 10)
padding = st.slider("Padding (px)", 10, 50, 20)

custom_style = f"""
<div style="background-color: {bg_color}; 
            color: {text_color}; 
            padding: {padding}px; 
            border-radius: {border_radius}px;
            text-align: center;">
    <h3 style="margin: 0;">Custom Styled Box</h3>
    <p>Adjust the controls to change styling!</p>
</div>
"""

st.markdown(custom_style, unsafe_allow_html=True)

# Tips
st.subheader("💡 Tips for Custom Components")

st.info("""
- **Security**: Use `unsafe_allow_html=True` carefully
- **Responsive**: Test on different screen sizes
- **Performance**: Minimize complex CSS/JS
- **Accessibility**: Ensure good color contrast
- **Compatibility**: Test across browsers
- **Maintenance**: Keep custom code documented
""")

# Warning
st.warning("""
⚠️ **Security Note**: Only use `unsafe_allow_html=True` with trusted content. 
Never render user-provided HTML without sanitization.
""")
