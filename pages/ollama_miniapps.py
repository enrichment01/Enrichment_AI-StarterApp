import streamlit as st
import time

def show():
    st.header("🚀 Ollama AI MiniApps")
    st.markdown("Complete mini-applications powered by Ollama.")
    
    # Select mini app
    app_choice = st.selectbox(
        "Choose a Mini App:",
        ["📝 Text Generator", "💬 Chatbot", "🔍 Text Analyzer"]
    )
    
    st.markdown("---")
    
    # Text Generator App
    if app_choice == "📝 Text Generator":
        st.subheader("📝 AI Text Generator")
        st.markdown("Generate creative text using Ollama models.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # User inputs
            prompt = st.text_area(
                "Enter your prompt:",
                placeholder="Write a short story about a robot learning to paint...",
                height=100
            )
            
            col_a, col_b = st.columns(2)
            with col_a:
                model = st.selectbox(
                    "Select Model:",
                    ["llama2", "mistral", "codellama", "phi"],
                    key="gen_model"
                )
            
            with col_b:
                temperature = st.slider(
                    "Creativity (Temperature):",
                    0.0, 2.0, 0.7, 0.1,
                    key="gen_temp"
                )
            
            max_tokens = st.slider(
                "Max Length (tokens):",
                50, 500, 200,
                key="gen_tokens"
            )
            
            if st.button("✨ Generate", key="generate_btn", type="primary"):
                if not prompt:
                    st.warning("Please enter a prompt!")
                else:
                    try:
                        import ollama
                        
                        with st.spinner(f"Generating with {model}..."):
                            response = ollama.generate(
                                model=model,
                                prompt=prompt,
                                options={
                                    'temperature': temperature,
                                    'num_predict': max_tokens,
                                }
                            )
                            
                            st.success("✅ Generated!")
                            st.markdown("### Result:")
                            st.write(response['response'])
                            
                            # Show stats
                            with st.expander("📊 Generation Stats"):
                                st.write(f"**Model:** {model}")
                                st.write(f"**Temperature:** {temperature}")
                                st.write(f"**Max Tokens:** {max_tokens}")
                                if 'total_duration' in response:
                                    duration_sec = response['total_duration'] / 1e9
                                    st.write(f"**Duration:** {duration_sec:.2f}s")
                    
                    except ImportError:
                        st.error("❌ Ollama Python SDK not installed. Run: `pip install ollama`")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.info("Make sure Ollama is running and the model is installed.")
        
        with col2:
            st.markdown("### 💡 Tips")
            st.info("""
            **Prompt Tips:**
            - Be specific and clear
            - Provide context
            - Use examples if needed
            
            **Temperature:**
            - 0.0-0.3: Focused, deterministic
            - 0.4-0.7: Balanced
            - 0.8-2.0: Creative, random
            
            **Models:**
            - llama2: General purpose
            - mistral: Fast, efficient
            - codellama: For code
            - phi: Lightweight
            """)
    
    # Chatbot App
    elif app_choice == "💬 Chatbot":
        st.subheader("💬 AI Chatbot")
        st.markdown("Have a conversation with an AI assistant.")
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        if "chatbot_model" not in st.session_state:
            st.session_state.chatbot_model = "llama2"
        
        # Sidebar settings
        with st.sidebar:
            st.markdown("### ⚙️ Chatbot Settings")
            
            st.session_state.chatbot_model = st.selectbox(
                "Model:",
                ["llama2", "mistral", "codellama", "phi"],
                index=0,
                key="chatbot_model_select"
            )
            
            system_prompt = st.text_area(
                "System Prompt:",
                value="You are a helpful AI assistant.",
                height=100,
                key="system_prompt"
            )
            
            temperature = st.slider(
                "Temperature:",
                0.0, 2.0, 0.7, 0.1,
                key="chatbot_temp"
            )
            
            if st.button("🗑️ Clear Chat", key="clear_chat"):
                st.session_state.messages = []
                st.rerun()
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Type your message..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate assistant response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                try:
                    import ollama
                    
                    # Prepare messages
                    messages = [{"role": "system", "content": system_prompt}]
                    messages.extend(st.session_state.messages)
                    
                    # Stream response
                    stream = ollama.chat(
                        model=st.session_state.chatbot_model,
                        messages=messages,
                        stream=True,
                        options={'temperature': temperature}
                    )
                    
                    for chunk in stream:
                        if 'message' in chunk and 'content' in chunk['message']:
                            full_response += chunk['message']['content']
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                    
                except ImportError:
                    full_response = "❌ Ollama Python SDK not installed. Run: `pip install ollama`"
                    message_placeholder.markdown(full_response)
                except Exception as e:
                    full_response = f"❌ Error: {str(e)}\n\nMake sure Ollama is running and the model is installed."
                    message_placeholder.markdown(full_response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        # Instructions
        if len(st.session_state.messages) == 0:
            st.info("""
            👋 Welcome to the AI Chatbot!
            
            **How to use:**
            1. Type your message in the input box below
            2. Press Enter to send
            3. Wait for the AI to respond
            4. Continue the conversation!
            
            **Customize:**
            - Change the model in the sidebar
            - Adjust the system prompt to change behavior
            - Modify temperature for creativity
            - Clear chat to start fresh
            """)
    
    # Text Analyzer App
    elif app_choice == "🔍 Text Analyzer":
        st.subheader("🔍 AI Text Analyzer")
        st.markdown("Analyze text with AI-powered insights.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            text_to_analyze = st.text_area(
                "Enter text to analyze:",
                placeholder="Paste any text here...",
                height=200,
                key="analyze_text"
            )
            
            analysis_type = st.selectbox(
                "Analysis Type:",
                [
                    "Summarize",
                    "Extract Key Points",
                    "Sentiment Analysis",
                    "Find Main Topics",
                    "Translate to Simple Language",
                    "Grammar Check"
                ],
                key="analysis_type"
            )
            
            model = st.selectbox(
                "Model:",
                ["llama2", "mistral", "phi"],
                key="analyze_model"
            )
            
            if st.button("🔍 Analyze", key="analyze_btn", type="primary"):
                if not text_to_analyze:
                    st.warning("Please enter text to analyze!")
                else:
                    # Create prompt based on analysis type
                    prompts = {
                        "Summarize": f"Summarize the following text concisely:\n\n{text_to_analyze}",
                        "Extract Key Points": f"Extract the key points from the following text as a bulleted list:\n\n{text_to_analyze}",
                        "Sentiment Analysis": f"Analyze the sentiment of the following text (positive, negative, or neutral) and explain why:\n\n{text_to_analyze}",
                        "Find Main Topics": f"Identify the main topics discussed in the following text:\n\n{text_to_analyze}",
                        "Translate to Simple Language": f"Rewrite the following text in simple, easy-to-understand language:\n\n{text_to_analyze}",
                        "Grammar Check": f"Check the following text for grammar errors and suggest corrections:\n\n{text_to_analyze}"
                    }
                    
                    prompt = prompts[analysis_type]
                    
                    try:
                        import ollama
                        
                        with st.spinner(f"Analyzing with {model}..."):
                            response = ollama.generate(
                                model=model,
                                prompt=prompt,
                                options={'temperature': 0.3}  # Lower temp for analysis
                            )
                            
                            st.success("✅ Analysis Complete!")
                            st.markdown("### Result:")
                            st.write(response['response'])
                            
                            # Show stats
                            with st.expander("📊 Analysis Stats"):
                                st.write(f"**Analysis Type:** {analysis_type}")
                                st.write(f"**Model:** {model}")
                                st.write(f"**Input Length:** {len(text_to_analyze)} characters")
                                if 'total_duration' in response:
                                    duration_sec = response['total_duration'] / 1e9
                                    st.write(f"**Duration:** {duration_sec:.2f}s")
                    
                    except ImportError:
                        st.error("❌ Ollama Python SDK not installed. Run: `pip install ollama`")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
                        st.info("Make sure Ollama is running and the model is installed.")
        
        with col2:
            st.markdown("### 📝 Sample Texts")
            
            sample_texts = {
                "News Article": "Scientists have discovered a new species of butterfly in the Amazon rainforest. The butterfly, named Morpho amazonicus, has distinctive blue and green wings that shimmer in the sunlight. Researchers believe this discovery could provide insights into the region's biodiversity.",
                "Product Review": "I recently purchased this laptop and I'm extremely impressed. The build quality is excellent, the screen is vibrant, and the battery life exceeds expectations. However, the keyboard could be better and it's a bit pricey.",
                "Technical Text": "The algorithm utilizes a recursive approach to traverse the binary tree in depth-first manner. By implementing memoization, we can optimize the time complexity from O(2^n) to O(n), significantly improving performance for large datasets."
            }
            
            for title, text in sample_texts.items():
                if st.button(f"Load: {title}", key=f"sample_{title}"):
                    st.session_state.analyze_text = text
                    st.rerun()
    
    # Code Examples
    st.markdown("---")
    with st.expander("💻 View Source Code"):
        st.markdown(f"### Code for {app_choice}")
        
        if app_choice == "📝 Text Generator":
            st.code("""
import ollama

prompt = "Write a short story about a robot"
model = "llama2"
temperature = 0.7

response = ollama.generate(
    model=model,
    prompt=prompt,
    options={
        'temperature': temperature,
        'num_predict': 200,
    }
)

print(response['response'])
            """, language="python")
        
        elif app_choice == "💬 Chatbot":
            st.code("""
import ollama

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

stream = ollama.chat(
    model='llama2',
    messages=messages,
    stream=True
)

for chunk in stream:
    print(chunk['message']['content'], end='')
            """, language="python")
        
        elif app_choice == "🔍 Text Analyzer":
            st.code("""
import ollama

text = "Your text here..."
analysis_type = "Summarize"

prompt = f"Summarize the following text concisely:\\n\\n{text}"

response = ollama.generate(
    model='llama2',
    prompt=prompt,
    options={'temperature': 0.3}
)

print(response['response'])
            """, language="python")
