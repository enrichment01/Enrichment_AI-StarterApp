import streamlit as st

st.header("🎛️ Sidebar Widgets — Streamlit Basics")
st.markdown("Using the sidebar for navigation and controls.")

# Sidebar text elements
st.sidebar.title("🎨 Sidebar Demo")
st.sidebar.write("This is the sidebar area")

# Sidebar input widgets
st.sidebar.subheader("Controls")

# Text input
name = st.sidebar.text_input("Your Name", "Guest")
st.write(f"Hello, {name}!")

# Number input
age = st.sidebar.number_input("Age", 0, 100, 25)
st.write(f"Age: {age}")

# Slider
temperature = st.sidebar.slider("Temperature (°C)", -10, 40, 20)
st.metric("Current Temperature", f"{temperature}°C")

# Select box
theme = st.sidebar.selectbox(
    "Theme",
    ["Light", "Dark", "Auto"]
)
st.write(f"Selected theme: {theme}")

# Radio buttons
st.sidebar.subheader("Preferences")
view_mode = st.sidebar.radio(
    "View Mode",
    ["Compact", "Detailed", "Grid"]
)
st.write(f"View mode: {view_mode}")

# Checkboxes
st.sidebar.subheader("Features")
show_chart = st.sidebar.checkbox("Show Chart", value=True)
show_table = st.sidebar.checkbox("Show Table", value=True)
show_metrics = st.sidebar.checkbox("Show Metrics", value=False)

# Display based on checkboxes
if show_chart:
    st.subheader("📈 Chart")
    import numpy as np
    import pandas as pd
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

if show_table:
    st.subheader("📊 Data Table")
    table_data = pd.DataFrame({
        'Column 1': [1, 2, 3, 4],
        'Column 2': [10, 20, 30, 40]
    })
    st.dataframe(table_data)

if show_metrics:
    st.subheader("📊 Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "24°C", "1.2°C")
    col2.metric("Humidity", "65%", "-3%")
    col3.metric("Pressure", "1013 hPa", "2 hPa")

# Multi-select
st.sidebar.subheader("Filters")
categories = st.sidebar.multiselect(
    "Select Categories",
    ["Technology", "Science", "Arts", "Sports"],
    default=["Technology"]
)
st.write(f"Selected categories: {', '.join(categories)}")

# Date and time
st.sidebar.subheader("Date & Time")
selected_date = st.sidebar.date_input("Select Date")
selected_time = st.sidebar.time_input("Select Time")

st.write(f"Date: {selected_date}")
st.write(f"Time: {selected_time}")

# Buttons
st.sidebar.subheader("Actions")
if st.sidebar.button("🔄 Refresh"):
    st.sidebar.success("Refreshed!")

if st.sidebar.button("💾 Save"):
    st.sidebar.success("Saved!")

if st.sidebar.button("🗑️ Clear"):
    st.sidebar.warning("Cleared!")

# Download button
st.sidebar.subheader("Export")
st.sidebar.download_button(
    label="📥 Download Data",
    data="Sample data content",
    file_name="data.txt",
    mime="text/plain"
)

# Tips
st.subheader("💡 Sidebar Tips")

st.info("""
- **Navigation**: Perfect for app-wide controls
- **Persistent**: Stays visible while scrolling main content
- **Space-saving**: Keeps main area clean
- **Organization**: Group related controls together
- **State**: Sidebar state persists across pages
""")

