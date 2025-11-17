import streamlit as st
import pandas as pd
import numpy as np

st.header("📂 Expander and Accordion — Streamlit Basics")
st.markdown("Collapsible sections for better content organization.")

# Basic expander
st.subheader("Basic Expander")

with st.expander("Click to expand"):
    st.write("This content is hidden by default")
    st.write("Click the expander to reveal it")

# Expander with default state
st.subheader("Expanded by Default")

with st.expander("Already Expanded", expanded=True):
    st.write("This expander starts in the open state")
    st.info("Set `expanded=True` to open by default")

# Multiple expanders (accordion pattern)
st.subheader("Accordion Pattern")

with st.expander("📚 What is Streamlit?"):
    st.write("""
    Streamlit is an open-source Python library that makes it easy to create 
    and share beautiful, custom web apps for machine learning and data science.
    """)

with st.expander("🚀 How to install?"):
    st.code("pip install streamlit", language="bash")
    st.write("Then run your app with:")
    st.code("streamlit run app.py", language="bash")

with st.expander("💡 Key features"):
    st.write("- Fast development")
    st.write("- Pure Python")
    st.write("- Interactive widgets")
    st.write("- Real-time updates")

# Expander with complex content
st.subheader("Expander with Charts and Data")

with st.expander("📊 View Data Analysis"):
    # Generate sample data
    data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.write("**Data Table:**")
    st.dataframe(data)
    
    st.write("**Line Chart:**")
    st.line_chart(data)
    
    st.write("**Statistics:**")
    st.write(data.describe())

# Expander with forms
st.subheader("Expander with Interactive Elements")

with st.expander("⚙️ Settings"):
    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
    font_size = st.slider("Font Size", 10, 20, 14)
    notifications = st.checkbox("Enable notifications")
    
    if st.button("Save Settings"):
        st.success(f"✅ Saved: Theme={theme}, Size={font_size}, Notifications={notifications}")

# Nested expanders
st.subheader("Nested Expanders")

with st.expander("🗂️ Main Category"):
    st.write("Main category content")
    
    with st.expander("📁 Subcategory 1"):
        st.write("Subcategory 1 content")
        st.button("Action 1")
    
    with st.expander("📁 Subcategory 2"):
        st.write("Subcategory 2 content")
        st.button("Action 2")

# FAQ example
st.subheader("FAQ Example")

faqs = {
    "How do I install Streamlit?": "Run `pip install streamlit` in your terminal.",
    "Can I use Streamlit for free?": "Yes! Streamlit is open-source and free to use.",
    "How do I deploy my app?": "Use Streamlit Community Cloud, Heroku, AWS, or any platform supporting Python.",
    "Does Streamlit support authentication?": "Not built-in, but you can use third-party libraries.",
    "Can I customize the theme?": "Yes, using the config.toml file or theme settings."
}

for question, answer in faqs.items():
    with st.expander(f"❓ {question}"):
        st.write(answer)

# Expander with code examples
st.subheader("Code Documentation")

with st.expander("🐍 Python Example"):
    st.code("""
def hello(name):
    return f"Hello, {name}!"

print(hello("World"))
    """, language="python")

with st.expander("📊 Chart Example"):
    st.code("""
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)
    """, language="python")

# Tips
st.subheader("💡 Expander Tips")

st.info("""
- **Organization**: Hide optional or detailed content
- **Space-saving**: Keep interface clean and focused
- **Default state**: Use `expanded=True/False`
- **Nesting**: Expanders can be nested for hierarchy
- **Icon**: Add emoji or icons to expander labels
- **Content**: Can contain any Streamlit element
""")

# Best practices
st.subheader("📋 Best Practices")

with st.expander("View Best Practices"):
    st.markdown("""
    1. **Clear labels**: Use descriptive expander titles
    2. **Logical grouping**: Group related content together
    3. **Important content**: Keep crucial info outside expanders
    4. **Nested sparingly**: Avoid too many nesting levels
    5. **Loading**: Use expanders for heavy content to improve load time
    """)
