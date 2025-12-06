import streamlit as st

from lib.helper_streamlit import show_code, show_snippet


st.header("✂️ String Manipulation — Python Basics")
st.markdown("Common string operations and methods in Python.")

# --- CODE START
# Basic string operations
namespace = {
    "text": "  Hello, Python!  ",
    "message": "Python is awesome",
    "name": "Alice",
    "age": 30,
    "words": ["Python", "is", "fun"],
    "sentence": " ".join(["Python", "is", "fun"]),
}

# --- CODE END

# =================================================================================================
# show_code(__file__)

show_snippet(
    """
st.write("Original:", repr(text))
st.write("Stripped:", text.strip())
""",
    namespace=namespace,
)


show_snippet(
    """
st.write("Lower case:", text.lower())
st.write("Upper case:", text.upper())
st.write("Title case:", text.title())
""",
    namespace=namespace,
)

show_snippet(
    """
st.write("message:", message)
st.write("Replace:", message.replace("awesome", "amazing"))
""",
    namespace=namespace,
)

show_snippet("""st.write("Split:", message.split())""", namespace=namespace)

show_snippet(
    """
st.write("Starts with 'Python':", message.startswith("Python"))
st.write("Contains 'is':", "is" in message)
""",
    namespace=namespace,
)


show_snippet(
    """
st.write("First 4 chars:", text[:4])
st.write("Last 4 chars:", text[-4:])
""",
    namespace=namespace,
)


show_snippet(
    """
st.write("Every 2nd char:", text[::2])
st.write("Reversed:", text[::-1])
""",
    namespace=namespace,
)

show_snippet(
    """
st.write("f-string:", f"Name: {name}, Age: {age}")
""",
    namespace=namespace,
)

show_snippet(
    """
st.write("format():", "Name: {}, Age: {}".format(name, age))
""",
    namespace=namespace,
)

show_snippet(
    """
st.write("%-formatting:", "Name: %s, Age: %d" % (name, age))
""",
    namespace=namespace,
)

show_snippet(
    """
sentence = " ".join(["Python", "is", "fun"])
st.write("Joined:", sentence)
""",
    namespace=namespace,
)
