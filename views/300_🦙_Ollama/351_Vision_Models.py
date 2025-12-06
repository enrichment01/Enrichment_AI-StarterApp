import streamlit as st

st.header("👁️ Vision Models — Ollama Basics")
st.markdown("Working with multimodal models that understand images and text.")

# Overview
st.subheader("What are Vision Models?")

st.write("""
Vision models (multimodal models) can process both images and text, enabling:
- Image description and analysis
- Visual question answering
- Document understanding
- OCR and text extraction
- Image-based reasoning
""")

# Available vision models
st.subheader("📚 Vision Models in Ollama")

vision_models = {
    "llava": "7B vision-language model (most popular)",
    "llava:13b": "13B version (higher quality)",
    "llava:34b": "34B version (best quality)",
    "bakllava": "Alternative vision model",
    "moondream": "Lightweight vision model (1.8B)"
}

for model, description in vision_models.items():
    st.write(f"**{model}**: {description}")

st.info("💡 Pull a vision model: `ollama pull llava`")

# Basic usage
st.subheader("🚀 Basic Vision API Usage")

basic_code = """
import ollama

# Analyze an image
response = ollama.chat(
    model='llava',
    messages=[
        {
            'role': 'user',
            'content': 'Describe this image in detail.',
            'images': ['image.jpg']  # Path to image file
        }
    ]
)

print(response['message']['content'])

# Output: 
# "The image shows a sunset over a beach with golden 
# sand and waves gently rolling onto the shore..."
"""

st.code(basic_code, language="python")

# Image formats
st.subheader("🖼️ Supported Image Formats")

st.write("**Input Methods:**")

image_formats = """
# Method 1: File path
messages = [{
    'role': 'user',
    'content': 'What is in this image?',
    'images': ['photo.jpg']
}]

# Method 2: URL (must be accessible)
messages = [{
    'role': 'user',
    'content': 'Describe this image.',
    'images': ['https://example.com/image.jpg']
}]

# Method 3: Base64 encoded
import base64

with open('image.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode()

messages = [{
    'role': 'user',
    'content': 'What do you see?',
    'images': [image_data]
}]

# Method 4: Multiple images
messages = [{
    'role': 'user',
    'content': 'Compare these two images.',
    'images': ['image1.jpg', 'image2.jpg']
}]
"""

st.code(image_formats, language="python")

# Common use cases
st.subheader("💼 Common Use Cases")

st.write("**1. Image Description**")
description_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': 'Describe this image in detail.',
        'images': ['photo.jpg']
    }]
)
"""
st.code(description_code, language="python")

st.write("**2. Visual Question Answering**")
vqa_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': 'What color is the car in this image?',
        'images': ['street.jpg']
    }]
)
"""
st.code(vqa_code, language="python")

st.write("**3. Object Detection**")
detection_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': 'List all objects you can identify in this image.',
        'images': ['room.jpg']
    }]
)

# Response might be:
# "I can see: a desk, laptop, lamp, chair, bookshelf, 
# window, and a plant."
"""
st.code(detection_code, language="python")

st.write("**4. Text Extraction (OCR)**")
ocr_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': 'Extract all text from this image.',
        'images': ['document.jpg']
    }]
)
"""
st.code(ocr_code, language="python")

# Multi-turn conversation
st.subheader("💬 Multi-turn with Images")

multimodal_conversation = """
import ollama

# Initialize conversation
messages = []

# Turn 1: Analyze first image
messages.append({
    'role': 'user',
    'content': 'What is the main subject of this image?',
    'images': ['photo1.jpg']
})

response = ollama.chat(model='llava', messages=messages)
messages.append(response['message'])

print("AI:", response['message']['content'])

# Turn 2: Follow-up question (no new image)
messages.append({
    'role': 'user',
    'content': 'What colors are dominant?'
})

response = ollama.chat(model='llava', messages=messages)
messages.append(response['message'])

print("AI:", response['message']['content'])

# Turn 3: Analyze another image
messages.append({
    'role': 'user',
    'content': 'How does this image compare to the first one?',
    'images': ['photo2.jpg']
})

response = ollama.chat(model='llava', messages=messages)
print("AI:", response['message']['content'])
"""

st.code(multimodal_conversation, language="python")

# Streamlit integration
st.subheader("📱 Streamlit Integration")

streamlit_vision = """
import streamlit as st
import ollama
from PIL import Image
import io

st.title("Vision Model Demo")

# File uploader
uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Question input
    question = st.text_input(
        "Ask about the image:",
        "Describe this image in detail."
    )
    
    if st.button("Analyze"):
        with st.spinner("Analyzing image..."):
            # Save uploaded file temporarily
            with open("temp_image.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Call vision model
            response = ollama.chat(
                model='llava',
                messages=[{
                    'role': 'user',
                    'content': question,
                    'images': ['temp_image.jpg']
                }]
            )
            
            # Display result
            st.success("Analysis complete!")
            st.write(response['message']['content'])
"""

st.code(streamlit_vision, language="python")

# Advanced patterns
st.subheader("🎯 Advanced Patterns")

st.write("**1. Structured Output**")
structured_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': '''
        Analyze this image and respond in JSON format:
        {
            "objects": ["list", "of", "objects"],
            "colors": ["dominant", "colors"],
            "scene_type": "indoor/outdoor/etc",
            "description": "brief description"
        }
        ''',
        'images': ['image.jpg']
    }]
)

import json
data = json.loads(response['message']['content'])
print(data['objects'])
"""
st.code(structured_code, language="python")

st.write("**2. Image Comparison**")
comparison_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': '''
        Compare these two images and tell me:
        1. What's similar?
        2. What's different?
        3. Which is better quality?
        ''',
        'images': ['before.jpg', 'after.jpg']
    }]
)
"""
st.code(comparison_code, language="python")

st.write("**3. Document Understanding**")
document_code = """
response = ollama.chat(
    model='llava',
    messages=[{
        'role': 'user',
        'content': '''
        This is an invoice image. Extract:
        - Invoice number
        - Date
        - Total amount
        - Vendor name
        ''',
        'images': ['invoice.jpg']
    }]
)
"""
st.code(document_code, language="python")

# Image upload demo (simulated)
st.subheader("🎮 Try It Out (Demo)")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    from PIL import Image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    question = st.text_input("Ask about the image:", "Describe what you see.")
    
    if st.button("Analyze Image"):
        st.info("In a real application with Ollama vision model installed, this would analyze the image.")
        st.write("**Simulated Response:**")
        st.success("I can see an uploaded image. The vision model would analyze it and provide detailed information based on your question.")

# Performance tips
st.subheader("⚡ Performance Tips")

st.info("""
**Optimization:**
- Resize large images (max 1024x1024 recommended)
- Use JPEG for photos, PNG for diagrams
- Smaller models (moondream) are faster
- Cache results for identical images

**Quality:**
- Higher resolution = better detail recognition
- Good lighting in images helps
- Clear, focused images work best
- llava:13b or llava:34b for best quality

**Memory:**
- Vision models use more RAM (8-16GB recommended)
- Processing images takes more time
- Unload model when not in use
""")

# Best practices
st.subheader("💡 Best Practices")

best_practices = """
**Prompting:**
- Be specific about what you want to know
- Ask one question at a time for clarity
- Provide context if needed
- Request structured output when appropriate

**Image Preparation:**
- Ensure images are clear and well-lit
- Crop to relevant area if possible
- Use appropriate resolution (not too small/large)
- Avoid heavily compressed images

**Error Handling:**
- Check if image file exists
- Validate image format
- Handle model loading errors
- Provide fallback for failures

**Use Cases:**
- Product catalog descriptions
- Content moderation
- Accessibility (image descriptions)
- Document processing
- Quality control
"""

st.code(best_practices)

# Limitations
st.subheader("⚠️ Current Limitations")

st.warning("""
**Be aware that vision models:**
- May hallucinate (describe things not in image)
- Struggle with fine details or small text
- Have biases from training data
- May misidentify objects
- Cannot count perfectly
- Limited spatial reasoning

Always validate critical information!
""")

# Complete example
st.subheader("📋 Complete Example Application")

complete_app = """
import ollama
import streamlit as st
from PIL import Image
import json

class VisionAnalyzer:
    def __init__(self, model='llava'):
        self.model = model
    
    def analyze_image(self, image_path, question):
        '''Analyze image with custom question'''
        response = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': question,
                'images': [image_path]
            }]
        )
        return response['message']['content']
    
    def extract_info(self, image_path):
        '''Extract structured information'''
        prompt = '''
        Analyze this image and provide:
        1. Main subject
        2. Setting/location type
        3. Notable objects
        4. Colors
        5. Overall mood
        
        Format as JSON.
        '''
        
        response = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }]
        )
        
        return response['message']['content']

# Streamlit UI
st.title("Image Analysis Tool")

analyzer = VisionAnalyzer()

uploaded = st.file_uploader("Upload image", type=['jpg', 'png'])

if uploaded:
    # Save and display image
    image = Image.open(uploaded)
    st.image(image, width=400)
    
    # Analysis options
    analysis_type = st.radio(
        "Analysis type:",
        ["Quick Description", "Detailed Analysis", "Custom Question"]
    )
    
    if analysis_type == "Custom Question":
        question = st.text_input("Your question:")
    elif analysis_type == "Quick Description":
        question = "Describe this image briefly."
    else:
        question = "Provide a detailed analysis of this image."
    
    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            # Save temp file
            temp_path = "temp.jpg"
            image.save(temp_path)
            
            # Analyze
            result = analyzer.analyze_image(temp_path, question)
            
            st.success("Analysis complete!")
            st.write(result)
"""

st.code(complete_app, language="python")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- **Start with llava**: Best balance of speed and quality
- **Test prompts**: Vision models are sensitive to wording
- **Batch processing**: Process multiple images efficiently
- **Validation**: Always verify important extractions
- **Feedback loop**: Improve prompts based on results
- **Fallbacks**: Have backup strategy for failures
""")
