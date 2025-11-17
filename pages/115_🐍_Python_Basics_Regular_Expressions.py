import streamlit as st
import re

st.header("🔍 Regular Expressions — Python Basics")
st.markdown("Pattern matching and text manipulation with regex.")

# Basic pattern matching
st.subheader("Basic Pattern Matching")

text = "The quick brown fox jumps over the lazy dog"

# Search for pattern
if re.search(r"fox", text):
    st.write("✅ Found 'fox' in text")

# Find all matches
words = re.findall(r"\w+", text)
st.write("**All words:**", words)

# Match at beginning
if re.match(r"The", text):
    st.write("✅ Text starts with 'The'")

# Common patterns
st.subheader("Common Regex Patterns")

patterns = {
    r"\d": "Any digit (0-9)",
    r"\w": "Any word character (a-z, A-Z, 0-9, _)",
    r"\s": "Any whitespace",
    r".": "Any character except newline",
    r"^": "Start of string",
    r"$": "End of string",
    r"*": "0 or more repetitions",
    r"+": "1 or more repetitions",
    r"?": "0 or 1 repetition"
}

for pattern, desc in patterns.items():
    st.write(f"**`{pattern}`**: {desc}")

# Email validation
st.subheader("Email Validation Example")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

emails = [
    "user@example.com",
    "invalid.email",
    "test@domain.co.uk",
    "bad@email"
]

for email in emails:
    if re.match(email_pattern, email):
        st.write(f"✅ Valid: {email}")
    else:
        st.write(f"❌ Invalid: {email}")

# Phone number extraction
st.subheader("Phone Number Extraction")

text_with_phones = """
Contact us at 123-456-7890 or 
(555) 123-4567 for more info.
Alternative: 555.987.6543
"""

phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_pattern, text_with_phones)

st.write("**Found phone numbers:**")
for phone in phones:
    st.write(f"- {phone}")

# Text substitution
st.subheader("Text Substitution")

original = "I love cats. Cats are great. Cats are cute."
replaced = re.sub(r'cats', 'dogs', original, flags=re.IGNORECASE)

st.write("**Original:**", original)
st.write("**Replaced:**", replaced)

# Splitting text
st.subheader("Splitting with Regex")

data = "apple,banana;cherry|date:elderberry"
fruits = re.split(r'[,;|:]', data)

st.write("**Split result:**", fruits)

# Groups and capturing
st.subheader("Capturing Groups")

log_entry = "2024-01-15 14:30:25 ERROR User login failed"
pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)'

match = re.match(pattern, log_entry)
if match:
    st.write("**Date:**", match.group(1))
    st.write("**Time:**", match.group(2))
    st.write("**Level:**", match.group(3))
    st.write("**Message:**", match.group(4))

# Practical example: URL extraction
st.subheader("URL Extraction")

text_with_urls = """
Visit https://www.example.com for more info.
Also check http://test.org and www.sample.net
"""

url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, text_with_urls)

st.write("**Extracted URLs:**")
for url in urls:
    st.write(f"- {url}")

