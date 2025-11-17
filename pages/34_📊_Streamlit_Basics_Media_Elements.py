import streamlit as st
from PIL import Image
import numpy as np

st.header("🎬 Media Elements — Streamlit Basics")
st.markdown("Displaying images, audio, and video in Streamlit.")

# Images
st.subheader("📷 Images")

# Create a sample image using numpy
img_array = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

st.image(img_array, caption="Generated Random Image", width=200)

# Multiple images
st.write("**Multiple Images:**")
col1, col2, col3 = st.columns(3)

with col1:
    img1 = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    st.image(img1, caption="Image 1", use_column_width=True)

with col2:
    img2 = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    st.image(img2, caption="Image 2", use_column_width=True)

with col3:
    img3 = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    st.image(img3, caption="Image 3", use_column_width=True)

# Image from URL
st.subheader("Image from URL")

st.code("""
st.image(
    "https://example.com/image.jpg",
    caption="Image from URL",
    width=400
)
""", language="python")

st.info("💡 Supported formats: JPG, PNG, GIF, SVG, WebP")

# Video
st.subheader("🎥 Video")

st.write("**Video from URL:**")
st.code("""
st.video("https://example.com/video.mp4")

# Or with YouTube
st.video("https://www.youtube.com/watch?v=VIDEO_ID")
""", language="python")

st.info("💡 Supported: MP4, WebM, Ogg, YouTube URLs")

# Audio
st.subheader("🔊 Audio")

st.write("**Audio from file:**")
st.code("""
audio_file = open('audio.mp3', 'rb')
st.audio(audio_file, format='audio/mp3')
""", language="python")

st.info("💡 Supported formats: MP3, WAV, OGG, FLAC")

# Camera input
st.subheader("📸 Camera Input")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture, caption="Captured Image")
    st.success("✅ Picture captured!")

# File uploader for media
st.subheader("📤 Upload Media")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png", "gif"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Display file info
    st.write("**File details:**")
    st.write(f"- Name: {uploaded_file.name}")
    st.write(f"- Size: {uploaded_file.size / 1024:.2f} KB")
    st.write(f"- Type: {uploaded_file.type}")

# Media parameters
st.subheader("⚙️ Image Parameters")

params = {
    "caption": "Text below image",
    "width": "Fixed width in pixels",
    "use_column_width": "Auto-fit to column",
    "clamp": "Clamp values to 0-255",
    "channels": "'RGB' or 'BGR'",
    "output_format": "'JPEG', 'PNG', etc."
}

for param, desc in params.items():
    st.write(f"**{param}**: {desc}")

# Example with all parameters
st.subheader("📋 Complete Example")

example_code = """
import streamlit as st
from PIL import Image
import numpy as np

# Create or load image
img = Image.open('photo.jpg')

# Display with options
st.image(
    img,
    caption='My Photo',
    width=400,
    use_column_width=False,
    clamp=True,
    channels='RGB',
    output_format='JPEG'
)
"""

st.code(example_code, language="python")

# Tips
st.subheader("💡 Media Tips")

st.info("""
- **Images**: Use PIL/numpy arrays or file paths
- **Optimization**: Large images are auto-compressed
- **Responsive**: Use `use_column_width=True` for mobile
- **Camera**: Works only in HTTPS or localhost
- **Formats**: Check browser compatibility for video/audio
""")
