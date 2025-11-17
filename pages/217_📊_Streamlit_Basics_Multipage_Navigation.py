import streamlit as st

st.header("🗺️ Multipage Navigation — Streamlit Basics")
st.markdown("Building and navigating multipage Streamlit applications.")

# Overview
st.subheader("📚 Multipage Apps Overview")

st.write("""
Streamlit automatically creates a multipage app when you have a `pages/` directory 
with Python files. The sidebar navigation is generated automatically.
""")

# File structure
st.subheader("📁 File Structure")

file_structure = """
my_app/
├── app.py                    # Main page (Home)
└── pages/
    ├── 1_📊_Page_One.py     # First page
    ├── 2_🎯_Page_Two.py     # Second page
    └── 3_⚙️_Settings.py      # Third page
"""

st.code(file_structure, language="text")

# Naming convention
st.subheader("📝 File Naming Convention")

naming = {
    "Format": "`{number}_{emoji}_{Title}.py`",
    "Number": "Optional, controls order (01, 02, 1, 2, etc.)",
    "Emoji": "Optional, shows in sidebar",
    "Title": "Converted to page title (underscores → spaces)"
}

for key, value in naming.items():
    st.write(f"**{key}**: {value}")

# Examples
st.subheader("Examples")

examples = """
# These files create pages in this order:
01_Introduction.py       → "Introduction"
02_📊_Data_Analysis.py   → "📊 Data Analysis"
03_🎯_Results.py         → "🎯 Results"
Settings.py              → "Settings" (no number, appears last)
"""

st.code(examples)

# Navigation
st.subheader("🧭 Navigation Methods")

st.write("**Method 1: Sidebar (Automatic)**")
st.code("""
# Navigation is automatic in sidebar
# Users click page names to navigate
""", language="python")

st.write("**Method 2: st.page_link (Manual)**")
st.code("""
# Create custom navigation buttons
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/1_Data.py", label="Data", icon="📊")
st.page_link("pages/2_Settings.py", label="Settings", icon="⚙️")
""", language="python")

# Page links demo
st.subheader("🔗 Custom Page Links")

st.write("**Navigation with page_link:**")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("app.py", label="🏠 Home", use_container_width=True)

with col2:
    st.page_link(
        "pages/200_📊_Streamlit_Basics_Text_Elements.py", 
        label="📝 Text Elements",
        use_container_width=True
    )

with col3:
    st.page_link(
        "pages/206_📊_Streamlit_Basics_Charts.py",
        label="📈 Charts",
        use_container_width=True
    )

# External links
st.subheader("🌐 External Links")

st.page_link("https://docs.streamlit.io", label="📚 Streamlit Docs", icon="🌐")
st.page_link("https://github.com/streamlit/streamlit", label="💻 GitHub Repo", icon="🌐")

# Current page info
st.subheader("📍 Current Page Information")

# Get current page from query params or session state
current_page = st.session_state.get('page', 'Unknown')
st.write(f"**Current page**: {current_page}")

# Page configuration
st.subheader("⚙️ Page Configuration")

config_example = """
import streamlit as st

# Set page config (must be first Streamlit command)
st.set_page_config(
    page_title="My App",
    page_icon="🎯",
    layout="wide",           # or "centered"
    initial_sidebar_state="expanded"  # or "collapsed"
)
"""

st.code(config_example, language="python")

# Shared state across pages
st.subheader("🔄 Sharing State Between Pages")

shared_state = """
# Use st.session_state to share data
# Page 1
st.session_state.user_name = "Alice"
st.session_state.score = 100

# Page 2 (can access the same data)
name = st.session_state.get('user_name', 'Guest')
score = st.session_state.get('score', 0)
st.write(f"Welcome {name}, Score: {score}")
"""

st.code(shared_state, language="python")

# Sidebar customization
st.subheader("🎨 Sidebar Customization")

sidebar_example = """
# Add content to sidebar on any page
st.sidebar.title("My App")
st.sidebar.write("Welcome!")

# Add widgets
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Add separator
st.sidebar.divider()

# Add info
st.sidebar.info("Version 1.0.0")
"""

st.code(sidebar_example, language="python")

# Best practices
st.subheader("💡 Best Practices")

practices = """
1. **Logical organization**: Group related pages
2. **Clear naming**: Use descriptive page names
3. **Consistent style**: Keep UI consistent across pages
4. **Navigation hints**: Guide users where to go next
5. **State management**: Use session_state for data sharing
6. **Page config**: Set once in main app.py
7. **Error handling**: Handle missing session_state keys
8. **Loading states**: Show spinners for slow operations
"""

st.code(practices)

# Common patterns
st.subheader("📋 Common Multipage Patterns")

patterns = {
    "Dashboard": "Main page with overview, detail pages for each section",
    "Wizard/Flow": "Sequential pages guiding through a process",
    "Admin Panel": "Different pages for different admin functions",
    "Documentation": "Main docs page with separate pages per topic",
    "Portfolio": "Project showcase with page per project"
}

for pattern, description in patterns.items():
    st.write(f"**{pattern}**: {description}")

# Tips
st.subheader("⚡ Tips")

st.info("""
- **Hot reload**: Streamlit auto-reloads when you edit pages
- **URL routing**: Each page gets its own URL
- **Bookmarking**: Users can bookmark specific pages
- **Hide pages**: Start filename with underscore to hide
- **Order**: Number prefixes control page order in sidebar
- **Icons**: Emojis in filename show in sidebar navigation
""")

# Example app structure
st.subheader("📦 Complete Example")

complete_example = """
# File: app.py (Home/Main page)
import streamlit as st

st.set_page_config(page_title="My App", page_icon="🏠")

st.title("Welcome to My App")
st.write("Use the sidebar to navigate")

# File: pages/1_📊_Data.py
import streamlit as st

st.title("📊 Data Analysis")
st.write("Analyze your data here")

# File: pages/2_⚙️_Settings.py
import streamlit as st

st.title("⚙️ Settings")
st.write("Configure your preferences")
"""

st.code(complete_example, language="python")
