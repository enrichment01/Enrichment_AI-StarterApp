import streamlit as st

st.set_page_config(page_title="10 Steps: Ollama Mini Apps", page_icon="🚀", layout="wide")

st.title("🚀 10 Steps to Build Ollama Mini Apps")
st.markdown("Learn to create chat, text generation, and text analysis applications with Ollama.")

# Create tabs for each step
tabs = st.tabs([
    "Chat Basics",
    "Message History",
    "Stream Chat",
    "Text Generator",
    "Creative Writing",
    "Text Analyzer",
    "Summarization",
    "Sentiment",
    "Key Points",
    "Full Apps"
])

# Step 1: Chat Interface Basics
with tabs[0]:
    st.header("Step 1: Chat Interface Basics")
    st.markdown("Build a simple chat interface foundation.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Simple Chat:")
        
        # Initialize chat history
        if 'step1_messages' not in st.session_state:
            st.session_state.step1_messages = []
        
        # Display messages
        chat_container = st.container()
        with chat_container:
            for msg in st.session_state.step1_messages:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])
        
        # User input
        user_input = st.chat_input("Type your message...", key="step1_input")
        
        if user_input:
            # Add user message
            st.session_state.step1_messages.append({
                "role": "user",
                "content": user_input
            })
            
            # Generate response
            try:
                import ollama
                response = ollama.chat(
                    model='llama2',
                    messages=st.session_state.step1_messages
                )
                
                # Add assistant message
                st.session_state.step1_messages.append({
                    "role": "assistant",
                    "content": response['message']['content']
                })
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        
        if st.button("Clear Chat", key="step1_clear"):
            st.session_state.step1_messages = []
            st.rerun()
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Generate AI response
    response = ollama.chat(
        model='llama2',
        messages=st.session_state.messages
    )
    
    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response['message']['content']
    })
    
    st.rerun()
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Use st.chat_message() and st.chat_input() for modern chat UI.")

# Step 2: Message History Management
with tabs[1]:
    st.header("Step 2: Message History Management")
    st.markdown("Manage conversation history effectively.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Chat with History Limit:")
        
        if 'step2_messages' not in st.session_state:
            st.session_state.step2_messages = []
        
        # Settings
        max_history = st.slider("Max history:", 2, 20, 10, step=2, key="step2_max")
        
        st.markdown(f"**Current messages: {len(st.session_state.step2_messages)}**")
        
        # Display messages
        for i, msg in enumerate(st.session_state.step2_messages):
            with st.chat_message(msg["role"]):
                st.write(f"{msg['content']}")
        
        # Input
        step2_input = st.chat_input("Message...", key="step2_chat")
        
        if step2_input:
            # Add user message
            st.session_state.step2_messages.append({
                "role": "user",
                "content": step2_input
            })
            
            # Trim history if needed
            if len(st.session_state.step2_messages) > max_history:
                # Keep system message if exists, then latest messages
                st.session_state.step2_messages = st.session_state.step2_messages[-max_history:]
            
            try:
                import ollama
                response = ollama.chat(
                    model='llama2',
                    messages=st.session_state.step2_messages
                )
                
                st.session_state.step2_messages.append({
                    "role": "assistant",
                    "content": response['message']['content']
                })
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Initialize
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Settings
max_history = st.slider("Max history:", 2, 20, 10)

# Process input
if user_input := st.chat_input("Message..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Trim history to max_history
    if len(st.session_state.messages) > max_history:
        st.session_state.messages = \\
            st.session_state.messages[-max_history:]
    
    # Get response
    response = ollama.chat(
        model='llama2',
        messages=st.session_state.messages
    )
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response['message']['content']
    })
"""
        st.code(code, language="python")
        
        st.markdown("### Why Limit History?")
        st.info("""
        - ✅ Faster responses
        - ✅ Lower memory usage
        - ✅ Stay within context limits
        - ✅ More focused conversations
        """)
    
    st.success("✅ **Key Point:** Manage history size for performance and context relevance.")

# Step 3: Streaming Chat
with tabs[2]:
    st.header("Step 3: Streaming Chat Responses")
    st.markdown("Display responses in real-time as they're generated.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Streaming Chat:")
        
        if 'step3_messages' not in st.session_state:
            st.session_state.step3_messages = []
        
        # Display existing messages
        for msg in st.session_state.step3_messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        # Input
        step3_input = st.chat_input("Message...", key="step3_chat")
        
        if step3_input:
            # Add and display user message
            st.session_state.step3_messages.append({
                "role": "user",
                "content": step3_input
            })
            
            with st.chat_message("user"):
                st.write(step3_input)
            
            # Stream assistant response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                try:
                    import ollama
                    stream = ollama.chat(
                        model='llama2',
                        messages=st.session_state.step3_messages,
                        stream=True
                    )
                    
                    for chunk in stream:
                        if 'message' in chunk and 'content' in chunk['message']:
                            full_response += chunk['message']['content']
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                    
                    # Save response
                    st.session_state.step3_messages.append({
                        "role": "assistant",
                        "content": full_response
                    })
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Handle new input
if prompt := st.chat_input("Message..."):
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    with st.chat_message("user"):
        st.write(prompt)
    
    # Stream response
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        
        stream = ollama.chat(
            model='llama2',
            messages=st.session_state.messages,
            stream=True
        )
        
        for chunk in stream:
            if 'message' in chunk:
                full_response += chunk['message']['content']
                placeholder.markdown(full_response + "▌")
        
        placeholder.markdown(full_response)
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response
        })
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Streaming provides better UX for longer responses.")

# Step 4: Text Generator Setup
with tabs[3]:
    st.header("Step 4: Text Generator Setup")
    st.markdown("Build a customizable text generation interface.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Text Generator:")
        
        # Generator settings
        gen_model = st.selectbox("Model:", ["llama2", "mistral", "phi"], key="gen_model")
        gen_temp = st.slider("Temperature:", 0.0, 2.0, 0.7, 0.1, key="gen_temp")
        gen_length = st.slider("Max length:", 50, 500, 200, 50, key="gen_length")
        
        # Prompt templates
        template = st.selectbox(
            "Template:",
            ["Custom", "Blog Post", "Email", "Story", "Product Description"],
            key="gen_template"
        )
        
        templates = {
            "Blog Post": "Write a blog post about: ",
            "Email": "Write a professional email about: ",
            "Story": "Write a short story about: ",
            "Product Description": "Write a product description for: "
        }
        
        if template != "Custom":
            prompt_prefix = templates[template]
            user_topic = st.text_input("Topic:", key="gen_topic")
            final_prompt = prompt_prefix + user_topic if user_topic else ""
        else:
            final_prompt = st.text_area("Prompt:", height=100, key="gen_prompt")
        
        if st.button("✨ Generate", key="gen_button", type="primary"):
            if final_prompt:
                with st.spinner(f"Generating with {gen_model}..."):
                    try:
                        import ollama
                        response = ollama.generate(
                            model=gen_model,
                            prompt=final_prompt,
                            options={
                                'temperature': gen_temp,
                                'num_predict': gen_length
                            }
                        )
                        
                        st.markdown("### Generated Text:")
                        st.write(response['response'])
                        
                        # Show stats
                        with st.expander("📊 Generation Stats"):
                            st.write(f"Model: {gen_model}")
                            st.write(f"Temperature: {gen_temp}")
                            st.write(f"Tokens: {response.get('eval_count', 'N/A')}")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter a prompt")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Settings
model = st.selectbox("Model:", ["llama2", "mistral"])
temperature = st.slider("Temperature:", 0.0, 2.0, 0.7)
max_length = st.slider("Max length:", 50, 500, 200)

# Template selection
template = st.selectbox("Template:", 
    ["Custom", "Blog Post", "Email", "Story"])

templates = {
    "Blog Post": "Write a blog post about: ",
    "Email": "Write a professional email about: ",
    "Story": "Write a short story about: "
}

if template != "Custom":
    topic = st.text_input("Topic:")
    prompt = templates[template] + topic
else:
    prompt = st.text_area("Prompt:")

# Generate
if st.button("Generate"):
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={
            'temperature': temperature,
            'num_predict': max_length
        }
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
    
    st.info("💡 **Tip:** Templates help users get started quickly with common use cases.")

# Step 5: Creative Writing Features
with tabs[4]:
    st.header("Step 5: Creative Writing Features")
    st.markdown("Add advanced features for creative text generation.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Creative Writer:")
        
        # Writing type
        writing_type = st.radio(
            "Writing Type:",
            ["Story", "Poem", "Dialogue", "Scene Description"],
            key="creative_type"
        )
        
        # Style
        style = st.selectbox(
            "Style:",
            ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror", "Comedy"],
            key="creative_style"
        )
        
        # Tone
        tone = st.select_slider(
            "Tone:",
            ["Very Serious", "Serious", "Neutral", "Light", "Very Light"],
            value="Neutral",
            key="creative_tone"
        )
        
        # Topic
        topic = st.text_input("Topic/Theme:", "A mysterious discovery", key="creative_topic")
        
        if st.button("✍️ Create", key="creative_button"):
            # Build prompt
            prompt = f"Write a {writing_type.lower()} in {style.lower()} style with a {tone.lower()} tone about: {topic}"
            
            st.markdown("### Generated Content:")
            placeholder = st.empty()
            full_text = ""
            
            try:
                import ollama
                stream = ollama.generate(
                    model='llama2',
                    prompt=prompt,
                    options={'temperature': 0.9},  # High creativity
                    stream=True
                )
                
                for chunk in stream:
                    if 'response' in chunk:
                        full_text += chunk['response']
                        placeholder.markdown(full_text + "▌")
                
                placeholder.markdown(full_text)
                st.success("✅ Creation complete!")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Creative settings
writing_type = st.radio("Type:", 
    ["Story", "Poem", "Dialogue"])

style = st.selectbox("Style:", 
    ["Fantasy", "Sci-Fi", "Mystery"])

tone = st.select_slider("Tone:", 
    ["Serious", "Neutral", "Light"])

topic = st.text_input("Topic:", "A mysterious discovery")

if st.button("Create"):
    # Build creative prompt
    prompt = f\"\"\"Write a {writing_type.lower()} 
    in {style.lower()} style 
    with a {tone.lower()} tone 
    about: {topic}\"\"\"
    
    # Stream with high creativity
    full_text = ""
    placeholder = st.empty()
    
    stream = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.9},
        stream=True
    )
    
    for chunk in stream:
        full_text += chunk['response']
        placeholder.markdown(full_text + "▌")
    
    placeholder.markdown(full_text)
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Combine multiple parameters for fine-tuned creative control.")

# Step 6: Text Analyzer Setup
with tabs[5]:
    st.header("Step 6: Text Analyzer Setup")
    st.markdown("Build a text analysis tool foundation.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Text Analyzer:")
        
        # Input text
        text_to_analyze = st.text_area(
            "Enter text to analyze:",
            "Artificial intelligence is transforming how we work and live. "
            "While it brings many benefits, it also raises important questions "
            "about privacy, ethics, and the future of employment.",
            height=150,
            key="analyzer_text"
        )
        
        # Analysis type
        analysis_type = st.selectbox(
            "Analysis Type:",
            ["Summarize", "Extract Keywords", "Identify Tone", "Count Words"],
            key="analyzer_type"
        )
        
        if st.button("🔍 Analyze", key="analyzer_button"):
            if analysis_type == "Count Words":
                # Simple analysis
                word_count = len(text_to_analyze.split())
                char_count = len(text_to_analyze)
                sentence_count = text_to_analyze.count('.') + text_to_analyze.count('!') + text_to_analyze.count('?')
                
                st.markdown("### Analysis Results:")
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Words", word_count)
                col_b.metric("Characters", char_count)
                col_c.metric("Sentences", sentence_count)
            else:
                # AI-powered analysis
                prompts = {
                    "Summarize": f"Summarize this text in 2-3 sentences:\n\n{text_to_analyze}",
                    "Extract Keywords": f"Extract the main keywords from this text:\n\n{text_to_analyze}",
                    "Identify Tone": f"Identify the tone of this text (e.g., formal, casual, positive, negative):\n\n{text_to_analyze}"
                }
                
                with st.spinner("Analyzing..."):
                    try:
                        import ollama
                        response = ollama.generate(
                            model='llama2',
                            prompt=prompts[analysis_type],
                            options={'temperature': 0.3}  # Low for factual
                        )
                        
                        st.markdown("### Analysis Results:")
                        st.write(response['response'])
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Input
text = st.text_area("Text to analyze:", height=150)

# Analysis options
analysis = st.selectbox("Analysis Type:", 
    ["Summarize", "Keywords", "Tone"])

if st.button("Analyze"):
    # Define prompts
    prompts = {
        "Summarize": f"Summarize: {text}",
        "Keywords": f"Extract keywords: {text}",
        "Tone": f"Identify tone: {text}"
    }
    
    # Analyze with AI
    response = ollama.generate(
        model='llama2',
        prompt=prompts[analysis],
        options={'temperature': 0.3}  # Factual
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Analysis Types:")
        st.info("""
        - **Summarize**: Condense text
        - **Keywords**: Extract main topics
        - **Tone**: Identify sentiment/style
        - **Count**: Basic statistics
        """)
    
    st.success("✅ **Key Point:** Use low temperature (0.2-0.4) for factual analysis tasks.")

# Step 7: Summarization Features
with tabs[6]:
    st.header("Step 7: Advanced Summarization")
    st.markdown("Create flexible summarization with different lengths and styles.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Smart Summarizer:")
        
        text_to_summarize = st.text_area(
            "Text to summarize:",
            "The development of artificial intelligence has accelerated dramatically in recent years. "
            "Machine learning algorithms can now perform tasks that were once thought to require human intelligence, "
            "such as recognizing images, understanding natural language, and making complex decisions. "
            "Deep learning, a subset of machine learning, has been particularly successful, enabling breakthroughs "
            "in areas like computer vision, speech recognition, and natural language processing. "
            "However, these advances also raise important questions about privacy, bias, and the future of work. "
            "As AI systems become more capable, society must grapple with how to ensure they are developed and deployed responsibly.",
            height=200,
            key="summary_text"
        )
        
        # Summarization options
        summary_length = st.select_slider(
            "Summary Length:",
            ["Very Brief", "Brief", "Moderate", "Detailed"],
            value="Brief",
            key="summary_length"
        )
        
        summary_style = st.radio(
            "Style:",
            ["Bullet Points", "Paragraph", "Key Takeaways"],
            key="summary_style"
        )
        
        if st.button("📝 Summarize", key="summary_button"):
            # Build prompt based on options
            length_map = {
                "Very Brief": "in one sentence",
                "Brief": "in 2-3 sentences",
                "Moderate": "in a short paragraph",
                "Detailed": "in a detailed paragraph"
            }
            
            style_map = {
                "Bullet Points": "as bullet points",
                "Paragraph": "as a flowing paragraph",
                "Key Takeaways": "as key takeaways"
            }
            
            prompt = f"Summarize the following text {length_map[summary_length]} {style_map[summary_style]}:\n\n{text_to_summarize}"
            
            with st.spinner("Summarizing..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.3}
                    )
                    
                    st.markdown("### Summary:")
                    st.write(response['response'])
                    
                    # Show original vs summary
                    with st.expander("📊 Compression Stats"):
                        original_words = len(text_to_summarize.split())
                        summary_words = len(response['response'].split())
                        compression = ((original_words - summary_words) / original_words) * 100
                        
                        col_a, col_b, col_c = st.columns(3)
                        col_a.metric("Original", f"{original_words} words")
                        col_b.metric("Summary", f"{summary_words} words")
                        col_c.metric("Compression", f"{compression:.0f}%")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

text = st.text_area("Text:", height=200)

# Options
length = st.select_slider("Length:", 
    ["Very Brief", "Brief", "Moderate", "Detailed"])

style = st.radio("Style:", 
    ["Bullet Points", "Paragraph", "Key Takeaways"])

if st.button("Summarize"):
    # Map options to prompt instructions
    length_map = {
        "Very Brief": "in one sentence",
        "Brief": "in 2-3 sentences",
        "Moderate": "in a short paragraph",
        "Detailed": "in a detailed paragraph"
    }
    
    style_map = {
        "Bullet Points": "as bullet points",
        "Paragraph": "as a flowing paragraph",
        "Key Takeaways": "as key takeaways"
    }
    
    # Build prompt
    prompt = f\"\"\"Summarize the following text 
    {length_map[length]} {style_map[style]}:
    
    {text}\"\"\"
    
    # Generate summary
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** Flexible summarization adapts to user needs.")

# Step 8: Sentiment Analysis
with tabs[7]:
    st.header("Step 8: Sentiment Analysis")
    st.markdown("Analyze emotional tone and sentiment of text.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Sentiment Analyzer:")
        
        sentiment_text = st.text_area(
            "Enter text for sentiment analysis:",
            "I absolutely love this product! It exceeded all my expectations and the customer service was fantastic.",
            height=120,
            key="sentiment_text"
        )
        
        if st.button("😊 Analyze Sentiment", key="sentiment_button"):
            prompt = f"""Analyze the sentiment of this text. 
            Provide:
            1. Overall sentiment (Positive/Negative/Neutral)
            2. Confidence level (High/Medium/Low)
            3. Key emotions detected
            4. Brief explanation
            
            Text: {sentiment_text}"""
            
            with st.spinner("Analyzing sentiment..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.2}
                    )
                    
                    st.markdown("### Sentiment Analysis:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

text = st.text_area("Text for sentiment analysis:")

if st.button("Analyze Sentiment"):
    prompt = f\"\"\"Analyze the sentiment of this text.
    Provide:
    1. Overall sentiment (Positive/Negative/Neutral)
    2. Confidence level (High/Medium/Low)
    3. Key emotions detected
    4. Brief explanation
    
    Text: {text}\"\"\"
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.2}  # Low for accuracy
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Sample Texts:")
        st.info("""
        **Positive**: "Amazing experience! Highly recommend."
        
        **Negative**: "Terrible service, very disappointed."
        
        **Neutral**: "The product works as described."
        
        **Mixed**: "Good quality but poor delivery."
        """)
    
    st.success("✅ **Key Point:** Low temperature ensures consistent sentiment classification.")

# Step 9: Key Points Extraction
with tabs[8]:
    st.header("Step 9: Key Points Extraction")
    st.markdown("Extract main ideas and important information.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Key Points Extractor:")
        
        keypoints_text = st.text_area(
            "Enter text to extract key points:",
            "Climate change is one of the most pressing issues facing our planet. "
            "Rising global temperatures are causing ice caps to melt, sea levels to rise, "
            "and weather patterns to become more extreme. Scientists agree that human activities, "
            "particularly the burning of fossil fuels, are the primary cause. "
            "To address this crisis, we need to transition to renewable energy sources, "
            "improve energy efficiency, and reduce carbon emissions. "
            "Individual actions matter, but systemic change through policy and technology is essential.",
            height=200,
            key="keypoints_text"
        )
        
        num_points = st.slider("Number of key points:", 3, 10, 5, key="num_points")
        
        if st.button("🔑 Extract Key Points", key="keypoints_button"):
            prompt = f"""Extract exactly {num_points} key points from this text.
            Format each point as a bullet point.
            Be concise and focus on the most important information.
            
            Text: {keypoints_text}"""
            
            with st.spinner("Extracting key points..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.2}
                    )
                    
                    st.markdown("### Key Points:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

text = st.text_area("Text:", height=200)

num_points = st.slider("Number of points:", 3, 10, 5)

if st.button("Extract Key Points"):
    prompt = f\"\"\"Extract exactly {num_points} key points 
    from this text. Format as bullet points.
    Be concise and focus on important information.
    
    Text: {text}\"\"\"
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.2}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Use Cases:")
        st.info("""
        - 📄 Meeting notes summarization
        - 📚 Study material extraction
        - 📰 Article main points
        - 📊 Report highlights
        - 📧 Email key actions
        """)
    
    st.success("✅ **Key Point:** Structured prompts ensure consistent output format.")

# Step 10: Complete Mini Apps Integration
with tabs[9]:
    st.header("Step 10: Complete Mini Apps")
    st.markdown("Combine all features into polished applications.")
    
    st.markdown("### Choose a Mini App:")
    
    app_choice = st.selectbox(
        "Select app:",
        ["💬 Chat Bot", "✍️ Text Generator", "🔍 Text Analyzer"],
        key="app_choice"
    )
    
    st.markdown("---")
    
    # Chat Bot
    if app_choice == "💬 Chat Bot":
        st.subheader("Complete Chat Bot")
        
        with st.sidebar:
            st.markdown("### Chat Settings")
            chat_model = st.selectbox("Model:", ["llama2", "mistral", "phi"], key="chat_model_final")
            chat_system = st.text_area(
                "System Message:",
                "You are a helpful and friendly assistant.",
                key="chat_system_final"
            )
            max_msgs = st.slider("Max messages:", 10, 50, 20, key="chat_max_final")
        
        if 'final_chat_messages' not in st.session_state:
            st.session_state.final_chat_messages = []
        
        # Display chat
        for msg in st.session_state.final_chat_messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        # Input
        if final_chat_input := st.chat_input("Type your message...", key="final_chat_input"):
            # Add user message
            st.session_state.final_chat_messages.append({
                "role": "user",
                "content": final_chat_input
            })
            
            # Prepare messages with system
            messages = [{"role": "system", "content": chat_system}] + st.session_state.final_chat_messages[-max_msgs:]
            
            with st.chat_message("user"):
                st.write(final_chat_input)
            
            # Stream response
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                
                try:
                    import ollama
                    stream = ollama.chat(
                        model=chat_model,
                        messages=messages,
                        stream=True
                    )
                    
                    for chunk in stream:
                        if 'message' in chunk and 'content' in chunk['message']:
                            full_response += chunk['message']['content']
                            placeholder.markdown(full_response + "▌")
                    
                    placeholder.markdown(full_response)
                    
                    st.session_state.final_chat_messages.append({
                        "role": "assistant",
                        "content": full_response
                    })
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        
        if st.button("🗑️ Clear Chat", key="final_chat_clear"):
            st.session_state.final_chat_messages = []
            st.rerun()
    
    # Text Generator
    elif app_choice == "✍️ Text Generator":
        st.subheader("Complete Text Generator")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            gen_category = st.selectbox(
                "Category:",
                ["Creative Writing", "Business", "Technical", "Marketing"],
                key="gen_cat_final"
            )
            
            gen_type = st.selectbox(
                "Type:",
                ["Story", "Email", "Blog Post", "Ad Copy", "Code Documentation"],
                key="gen_type_final"
            )
            
            gen_prompt_final = st.text_area("Your prompt:", height=100, key="gen_prompt_final")
            
            gen_temp_final = st.slider("Creativity:", 0.0, 2.0, 0.7, 0.1, key="gen_temp_final")
            
            if st.button("✨ Generate", type="primary", key="gen_final"):
                if gen_prompt_final:
                    with st.spinner("Generating..."):
                        try:
                            import ollama
                            response = ollama.generate(
                                model='llama2',
                                prompt=gen_prompt_final,
                                options={'temperature': gen_temp_final}
                            )
                            
                            st.markdown("### Generated Content:")
                            st.write(response['response'])
                            
                            # Download button
                            st.download_button(
                                "📥 Download",
                                response['response'],
                                "generated_text.txt",
                                "text/plain"
                            )
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        with col2:
            st.markdown("### Tips")
            st.info("""
            **For best results:**
            - Be specific
            - Provide context
            - Adjust temperature
            - Iterate and refine
            """)
    
    # Text Analyzer
    else:
        st.subheader("Complete Text Analyzer")
        
        analyze_text_final = st.text_area("Text to analyze:", height=200, key="analyze_final")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("📝 Summarize", key="analyze_sum"):
                if analyze_text_final:
                    with st.spinner("Summarizing..."):
                        try:
                            import ollama
                            response = ollama.generate(
                                model='llama2',
                                prompt=f"Summarize this text concisely:\n\n{analyze_text_final}",
                                options={'temperature': 0.3}
                            )
                            st.markdown("**Summary:**")
                            st.write(response['response'])
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        with col2:
            if st.button("😊 Sentiment", key="analyze_sent"):
                if analyze_text_final:
                    with st.spinner("Analyzing..."):
                        try:
                            import ollama
                            response = ollama.generate(
                                model='llama2',
                                prompt=f"Identify the sentiment (Positive/Negative/Neutral) of this text:\n\n{analyze_text_final}",
                                options={'temperature': 0.2}
                            )
                            st.markdown("**Sentiment:**")
                            st.write(response['response'])
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        with col3:
            if st.button("🔑 Key Points", key="analyze_key"):
                if analyze_text_final:
                    with st.spinner("Extracting..."):
                        try:
                            import ollama
                            response = ollama.generate(
                                model='llama2',
                                prompt=f"Extract 5 key points from this text:\n\n{analyze_text_final}",
                                options={'temperature': 0.2}
                            )
                            st.markdown("**Key Points:**")
                            st.write(response['response'])
                        except Exception as e:
                            st.error(f"Error: {str(e)}")
        
        with col4:
            if st.button("📊 Stats", key="analyze_stats"):
                if analyze_text_final:
                    words = len(analyze_text_final.split())
                    chars = len(analyze_text_final)
                    sentences = analyze_text_final.count('.') + analyze_text_final.count('!') + analyze_text_final.count('?')
                    
                    st.markdown("**Statistics:**")
                    st.write(f"Words: {words}")
                    st.write(f"Characters: {chars}")
                    st.write(f"Sentences: {sentences}")
    
    st.markdown("---")
    st.success("🎉 **Congratulations!** You've mastered building Ollama mini apps!")

# Summary
st.markdown("---")
st.markdown("## 📝 Summary")

summary_cols = st.columns(2)

with summary_cols[0]:
    st.markdown("""
    ### Chat Apps:
    1. ✅ Basic chat interface
    2. ✅ Message history management
    3. ✅ Streaming chat responses
    """)
    
    st.markdown("""
    ### Text Generation:
    4. ✅ Generator setup
    5. ✅ Creative writing features
    """)

with summary_cols[1]:
    st.markdown("""
    ### Text Analysis:
    6. ✅ Analyzer foundation
    7. ✅ Summarization
    8. ✅ Sentiment analysis
    9. ✅ Key points extraction
    """)
    
    st.markdown("""
    ### Integration:
    10. ✅ Complete mini apps
    """)

st.info("💡 **Next Steps:** Customize these mini apps for your specific use cases!")
