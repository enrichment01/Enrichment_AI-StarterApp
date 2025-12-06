import streamlit as st

st.header("📝 Forms — Streamlit Basics")
st.markdown("Creating forms with batch submission in Streamlit.")

# Basic form
st.subheader("Basic Form Example")

with st.form("basic_form"):
    st.write("**User Registration**")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.success("✅ Form submitted!")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")

# Form with various widgets
st.subheader("Form with Multiple Widgets")

with st.form("detailed_form"):
    st.write("**Survey Form**")
    
    # Text inputs
    name = st.text_input("Full Name")
    
    # Select box
    department = st.selectbox(
        "Department",
        ["Engineering", "Marketing", "Sales", "HR"]
    )
    
    # Radio buttons
    experience = st.radio(
        "Experience Level",
        ["Junior", "Mid-level", "Senior"]
    )
    
    # Checkboxes
    st.write("**Skills:**")
    python = st.checkbox("Python")
    javascript = st.checkbox("JavaScript")
    sql = st.checkbox("SQL")
    
    # Slider
    satisfaction = st.slider("Satisfaction", 1, 10, 5)
    
    # Text area
    comments = st.text_area("Comments")
    
    # Submit buttons
    col1, col2 = st.columns(2)
    with col1:
        submit = st.form_submit_button("Submit Survey")
    with col2:
        clear = st.form_submit_button("Clear Form")
    
    if submit:
        st.success("✅ Survey submitted!")
        skills = []
        if python:
            skills.append("Python")
        if javascript:
            skills.append("JavaScript")
        if sql:
            skills.append("SQL")
        
        st.write("**Results:**")
        st.write(f"- Name: {name}")
        st.write(f"- Department: {department}")
        st.write(f"- Experience: {experience}")
        st.write(f"- Skills: {', '.join(skills) if skills else 'None selected'}")
        st.write(f"- Satisfaction: {satisfaction}/10")
        st.write(f"- Comments: {comments}")

# Form with validation
st.subheader("Form with Validation")

with st.form("validation_form"):
    st.write("**Login Form**")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    remember = st.checkbox("Remember me")
    
    login = st.form_submit_button("Login")
    
    if login:
        if not username:
            st.error("❌ Username is required")
        elif not password:
            st.error("❌ Password is required")
        elif len(password) < 6:
            st.error("❌ Password must be at least 6 characters")
        else:
            st.success(f"✅ Welcome, {username}!")
            if remember:
                st.info("Session will be remembered")

# Multiple forms
st.subheader("Multiple Forms on Same Page")

col1, col2 = st.columns(2)

with col1:
    with st.form("form1"):
        st.write("**Quick Poll**")
        answer = st.radio("Do you like Streamlit?", ["Yes", "No"])
        if st.form_submit_button("Vote"):
            st.write(f"You voted: {answer}")

with col2:
    with st.form("form2"):
        st.write("**Feedback**")
        rating = st.slider("Rate us", 1, 5, 3)
        if st.form_submit_button("Send"):
            st.write(f"Rating: {rating}/5 ⭐")

# Tips
st.subheader("💡 Form Tips")

st.info("""
- **Batch submission**: Forms prevent re-runs until submit
- **Unique keys**: Each form needs unique key/name
- **Validation**: Check inputs before processing
- **Clear button**: Use second submit button for clearing
- **Multiple forms**: Can have many forms on one page
""")

