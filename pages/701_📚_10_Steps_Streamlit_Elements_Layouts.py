import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="10 Steps: Streamlit Elements & Layouts", page_icon="📚", layout="wide")

st.title("📚 10 Steps to Master Streamlit Elements and Layouts")
st.markdown("A comprehensive guide to learn Streamlit's UI elements and layout capabilities.")

# Create tabs for each step
tabs = st.tabs([
    "Text",
    "Data",
    "Charts",
    "Input",
    "Columns",
    "Tabs",
    "Expanders",
    "Sidebar",
    "Forms",
    "Complete Example"
])

# Step 1: Text Elements
with tabs[0]:
    st.header("Step 1: Text Elements")
    st.markdown("Learn how to display text in various formats.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Example:")
        st.title("This is a Title")
        st.header("This is a Header")
        st.subheader("This is a Subheader")
        st.text("This is plain text")
        st.markdown("This is **bold** and *italic* markdown")
        st.caption("This is a caption for small text")
        st.code("print('Hello, World!')", language="python")
    
    with col2:
        st.markdown("### Code:")
        code = """
st.title("This is a Title")
st.header("This is a Header")
st.subheader("This is a Subheader")
st.text("This is plain text")
st.markdown("This is **bold** and *italic* markdown")
st.caption("This is a caption for small text")
st.code("print('Hello, World!')", language="python")
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** Use markdown for formatted text with headers, lists, links, and emphasis.")

# Step 2: Data Display
with tabs[1]:
    st.header("Step 2: Data Display Elements")
    st.markdown("Display data using dataframes, tables, and metrics.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Example:")
        
        # Sample data
        df = pd.DataFrame({
            'Product': ['Apple', 'Banana', 'Cherry', 'Date'],
            'Price': [1.2, 0.5, 2.5, 3.0],
            'Stock': [100, 150, 80, 60]
        })
        
        st.markdown("**DataFrame (Interactive):**")
        st.dataframe(df, use_container_width=True)
        
        st.markdown("**Static Table:**")
        st.table(df.head(2))
        
        st.markdown("**Metrics:**")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Total Products", "4", "+2")
        col_b.metric("Avg Price", "$1.80", "-$0.20")
        col_c.metric("Total Stock", "390", "+50")
    
    with col2:
        st.markdown("### Code:")
        code = """
import pandas as pd

df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Cherry', 'Date'],
    'Price': [1.2, 0.5, 2.5, 3.0],
    'Stock': [100, 150, 80, 60]
})

# Interactive dataframe
st.dataframe(df, use_container_width=True)

# Static table
st.table(df.head(2))

# Metrics
col_a, col_b, col_c = st.columns(3)
col_a.metric("Total Products", "4", "+2")
col_b.metric("Avg Price", "$1.80", "-$0.20")
col_c.metric("Total Stock", "390", "+50")
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Use dataframe for large interactive data, table for static display, and metrics for KPIs.")

# Step 3: Charts and Visualizations
with tabs[2]:
    st.header("Step 3: Charts and Visualizations")
    st.markdown("Create beautiful charts with simple commands.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Example:")
        
        # Sample chart data
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['A', 'B', 'C']
        )
        
        st.markdown("**Line Chart:**")
        st.line_chart(chart_data)
        
        st.markdown("**Bar Chart:**")
        bar_data = pd.DataFrame({
            'Category': ['X', 'Y', 'Z'],
            'Values': [10, 25, 15]
        })
        st.bar_chart(bar_data.set_index('Category'))
    
    with col2:
        st.markdown("### Code:")
        code = """
import pandas as pd
import numpy as np

# Line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Bar chart
bar_data = pd.DataFrame({
    'Category': ['X', 'Y', 'Z'],
    'Values': [10, 25, 15]
})
st.bar_chart(bar_data.set_index('Category'))
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** Streamlit also supports area_chart, scatter_chart, and map for geographical data.")

# Step 4: Input Widgets
with tabs[3]:
    st.header("Step 4: Input Widgets")
    st.markdown("Collect user input with various interactive widgets.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Example:")
        
        name = st.text_input("Enter your name:", "John Doe")
        age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
        rating = st.slider("Rate your experience:", 0, 10, 5)
        option = st.selectbox("Choose an option:", ["Option A", "Option B", "Option C"])
        agree = st.checkbox("I agree to the terms")
        
        if st.button("Submit"):
            st.write(f"Name: {name}, Age: {age}, Rating: {rating}, Option: {option}, Agreed: {agree}")
    
    with col2:
        st.markdown("### Code:")
        code = """
name = st.text_input("Enter your name:", "John Doe")
age = st.number_input("Enter your age:", 
                      min_value=0, max_value=120, value=25)
rating = st.slider("Rate your experience:", 0, 10, 5)
option = st.selectbox("Choose an option:", 
                      ["Option A", "Option B", "Option C"])
agree = st.checkbox("I agree to the terms")

if st.button("Submit"):
    st.write(f"Name: {name}, Age: {age}")
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Input widgets automatically trigger re-runs when values change.")

# Step 5: Columns Layout
with tabs[4]:
    st.header("Step 5: Columns Layout")
    st.markdown("Organize content side by side using columns.")
    
    st.markdown("### Example: 3-Column Layout")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown("**Column 1**")
        st.info("This is the first column with ratio 1")
        st.write("Content goes here")
    
    with col2:
        st.markdown("**Column 2**")
        st.success("This is the wider middle column with ratio 2")
        st.write("More content here")
    
    with col3:
        st.markdown("**Column 3**")
        st.warning("This is the third column with ratio 1")
        st.write("Last column")
    
    st.markdown("### Code:")
    code = """
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("**Column 1**")
    st.info("This is the first column with ratio 1")

with col2:
    st.markdown("**Column 2**")
    st.success("This is the wider middle column with ratio 2")

with col3:
    st.markdown("**Column 3**")
    st.warning("This is the third column with ratio 1")
"""
    st.code(code, language="python")
    
    st.info("💡 **Tip:** Column ratios [1, 2, 1] means the middle column is twice as wide as the others.")

# Step 6: Tabs Layout
with tabs[5]:
    st.header("Step 6: Tabs Layout")
    st.markdown("Organize content into tabs for better navigation.")
    
    st.markdown("### Example: Tab Navigation")
    
    inner_tabs = st.tabs(["🏠 Home", "📊 Data", "⚙️ Settings"])
    
    with inner_tabs[0]:
        st.markdown("### Welcome Tab")
        st.write("This is the home tab content.")
        st.balloons()
    
    with inner_tabs[1]:
        st.markdown("### Data Tab")
        sample_data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
        st.dataframe(sample_data)
    
    with inner_tabs[2]:
        st.markdown("### Settings Tab")
        st.write("Configuration options go here.")
        enable = st.checkbox("Enable feature")
        st.write(f"Feature enabled: {enable}")
    
    st.markdown("### Code:")
    code = """
tabs = st.tabs(["🏠 Home", "📊 Data", "⚙️ Settings"])

with tabs[0]:
    st.markdown("### Welcome Tab")
    st.write("This is the home tab content.")

with tabs[1]:
    st.markdown("### Data Tab")
    sample_data = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    st.dataframe(sample_data)

with tabs[2]:
    st.markdown("### Settings Tab")
    enable = st.checkbox("Enable feature")
"""
    st.code(code, language="python")
    
    st.success("✅ **Key Point:** Tabs are perfect for organizing related content without scrolling.")

# Step 7: Expanders and Containers
with tabs[6]:
    st.header("Step 7: Expanders and Containers")
    st.markdown("Control content visibility with expanders and organize with containers.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Expander Example:")
        
        with st.expander("📖 Click to expand details"):
            st.write("This content is hidden by default")
            st.write("It helps keep your app clean and organized")
            st.code("hidden_data = [1, 2, 3, 4, 5]", language="python")
        
        with st.expander("🔍 More Information", expanded=True):
            st.write("This expander is open by default")
    
    with col2:
        st.markdown("### Container Example:")
        
        container = st.container()
        container.write("This is inside a container")
        container.success("Containers help group related elements")
        
        st.write("This is outside the container")
    
    st.markdown("### Code:")
    code = """
# Expander (collapsed by default)
with st.expander("📖 Click to expand details"):
    st.write("This content is hidden by default")
    st.code("hidden_data = [1, 2, 3, 4, 5]", language="python")

# Expander (expanded by default)
with st.expander("🔍 More Information", expanded=True):
    st.write("This expander is open by default")

# Container
container = st.container()
container.write("This is inside a container")
container.success("Containers help group related elements")
"""
    st.code(code, language="python")
    
    st.info("💡 **Tip:** Use expanders for optional/advanced content and containers to group related elements.")

# Step 8: Sidebar Elements
with tabs[7]:
    st.header("Step 8: Sidebar Elements")
    st.markdown("Add controls and information to the sidebar.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Sidebar Features:")
        st.write("Check the sidebar on the left to see sidebar elements in action!")
        
        # Add to sidebar
        with st.sidebar:
            st.markdown("### Sidebar Demo")
            st.info("This is in the sidebar!")
            
            sidebar_input = st.text_input("Sidebar Input:", "Type here", key="sidebar_demo_input")
            sidebar_slider = st.slider("Sidebar Slider:", 0, 100, 50, key="sidebar_demo_slider")
            
            if st.button("Sidebar Button", key="sidebar_demo_button"):
                st.success("Button clicked!")
        
        st.write(f"Sidebar Input: {st.session_state.get('sidebar_demo_input', 'N/A')}")
        st.write(f"Sidebar Slider: {st.session_state.get('sidebar_demo_slider', 'N/A')}")
    
    with col2:
        st.markdown("### Code:")
        code = """
# Method 1: Using with statement
with st.sidebar:
    st.markdown("### Sidebar Demo")
    st.info("This is in the sidebar!")
    
    sidebar_input = st.text_input("Sidebar Input:", "Type here")
    sidebar_slider = st.slider("Sidebar Slider:", 0, 100, 50)
    
    if st.button("Sidebar Button"):
        st.success("Button clicked!")

# Method 2: Direct call
st.sidebar.selectbox("Choose:", ["A", "B", "C"])
st.sidebar.checkbox("Enable feature")
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Sidebar is perfect for navigation, settings, and filters.")

# Step 9: Forms
with tabs[8]:
    st.header("Step 9: Forms")
    st.markdown("Group inputs together and submit them all at once.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Example Form:")
        
        with st.form("demo_form"):
            st.markdown("**User Registration**")
            
            form_name = st.text_input("Full Name:")
            form_email = st.text_input("Email:")
            form_age = st.number_input("Age:", min_value=18, max_value=100, value=25)
            form_country = st.selectbox("Country:", ["USA", "UK", "Canada", "Australia"])
            form_subscribe = st.checkbox("Subscribe to newsletter")
            
            submitted = st.form_submit_button("Register")
            
            if submitted:
                st.success("✅ Registration successful!")
                st.write(f"Name: {form_name}")
                st.write(f"Email: {form_email}")
                st.write(f"Age: {form_age}")
                st.write(f"Country: {form_country}")
                st.write(f"Subscribed: {form_subscribe}")
    
    with col2:
        st.markdown("### Code:")
        code = """
with st.form("demo_form"):
    st.markdown("**User Registration**")
    
    form_name = st.text_input("Full Name:")
    form_email = st.text_input("Email:")
    form_age = st.number_input("Age:", min_value=18, 
                                max_value=100, value=25)
    form_country = st.selectbox("Country:", 
                                ["USA", "UK", "Canada"])
    form_subscribe = st.checkbox("Subscribe to newsletter")
    
    submitted = st.form_submit_button("Register")
    
    if submitted:
        st.success("✅ Registration successful!")
        st.write(f"Name: {form_name}")
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** Forms prevent re-runs on each input change, improving performance for complex apps.")

# Step 10: Complete Example
with tabs[9]:
    st.header("Step 10: Complete Layout Example")
    st.markdown("Combine everything you've learned into a comprehensive example.")
    
    st.markdown("### Interactive Dashboard Demo")
    
    # Sidebar configuration
    with st.sidebar:
        st.markdown("### Dashboard Settings")
        chart_type = st.selectbox("Chart Type:", ["Line", "Bar", "Area"])
        data_points = st.slider("Data Points:", 10, 100, 30)
        show_stats = st.checkbox("Show Statistics", value=True)
    
    # Main content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Users", "1,234", "+123")
    with col2:
        st.metric("Revenue", "$45.6K", "+$5.2K")
    with col3:
        st.metric("Conversion", "3.2%", "+0.5%")
    
    # Generate sample data
    sample_data = pd.DataFrame(
        np.random.randn(data_points, 3),
        columns=['Series A', 'Series B', 'Series C']
    )
    
    # Display chart based on selection
    st.markdown(f"### {chart_type} Chart")
    if chart_type == "Line":
        st.line_chart(sample_data)
    elif chart_type == "Bar":
        st.bar_chart(sample_data)
    else:
        st.area_chart(sample_data)
    
    # Statistics in expander
    if show_stats:
        with st.expander("📊 Statistical Summary", expanded=True):
            st.dataframe(sample_data.describe())
    
    # Tabs for additional info
    detail_tabs = st.tabs(["📈 Trends", "📋 Raw Data", "⚙️ Export"])
    
    with detail_tabs[0]:
        st.markdown("**Trend Analysis**")
        st.write("Analyzing data trends over time...")
        st.line_chart(sample_data.cumsum())
    
    with detail_tabs[1]:
        st.markdown("**Raw Data Table**")
        st.dataframe(sample_data, use_container_width=True)
    
    with detail_tabs[2]:
        st.markdown("**Export Options**")
        csv = sample_data.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="dashboard_data.csv",
            mime="text/csv"
        )
    
    st.markdown("---")
    st.markdown("### Complete Code:")
    code = """
import streamlit as st
import pandas as pd
import numpy as np

# Sidebar
with st.sidebar:
    st.markdown("### Dashboard Settings")
    chart_type = st.selectbox("Chart Type:", ["Line", "Bar", "Area"])
    data_points = st.slider("Data Points:", 10, 100, 30)
    show_stats = st.checkbox("Show Statistics", value=True)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", "1,234", "+123")
col2.metric("Revenue", "$45.6K", "+$5.2K")
col3.metric("Conversion", "3.2%", "+0.5%")

# Generate data
sample_data = pd.DataFrame(
    np.random.randn(data_points, 3),
    columns=['Series A', 'Series B', 'Series C']
)

# Display chart
if chart_type == "Line":
    st.line_chart(sample_data)
elif chart_type == "Bar":
    st.bar_chart(sample_data)
else:
    st.area_chart(sample_data)

# Statistics
if show_stats:
    with st.expander("📊 Statistical Summary", expanded=True):
        st.dataframe(sample_data.describe())

# Tabs for details
tabs = st.tabs(["📈 Trends", "📋 Raw Data", "⚙️ Export"])
with tabs[0]:
    st.line_chart(sample_data.cumsum())
with tabs[1]:
    st.dataframe(sample_data)
with tabs[2]:
    csv = sample_data.to_csv(index=False)
    st.download_button("Download CSV", csv, "data.csv", "text/csv")
"""
    st.code(code, language="python")
    
    st.success("🎉 **Congratulations!** You've mastered Streamlit elements and layouts!")

# Summary at the bottom
st.markdown("---")
st.markdown("## 📝 Summary")

summary_cols = st.columns(2)

with summary_cols[0]:
    st.markdown("""
    ### What You Learned:
    1. ✅ Display text with various formatting options
    2. ✅ Show data using dataframes, tables, and metrics
    3. ✅ Create charts and visualizations
    4. ✅ Collect user input with widgets
    5. ✅ Organize content with columns
    """)

with summary_cols[1]:
    st.markdown("""
    ### Advanced Techniques:
    6. ✅ Navigate content with tabs
    7. ✅ Control visibility with expanders
    8. ✅ Use sidebar for settings and navigation
    9. ✅ Group inputs efficiently with forms
    10. ✅ Build complete interactive dashboards
    """)

st.info("💡 **Next Steps:** Try combining these elements in your own Streamlit applications!")
