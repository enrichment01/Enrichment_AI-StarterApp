import streamlit as st

st.header("💾 Session State — Streamlit Basics")
st.markdown("Managing state across reruns in Streamlit applications.")

# Initialize session state
if "counter" not in st.session_state:
    st.session_state.counter = 0

if "messages" not in st.session_state:
    st.session_state.messages = []

# Counter example
st.subheader("Counter Example")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ Increment"):
        st.session_state.counter += 1

with col2:
    if st.button("➖ Decrement"):
        st.session_state.counter -= 1

with col3:
    if st.button("🔄 Reset"):
        st.session_state.counter = 0

st.metric("Current Count", st.session_state.counter)

# Message board example
st.subheader("Message Board")

message = st.text_input("Enter a message:")

if st.button("📝 Add Message"):
    if message:
        st.session_state.messages.append(message)
        st.success("Message added!")

if st.button("🗑️ Clear All Messages"):
    st.session_state.messages = []

if st.session_state.messages:
    st.write("**Messages:**")
    for i, msg in enumerate(st.session_state.messages, 1):
        st.write(f"{i}. {msg}")
else:
    st.info("No messages yet")

# Form state example
st.subheader("Form with State")

if "form_data" not in st.session_state:
    st.session_state.form_data = {"name": "", "age": 0}

name_input = st.text_input("Name", value=st.session_state.form_data["name"])
age_input = st.number_input("Age", value=st.session_state.form_data["age"], min_value=0, max_value=120)

if st.button("💾 Save Form"):
    st.session_state.form_data = {
        "name": name_input,
        "age": age_input
    }
    st.success("Form data saved!")

st.write("**Saved data:**", st.session_state.form_data)

# Callback example
st.subheader("Callbacks with Session State")

def update_name():
    st.session_state.display_name = st.session_state.name_input.upper()

if "display_name" not in st.session_state:
    st.session_state.display_name = ""

st.text_input(
    "Enter your name:",
    key="name_input",
    on_change=update_name
)

if st.session_state.display_name:
    st.success(f"Hello, {st.session_state.display_name}!")

# Tips
st.subheader("💡 Session State Best Practices")

st.info("""
- **Initialize values**: Always check if key exists before use
- **Use keys**: Set `key` parameter for widgets to auto-sync
- **Callbacks**: Use `on_change` for immediate reactions
- **Clear state**: Reset when needed for fresh start
- **Persistence**: State is per-user session only
""")

# Debug view
with st.expander("🔍 View Session State"):
    st.write(st.session_state)

