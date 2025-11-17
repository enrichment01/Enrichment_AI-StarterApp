import streamlit as st
import time
from scripts import text_generator, chatbot, text_analyzer, code_utils

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
                    with st.spinner(f"Generating with {model}..."):
                        result = text_generator.generate_text(
                            model=model,
                            prompt=prompt,
                            temperature=temperature,
                            max_tokens=max_tokens
                        )
                        
                        if result['status'] == 'success':
                            st.success("✅ Generated!")
                            st.markdown("### Result:")
                            st.write(result['response'])
                            
                            # Show stats
                            with st.expander("📊 Generation Stats"):
                                for key, value in result['stats'].items():
                                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")
                        else:
                            st.error(f"❌ {result['message']}")
        
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
                
                # Prepare messages
                messages = chatbot.prepare_chat_messages(
                    st.session_state.messages,
                    system_prompt
                )
                
                # Stream response
                stream = chatbot.generate_chat_response(
                    model=st.session_state.chatbot_model,
                    messages=messages,
                    temperature=temperature,
                    stream=True
                )
                
                for chunk in stream:
                    if 'message' in chunk and 'content' in chunk['message']:
                        full_response += chunk['message']['content']
                        message_placeholder.markdown(full_response + "▌")
                
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
                    with st.spinner(f"Analyzing with {model}..."):
                        result = text_analyzer.analyze_text(
                            model=model,
                            text=text_to_analyze,
                            analysis_type=analysis_type
                        )
                        
                        if result['status'] == 'success':
                            st.success("✅ Analysis Complete!")
                            st.markdown("### Result:")
                            st.write(result['response'])
                            
                            # Show stats
                            with st.expander("📊 Analysis Stats"):
                                for key, value in result['stats'].items():
                                    st.write(f"**{key.replace('_', ' ').title()}:** {value}")
                        else:
                            st.error(f"❌ {result['message']}")
        
        with col2:
            st.markdown("### 📝 Sample Texts")
            
            for title in text_analyzer.SAMPLE_TEXTS.keys():
                if st.button(f"Load: {title}", key=f"sample_{title}"):
                    st.session_state.analyze_text = text_analyzer.get_sample_text(title)
                    st.rerun()
    
    # Code Examples
    st.markdown("---")
    with st.expander("💻 View Source Code"):
        st.markdown(f"### Code for {app_choice}")
        
        if app_choice == "📝 Text Generator":
            CODE = code_utils.get_code("ollama_miniapps/text_generator.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
        elif app_choice == "💬 Chatbot":
            CODE = code_utils.get_code("ollama_miniapps/chatbot.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
        
        elif app_choice == "🔍 Text Analyzer":
            CODE = code_utils.get_code("ollama_miniapps/text_analyzer.py")
            st.code(CODE, language="python")
            code_utils.run_code(CODE)
