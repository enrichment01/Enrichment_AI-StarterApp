import streamlit as st
import json

st.set_page_config(page_title="10 Steps: Ollama Amazing Apps", page_icon="⭐", layout="wide")

st.title("⭐ 10 Steps: Ollama Amazing Small Apps")
st.markdown("Build creative and practical AI-powered applications with Ollama.")

# Create tabs for each step
tabs = st.tabs([
    "Code Generator",
    "Code Explainer",
    "Translator",
    "Story Generator",
    "Email Writer",
    "Resume Analyzer",
    "Meeting Notes",
    "Q&A Assistant",
    "Name Generator",
    "App Showcase"
])

# Step 1: Code Generator
with tabs[0]:
    st.header("Step 1: AI Code Generator")
    st.markdown("Generate code in multiple programming languages.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Code Generator:")
        
        # Language selection
        code_lang = st.selectbox(
            "Programming Language:",
            ["Python", "JavaScript", "Java", "C++", "Go", "Rust", "SQL"],
            key="code_lang"
        )
        
        # Code description
        code_desc = st.text_area(
            "Describe what code you need:",
            "Function to calculate factorial of a number using recursion",
            height=100,
            key="code_desc"
        )
        
        # Additional options
        include_comments = st.checkbox("Include comments", value=True, key="code_comments")
        include_docstring = st.checkbox("Include documentation", value=True, key="code_docs")
        
        if st.button("💻 Generate Code", key="code_gen_btn", type="primary"):
            prompt = f"Generate {code_lang} code for the following task: {code_desc}\n"
            if include_comments:
                prompt += "Include inline comments. "
            if include_docstring:
                prompt += "Include documentation/docstrings. "
            
            with st.spinner(f"Generating {code_lang} code..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='codellama',  # Best for code
                        prompt=prompt,
                        options={'temperature': 0.2}  # Low for accuracy
                    )
                    
                    st.markdown("### Generated Code:")
                    st.code(response['response'], language=code_lang.lower())
                    
                    # Download button
                    extensions = {
                        "Python": ".py", "JavaScript": ".js", "Java": ".java",
                        "C++": ".cpp", "Go": ".go", "Rust": ".rs", "SQL": ".sql"
                    }
                    st.download_button(
                        "📥 Download Code",
                        response['response'],
                        f"generated_code{extensions.get(code_lang, '.txt')}",
                        "text/plain"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.info("Tip: Make sure codellama model is installed: `ollama pull codellama`")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Language selection
lang = st.selectbox("Language:", 
    ["Python", "JavaScript", "Java"])

# Description
desc = st.text_area("Describe the code:")

# Options
comments = st.checkbox("Include comments", value=True)
docs = st.checkbox("Include documentation", value=True)

if st.button("Generate Code"):
    # Build prompt
    prompt = f"Generate {lang} code for: {desc}\\n"
    if comments:
        prompt += "Include inline comments. "
    if docs:
        prompt += "Include documentation. "
    
    # Generate with codellama
    response = ollama.generate(
        model='codellama',
        prompt=prompt,
        options={'temperature': 0.2}
    )
    
    st.code(response['response'], language=lang.lower())
"""
        st.code(code, language="python")
        
        st.markdown("### Tips:")
        st.info("""
        - **codellama** model is best for code
        - Use low temperature (0.1-0.3)
        - Be specific about requirements
        - Include example input/output
        """)
    
    st.success("✅ **Key Point:** Use codellama model and low temperature for accurate code generation.")

# Step 2: Code Explainer
with tabs[1]:
    st.header("Step 2: AI Code Explainer")
    st.markdown("Understand code with AI-powered explanations.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Code Explainer:")
        
        # Code input
        code_to_explain = st.text_area(
            "Paste code to explain:",
            """def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)""",
            height=200,
            key="code_explain_input"
        )
        
        explanation_level = st.radio(
            "Explanation Level:",
            ["Beginner", "Intermediate", "Expert"],
            key="explain_level"
        )
        
        if st.button("📚 Explain Code", key="explain_btn"):
            level_prompts = {
                "Beginner": "Explain this code in simple terms for a beginner:",
                "Intermediate": "Explain this code with technical details:",
                "Expert": "Provide an expert-level analysis of this code, including complexity and optimization:"
            }
            
            prompt = f"{level_prompts[explanation_level]}\n\n{code_to_explain}"
            
            with st.spinner("Analyzing code..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='codellama',
                        prompt=prompt,
                        options={'temperature': 0.3}
                    )
                    
                    st.markdown("### Explanation:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Code input
code = st.text_area("Paste code:", height=200)

# Explanation level
level = st.radio("Level:", 
    ["Beginner", "Intermediate", "Expert"])

if st.button("Explain Code"):
    # Customize prompt based on level
    level_prompts = {
        "Beginner": "Explain simply for a beginner:",
        "Intermediate": "Explain with technical details:",
        "Expert": "Provide expert analysis:"
    }
    
    prompt = f"{level_prompts[level]}\\n\\n{code}"
    
    # Generate explanation
    response = ollama.generate(
        model='codellama',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Use Cases:")
        st.info("""
        - 📖 Learning new code
        - 🔍 Code review
        - 📝 Documentation
        - 🎓 Teaching programming
        - 🐛 Debugging assistance
        """)
    
    st.success("✅ **Key Point:** Adjust explanation level to match your audience's expertise.")

# Step 3: Language Translator
with tabs[2]:
    st.header("Step 3: AI Language Translator")
    st.markdown("Translate text between languages with context awareness.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Smart Translator:")
        
        # Language selection
        col_from, col_to = st.columns(2)
        
        with col_from:
            from_lang = st.selectbox(
                "From:",
                ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Chinese", "Japanese"],
                key="from_lang"
            )
        
        with col_to:
            to_lang = st.selectbox(
                "To:",
                ["Spanish", "French", "German", "Italian", "Portuguese", "Chinese", "Japanese", "English"],
                key="to_lang"
            )
        
        # Text to translate
        text_translate = st.text_area(
            "Text to translate:",
            "Hello! How are you today? I hope you're having a wonderful day.",
            height=100,
            key="translate_text"
        )
        
        # Translation style
        style = st.radio(
            "Translation Style:",
            ["Formal", "Casual", "Literary"],
            key="translate_style",
            horizontal=True
        )
        
        if st.button("🌍 Translate", key="translate_btn"):
            prompt = f"Translate the following text from {from_lang} to {to_lang}. Use a {style.lower()} style:\n\n{text_translate}"
            
            with st.spinner("Translating..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.3}
                    )
                    
                    st.markdown("### Translation:")
                    st.write(response['response'])
                    
                    # Back-translation for verification
                    if st.checkbox("Show back-translation (verify accuracy)", key="back_trans"):
                        back_prompt = f"Translate this {to_lang} text back to {from_lang}:\n\n{response['response']}"
                        back_response = ollama.generate(
                            model='llama2',
                            prompt=back_prompt,
                            options={'temperature': 0.3}
                        )
                        st.markdown("### Back-translation:")
                        st.write(back_response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Language selection
col1, col2 = st.columns(2)
with col1:
    from_lang = st.selectbox("From:", 
        ["English", "Spanish", "French"])
with col2:
    to_lang = st.selectbox("To:", 
        ["Spanish", "French", "German"])

# Text input
text = st.text_area("Text to translate:")

# Style
style = st.radio("Style:", 
    ["Formal", "Casual", "Literary"])

if st.button("Translate"):
    prompt = f\"\"\"Translate from {from_lang} to {to_lang}.
    Use a {style.lower()} style:
    
    {text}\"\"\"
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Features:")
        st.info("""
        - ✅ Multiple languages
        - ✅ Style control (formal/casual)
        - ✅ Context-aware translation
        - ✅ Back-translation verification
        - ✅ Preserves meaning and tone
        """)
    
    st.success("✅ **Key Point:** AI translation understands context better than word-for-word translation.")

# Step 4: Story Generator
with tabs[3]:
    st.header("Step 4: Creative Story Generator")
    st.markdown("Generate engaging stories with customizable elements.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Story Creator:")
        
        # Story parameters
        genre = st.selectbox(
            "Genre:",
            ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror", "Adventure", "Comedy"],
            key="story_genre"
        )
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            protagonist = st.text_input("Protagonist:", "a young detective", key="story_protag")
        
        with col_b:
            setting = st.text_input("Setting:", "a futuristic city", key="story_setting")
        
        conflict = st.text_input("Conflict/Challenge:", "solve a mysterious disappearance", key="story_conflict")
        
        length = st.select_slider(
            "Story Length:",
            ["Very Short", "Short", "Medium", "Long"],
            value="Short",
            key="story_length"
        )
        
        if st.button("📖 Generate Story", key="story_btn", type="primary"):
            length_map = {
                "Very Short": "a very brief story (2-3 paragraphs)",
                "Short": "a short story (4-5 paragraphs)",
                "Medium": "a medium-length story (6-8 paragraphs)",
                "Long": "a longer story (10+ paragraphs)"
            }
            
            prompt = f"""Write {length_map[length]} in the {genre} genre.
            
            Protagonist: {protagonist}
            Setting: {setting}
            Central Conflict: {conflict}
            
            Make it engaging with vivid descriptions, compelling characters, and an interesting plot."""
            
            st.markdown("### Your Story:")
            placeholder = st.empty()
            full_story = ""
            
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
                        full_story += chunk['response']
                        placeholder.markdown(full_story + "▌")
                
                placeholder.markdown(full_story)
                
                # Download option
                st.download_button(
                    "📥 Download Story",
                    full_story,
                    "my_story.txt",
                    "text/plain"
                )
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Story parameters
genre = st.selectbox("Genre:", 
    ["Fantasy", "Sci-Fi", "Mystery"])

protagonist = st.text_input("Protagonist:", 
    "a young detective")
setting = st.text_input("Setting:", 
    "a futuristic city")
conflict = st.text_input("Conflict:", 
    "solve a mysterious disappearance")

length = st.select_slider("Length:", 
    ["Short", "Medium", "Long"])

if st.button("Generate Story"):
    prompt = f\"\"\"Write a {length.lower()} story 
    in the {genre} genre.
    
    Protagonist: {protagonist}
    Setting: {setting}
    Conflict: {conflict}
    
    Make it engaging and vivid.\"\"\"
    
    # Stream with high creativity
    full_story = ""
    placeholder = st.empty()
    
    stream = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.9},
        stream=True
    )
    
    for chunk in stream:
        full_story += chunk['response']
        placeholder.markdown(full_story + "▌")
"""
        st.code(code, language="python")
    
    st.success("✅ **Key Point:** High temperature (0.8-1.0) produces more creative and varied stories.")

# Step 5: Email Writer
with tabs[4]:
    st.header("Step 5: Professional Email Writer")
    st.markdown("Generate professional emails for any situation.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Email Generator:")
        
        # Email type
        email_type = st.selectbox(
            "Email Type:",
            ["Business Inquiry", "Job Application", "Follow-up", "Thank You", "Complaint", "Invitation", "Networking"],
            key="email_type"
        )
        
        # Recipient
        recipient = st.text_input("Recipient:", "Hiring Manager", key="email_recipient")
        
        # Purpose
        purpose = st.text_area(
            "Email Purpose:",
            "Express interest in the Senior Developer position and request an interview",
            height=80,
            key="email_purpose"
        )
        
        # Tone
        tone = st.select_slider(
            "Tone:",
            ["Very Formal", "Formal", "Professional", "Friendly", "Casual"],
            value="Professional",
            key="email_tone"
        )
        
        # Additional details
        include_signature = st.checkbox("Include signature section", value=True, key="email_sig")
        
        if st.button("✉️ Generate Email", key="email_btn"):
            prompt = f"""Write a {tone.lower()} email for: {email_type}

Recipient: {recipient}
Purpose: {purpose}

The email should be clear, concise, and professional."""
            
            if include_signature:
                prompt += " Include a signature section with placeholders like [Your Name], [Your Contact]."
            
            with st.spinner("Composing email..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.4}
                    )
                    
                    st.markdown("### Generated Email:")
                    st.write(response['response'])
                    
                    # Copy to clipboard hint
                    st.info("💡 Tip: You can copy the email and customize it further.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Email parameters
email_type = st.selectbox("Email Type:", 
    ["Business Inquiry", "Job Application", "Follow-up"])

recipient = st.text_input("Recipient:", "Hiring Manager")

purpose = st.text_area("Purpose:", height=80)

tone = st.select_slider("Tone:", 
    ["Formal", "Professional", "Friendly"])

if st.button("Generate Email"):
    prompt = f\"\"\"Write a {tone.lower()} email for: 
    {email_type}
    
    Recipient: {recipient}
    Purpose: {purpose}
    
    The email should be clear and professional.\"\"\"
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.4}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Email Tips:")
        st.info("""
        - ✅ Clear subject line
        - ✅ Professional greeting
        - ✅ Concise body
        - ✅ Specific call-to-action
        - ✅ Proper closing
        """)
    
    st.success("✅ **Key Point:** Moderate temperature (0.3-0.5) balances professionalism with natural flow.")

# Step 6: Resume Analyzer
with tabs[5]:
    st.header("Step 6: AI Resume Analyzer")
    st.markdown("Get detailed feedback on resumes and CVs.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Resume Analyzer:")
        
        # Resume input
        resume_text = st.text_area(
            "Paste resume text:",
            """John Doe
Software Engineer

Experience:
- 3 years as Full Stack Developer
- Proficient in Python, JavaScript, React
- Built scalable web applications

Education:
- B.S. Computer Science, State University

Skills:
- Programming: Python, JavaScript, Java
- Frameworks: React, Django, Node.js
- Tools: Git, Docker, AWS""",
            height=250,
            key="resume_text"
        )
        
        # Job role context
        job_role = st.text_input(
            "Target Job Role (optional):",
            "Senior Software Engineer",
            key="resume_role"
        )
        
        # Analysis type
        analysis_types = st.multiselect(
            "Analysis to perform:",
            ["Overall Assessment", "Strengths", "Weaknesses", "Suggestions", "ATS Optimization"],
            default=["Overall Assessment", "Suggestions"],
            key="resume_analysis"
        )
        
        if st.button("📊 Analyze Resume", key="resume_btn"):
            analyses = ", ".join(analysis_types)
            
            prompt = f"""Analyze this resume for a {job_role} position.

Provide:
{', '.join(analysis_types)}

Resume:
{resume_text}

Be specific and constructive in your feedback."""
            
            with st.spinner("Analyzing resume..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.3}
                    )
                    
                    st.markdown("### Analysis:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Resume input
resume = st.text_area("Paste resume:", height=250)

# Target role
role = st.text_input("Target Role:", 
    "Senior Software Engineer")

# Analysis options
analysis = st.multiselect("Analysis:", 
    ["Assessment", "Strengths", "Weaknesses", 
     "Suggestions", "ATS Optimization"])

if st.button("Analyze Resume"):
    prompt = f\"\"\"Analyze this resume for {role}.
    
    Provide: {', '.join(analysis)}
    
    Resume:
    {resume}
    
    Be specific and constructive.\"\"\"
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### What to Analyze:")
        st.info("""
        - ✅ Content quality
        - ✅ Relevant keywords
        - ✅ Achievements vs duties
        - ✅ Formatting consistency
        - ✅ ATS compatibility
        """)
    
    st.success("✅ **Key Point:** AI can provide objective feedback on resume effectiveness.")

# Step 7: Meeting Summarizer
with tabs[6]:
    st.header("Step 7: Meeting Notes Summarizer")
    st.markdown("Transform meeting transcripts into actionable summaries.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Meeting Summarizer:")
        
        # Meeting notes input
        meeting_notes = st.text_area(
            "Paste meeting transcript/notes:",
            """Team Meeting - Product Launch Discussion

John: We need to finalize the product launch date. Marketing suggests June 15th.

Sarah: That works for us. We'll need the final specs by May 30th.

Mike: I can commit to that. What about the budget?

John: Budget is approved at $50k. Any concerns?

Sarah: No concerns. I'll prepare the marketing plan and share it by Friday.

Mike: Let's schedule a follow-up next Tuesday to review progress.

Action Items:
- Final specs delivery: May 30th (Mike)
- Marketing plan: This Friday (Sarah)
- Follow-up meeting: Next Tuesday""",
            height=300,
            key="meeting_notes"
        )
        
        # Summary options
        include_action_items = st.checkbox("Extract action items", value=True, key="meeting_actions")
        include_decisions = st.checkbox("Highlight decisions", value=True, key="meeting_decisions")
        include_attendees = st.checkbox("List attendees", value=False, key="meeting_attendees")
        
        if st.button("📝 Summarize Meeting", key="meeting_btn"):
            prompt = f"Summarize the following meeting notes:\n\n{meeting_notes}\n\n"
            
            if include_action_items:
                prompt += "Clearly list all action items with assigned owners and deadlines.\n"
            if include_decisions:
                prompt += "Highlight key decisions made.\n"
            if include_attendees:
                prompt += "List meeting attendees.\n"
            
            prompt += "Keep the summary concise and well-organized."
            
            with st.spinner("Summarizing meeting..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.2}
                    )
                    
                    st.markdown("### Meeting Summary:")
                    st.write(response['response'])
                    
                    # Download option
                    st.download_button(
                        "📥 Download Summary",
                        response['response'],
                        "meeting_summary.txt",
                        "text/plain"
                    )
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Meeting notes input
notes = st.text_area("Meeting notes:", height=300)

# Summary options
action_items = st.checkbox("Extract action items", 
    value=True)
decisions = st.checkbox("Highlight decisions", 
    value=True)

if st.button("Summarize Meeting"):
    prompt = f"Summarize these meeting notes:\\n\\n{notes}\\n\\n"
    
    if action_items:
        prompt += "List all action items with owners.\\n"
    if decisions:
        prompt += "Highlight key decisions.\\n"
    
    prompt += "Keep it concise and organized."
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.2}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Best Practices:")
        st.info("""
        - ✅ Include timestamps if available
        - ✅ Note who said what
        - ✅ Capture decisions clearly
        - ✅ List all action items
        - ✅ Share summary promptly
        """)
    
    st.success("✅ **Key Point:** Low temperature ensures accurate extraction of facts and action items.")

# Step 8: Q&A Assistant
with tabs[7]:
    st.header("Step 8: Smart Q&A Assistant")
    st.markdown("Build an intelligent question-answering system.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Q&A Assistant:")
        
        # Context/knowledge base
        context = st.text_area(
            "Knowledge Base / Context:",
            """Our company offers three subscription plans:

Basic Plan ($9/month):
- Up to 5 users
- 10GB storage
- Email support

Pro Plan ($29/month):
- Up to 25 users
- 100GB storage
- Priority email support
- Advanced analytics

Enterprise Plan (Custom pricing):
- Unlimited users
- Unlimited storage
- 24/7 phone support
- Dedicated account manager
- Custom integrations

Free trial available for all plans.""",
            height=250,
            key="qa_context"
        )
        
        # Question
        question = st.text_input(
            "Ask a question:",
            "What's included in the Pro plan?",
            key="qa_question"
        )
        
        # Response style
        answer_style = st.radio(
            "Answer Style:",
            ["Concise", "Detailed", "Bullet Points"],
            key="qa_style",
            horizontal=True
        )
        
        if st.button("❓ Get Answer", key="qa_btn"):
            style_instructions = {
                "Concise": "Provide a brief, direct answer.",
                "Detailed": "Provide a comprehensive, detailed answer.",
                "Bullet Points": "Answer using bullet points."
            }
            
            prompt = f"""Based on the following context, answer the question.
{style_instructions[answer_style]}

Context:
{context}

Question: {question}

Answer:"""
            
            with st.spinner("Finding answer..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.2}
                    )
                    
                    st.markdown("### Answer:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# Knowledge base
context = st.text_area("Knowledge Base:", height=250)

# Question
question = st.text_input("Ask a question:")

# Style
style = st.radio("Answer Style:", 
    ["Concise", "Detailed", "Bullet Points"])

if st.button("Get Answer"):
    style_map = {
        "Concise": "Provide a brief answer.",
        "Detailed": "Provide a detailed answer.",
        "Bullet Points": "Answer using bullet points."
    }
    
    prompt = f\"\"\"Based on this context, answer the question.
    {style_map[style]}
    
    Context:
    {context}
    
    Question: {question}
    
    Answer:\"\"\"
    
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
        - 📚 Documentation assistant
        - 🛍️ Customer support
        - 📖 Educational content
        - 🏢 Company knowledge base
        - 📋 FAQ automation
        """)
    
    st.success("✅ **Key Point:** Grounding answers in context prevents hallucination.")

# Step 9: Creative Name Generator
with tabs[8]:
    st.header("Step 9: Creative Name Generator")
    st.markdown("Generate creative names for products, companies, or projects.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Name Generator:")
        
        # What to name
        name_type = st.selectbox(
            "What needs a name?",
            ["Startup/Company", "Product", "App", "Project", "Character", "Brand", "Website"],
            key="name_type"
        )
        
        # Description
        description = st.text_area(
            "Describe it:",
            "A mobile app that helps people track their daily water intake and stay hydrated",
            height=100,
            key="name_desc"
        )
        
        # Style preferences
        col_a, col_b = st.columns(2)
        
        with col_a:
            name_style = st.selectbox(
                "Style:",
                ["Modern", "Classic", "Playful", "Professional", "Tech-savvy", "Elegant"],
                key="name_style"
            )
        
        with col_b:
            num_suggestions = st.slider("Number of suggestions:", 3, 10, 5, key="name_count")
        
        # Additional preferences
        short_names = st.checkbox("Prefer short names (1-2 words)", value=True, key="name_short")
        
        if st.button("✨ Generate Names", key="name_btn", type="primary"):
            prompt = f"""Generate {num_suggestions} creative {name_style.lower()} names for a {name_type.lower()}.

Description: {description}
"""
            
            if short_names:
                prompt += "\nPrefer short, memorable names (1-2 words)."
            
            prompt += "\n\nFor each name, provide a brief explanation of why it fits."
            
            with st.spinner("Generating creative names..."):
                try:
                    import ollama
                    response = ollama.generate(
                        model='llama2',
                        prompt=prompt,
                        options={'temperature': 0.8}  # Creative
                    )
                    
                    st.markdown("### Name Suggestions:")
                    st.write(response['response'])
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.markdown("### Code:")
        code = """
import streamlit as st
import ollama

# What to name
name_type = st.selectbox("What needs a name?", 
    ["Startup", "Product", "App", "Project"])

# Description
description = st.text_area("Describe it:", height=100)

# Preferences
style = st.selectbox("Style:", 
    ["Modern", "Classic", "Playful"])
num_names = st.slider("Suggestions:", 3, 10, 5)
short = st.checkbox("Prefer short names", value=True)

if st.button("Generate Names"):
    prompt = f\"\"\"Generate {num_names} creative 
    {style.lower()} names for a {name_type.lower()}.
    
    Description: {description}
    \"\"\"
    
    if short:
        prompt += "\\nPrefer short names (1-2 words)."
    
    prompt += "\\nExplain each name."
    
    response = ollama.generate(
        model='llama2',
        prompt=prompt,
        options={'temperature': 0.8}
    )
    
    st.write(response['response'])
"""
        st.code(code, language="python")
        
        st.markdown("### Naming Tips:")
        st.info("""
        - ✅ Easy to pronounce
        - ✅ Memorable
        - ✅ Relevant to purpose
        - ✅ Available domain/trademark
        - ✅ Works across cultures
        """)
    
    st.success("✅ **Key Point:** Higher temperature (0.7-0.9) generates more diverse and creative names.")

# Step 10: Application Showcase
with tabs[9]:
    st.header("Step 10: Amazing Apps Showcase")
    st.markdown("Explore all the amazing apps you can build with Ollama!")
    
    st.markdown("### 🎯 Application Gallery")
    
    # Create a grid of app cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.markdown("#### 💻 Code Generator")
            st.markdown("Generate code in any language")
            st.caption("Best for: Development tasks")
            
        with st.container():
            st.markdown("#### 🌍 Translator")
            st.markdown("Context-aware language translation")
            st.caption("Best for: Multilingual content")
            
        with st.container():
            st.markdown("#### ✉️ Email Writer")
            st.markdown("Professional email composition")
            st.caption("Best for: Business communication")
    
    with col2:
        with st.container():
            st.markdown("#### 📚 Code Explainer")
            st.markdown("Understand any code snippet")
            st.caption("Best for: Learning & review")
            
        with st.container():
            st.markdown("#### 📖 Story Generator")
            st.markdown("Creative storytelling")
            st.caption("Best for: Content creation")
            
        with st.container():
            st.markdown("#### 📊 Resume Analyzer")
            st.markdown("Get resume feedback")
            st.caption("Best for: Job hunting")
    
    with col3:
        with st.container():
            st.markdown("#### 📝 Meeting Notes")
            st.markdown("Summarize meetings")
            st.caption("Best for: Productivity")
            
        with st.container():
            st.markdown("#### ❓ Q&A Assistant")
            st.markdown("Knowledge base queries")
            st.caption("Best for: Support & docs")
            
        with st.container():
            st.markdown("#### ✨ Name Generator")
            st.markdown("Creative naming")
            st.caption("Best for: Branding")
    
    st.markdown("---")
    
    # Complete integrated example
    st.markdown("### 🚀 Quick Multi-Tool Demo")
    st.markdown("Try any of the amazing apps in one place!")
    
    demo_app = st.selectbox(
        "Choose an app:",
        [
            "💻 Code Generator",
            "📚 Code Explainer",
            "🌍 Language Translator",
            "📖 Story Generator",
            "✉️ Email Writer",
            "📊 Resume Analyzer",
            "📝 Meeting Summarizer",
            "❓ Q&A Assistant",
            "✨ Name Generator"
        ],
        key="demo_app"
    )
    
    st.markdown(f"**{demo_app}** - Visit the respective tab above for the full experience!")
    
    st.markdown("---")
    
    # Architecture diagram
    st.markdown("### 🏗️ App Architecture")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        #### Common Pattern:
        1. **User Input** → Interface for data
        2. **Prompt Engineering** → Craft effective prompts
        3. **Ollama Processing** → AI generation
        4. **Result Display** → Show formatted output
        5. **Options** → Export, save, iterate
        """)
    
    with col2:
        st.markdown("""
        #### Best Practices:
        - ✅ Clear user instructions
        - ✅ Appropriate temperature settings
        - ✅ Error handling
        - ✅ Streaming for long outputs
        - ✅ Export/download options
        - ✅ Context management
        """)
    
    st.markdown("---")
    
    # Complete app template
    st.markdown("### 📋 Complete App Template")
    
    template_code = """
import streamlit as st
import ollama

st.set_page_config(page_title="My AI App", page_icon="🤖", layout="wide")

st.title("🤖 My AI-Powered App")

# Sidebar configuration
with st.sidebar:
    st.markdown("### Settings")
    model = st.selectbox("Model:", ["llama2", "mistral", "codellama"])
    temperature = st.slider("Temperature:", 0.0, 2.0, 0.7)
    
# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Input")
    
    # User inputs
    user_input = st.text_area("Enter your prompt:", height=200)
    
    # Processing options
    stream_output = st.checkbox("Stream output", value=True)
    
    if st.button("🚀 Generate", type="primary"):
        if user_input:
            # Build prompt
            prompt = f"Process this: {user_input}"
            
            # Generate
            if stream_output:
                placeholder = st.empty()
                full_response = ""
                
                stream = ollama.generate(
                    model=model,
                    prompt=prompt,
                    options={'temperature': temperature},
                    stream=True
                )
                
                for chunk in stream:
                    full_response += chunk['response']
                    placeholder.markdown(full_response + "▌")
                
                placeholder.markdown(full_response)
            else:
                with st.spinner("Processing..."):
                    response = ollama.generate(
                        model=model,
                        prompt=prompt,
                        options={'temperature': temperature}
                    )
                    st.write(response['response'])
            
            # Download option
            st.download_button(
                "📥 Download",
                full_response if stream_output else response['response'],
                "result.txt",
                "text/plain"
            )
        else:
            st.warning("Please enter a prompt")

with col2:
    st.markdown("### Help")
    st.info(\"\"\"
    **How to use:**
    1. Enter your prompt
    2. Adjust settings
    3. Click Generate
    4. Download results
    \"\"\")
    
    st.markdown("### Tips")
    st.success(\"\"\"
    - Be specific
    - Adjust temperature
    - Use streaming
    - Iterate
    \"\"\")
"""
    
    st.code(template_code, language="python")
    
    st.markdown("---")
    
    st.success("🎉 **Congratulations!** You've learned to build 10 amazing AI-powered applications!")
    
    st.markdown("### 🎓 What's Next?")
    st.info("""
    - 🔨 Customize these apps for your needs
    - 🎨 Add your own branding and styling
    - 📊 Integrate with databases and APIs
    - 🚀 Deploy your apps to production
    - 🤝 Share your creations with others
    """)

# Summary
st.markdown("---")
st.markdown("## 📝 Summary")

summary_cols = st.columns(2)

with summary_cols[0]:
    st.markdown("""
    ### Development Tools:
    1. ✅ AI Code Generator
    2. ✅ Code Explainer
    3. ✅ Language Translator
    4. ✅ Story Generator
    5. ✅ Professional Email Writer
    """)

with summary_cols[1]:
    st.markdown("""
    ### Productivity Apps:
    6. ✅ Resume Analyzer
    7. ✅ Meeting Summarizer
    8. ✅ Q&A Assistant
    9. ✅ Creative Name Generator
    10. ✅ Complete App Showcase
    """)

st.info("💡 **Final Tip:** Mix and match features from different apps to create your own unique AI-powered tools!")
