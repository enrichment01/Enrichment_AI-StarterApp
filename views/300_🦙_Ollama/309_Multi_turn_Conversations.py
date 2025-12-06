import streamlit as st

st.header("💬 Multi-turn Conversations — Ollama Basics")
st.markdown("Building conversational AI with context and memory.")

# Explanation
st.subheader("What are Multi-turn Conversations?")

st.write("""
Multi-turn conversations allow the AI to remember previous messages and 
maintain context throughout a conversation, just like chatting with a person.
""")

# Basic example
st.subheader("Basic Multi-turn Example")

code_example = """
import ollama

# Initialize conversation history
messages = []

# Turn 1: User introduces themselves
messages.append({
    'role': 'user',
    'content': 'My name is Alice and I love Python.'
})

response = ollama.chat(
    model='phi4-mini',
    messages=messages
)

# Add AI response to history
messages.append({
    'role': 'assistant',
    'content': response['message']['content']
})

# Turn 2: User asks a follow-up (AI remembers name)
messages.append({
    'role': 'user',
    'content': 'What did I say my name was?'
})

response = ollama.chat(
    model='phi4-mini',
    messages=messages
)

print(response['message']['content'])
# Output: "You said your name was Alice."
"""

st.code(code_example, language="python")

# Interactive demo
st.subheader("🎮 Interactive Demo")

# Initialize chat history in session state
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Display chat history
for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to history
    st.session_state.chat_messages.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Simulate AI response (placeholder since Ollama might not be available)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # In a real app, you would call ollama.chat() here
            ai_response = f"I understand you said: '{user_input}'. I'm maintaining context of our conversation."
            st.write(ai_response)
    
    # Add AI response to history
    st.session_state.chat_messages.append({
        "role": "assistant",
        "content": ai_response
    })

# Clear chat button
if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_messages = []
    st.rerun()

# Message structure
st.subheader("📋 Message Structure")

message_format = """
messages = [
    {
        'role': 'system',      # System instructions
        'content': 'You are a helpful assistant.'
    },
    {
        'role': 'user',        # User message
        'content': 'Hello!'
    },
    {
        'role': 'assistant',   # AI response
        'content': 'Hi! How can I help?'
    },
    {
        'role': 'user',        # Follow-up
        'content': 'Tell me a joke.'
    }
]
"""

st.code(message_format, language="python")

# Roles explanation
st.subheader("🎭 Message Roles")

roles = {
    "system": "Sets AI behavior and instructions (optional)",
    "user": "Messages from the human user",
    "assistant": "Messages from the AI assistant"
}

for role, description in roles.items():
    st.write(f"**{role}**: {description}")

# Context management
st.subheader("🧠 Context Management")

context_example = """
# Strategy 1: Keep full history
messages = []  # Keep all messages
# Pros: Full context
# Cons: Can exceed context window, slow

# Strategy 2: Sliding window
messages = messages[-10:]  # Keep last 10 messages
# Pros: Bounded memory
# Cons: Loses older context

# Strategy 3: Summarization
if len(messages) > 20:
    summary = summarize_conversation(messages[:10])
    messages = [
        {'role': 'system', 'content': f'Previous context: {summary}'}
    ] + messages[10:]
# Pros: Maintains key info
# Cons: More complex
"""

st.code(context_example, language="python")

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Context Management:**
- Limit history to prevent context overflow
- Keep only relevant messages for the task
- Use system message to set consistent behavior

**Message Handling:**
- Always maintain proper role alternation
- Don't skip the assistant's responses
- Store messages in order

**Performance:**
- Fewer messages = faster responses
- Consider summarizing old conversations
- Clear irrelevant context when switching topics
""")

# Common patterns
st.subheader("📋 Common Patterns")

patterns = """
# Pattern 1: Chat with system prompt
messages = [
    {'role': 'system', 'content': 'You are a Python expert.'}
]

# User asks questions
messages.append({'role': 'user', 'content': 'How do I use lists?'})
response = ollama.chat(model='phi4-mini', messages=messages)
messages.append(response['message'])

# Pattern 2: Conversation reset
if user_wants_new_topic:
    messages = [
        {'role': 'system', 'content': system_prompt}
    ]  # Clear history, keep system prompt

# Pattern 3: Context injection
messages.append({
    'role': 'system',
    'content': f'Additional context: {external_data}'
})
"""

st.code(patterns, language="python")

# Error handling
st.subheader("⚠️ Error Handling")

error_example = """
try:
    response = ollama.chat(
        model='phi4-mini',
        messages=messages
    )
    messages.append(response['message'])
    
except Exception as e:
    if 'context length' in str(e):
        # Too many messages, trim history
        messages = messages[-5:]
        response = ollama.chat(model='phi4-mini', messages=messages)
    else:
        print(f"Error: {e}")
"""

st.code(error_example, language="python")

# Tips
st.subheader("⚡ Tips")

tips = """
- **Context window**: Most models have 2048-4096 token limit
- **Token counting**: Each message uses tokens (prompt + response)
- **System prompts**: Use for consistent behavior across conversation
- **Message order**: Maintain chronological order
- **Stateless**: Each API call is independent; you manage history
"""

st.code(tips)
