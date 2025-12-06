import streamlit as st

st.header("📏 Context Window Management — Ollama Basics")
st.markdown("Managing token limits and context in long conversations.")

# Overview
st.subheader("What is a Context Window?")

st.write("""
The context window is the maximum number of tokens (words and characters) 
that a language model can process at once. This includes both the input 
(prompt + history) and the output (response).
""")

# Model context limits
st.subheader("📊 Model Context Limits")

models = {
    "phi4-mini": "4096 tokens (~3000 words)",
    "mistral": "8192 tokens (~6000 words)",
    "codellama": "16384 tokens (~12000 words)",
    "llama3": "8192 tokens (~6000 words)"
}

for model, limit in models.items():
    st.write(f"**{model}**: {limit}")

# Token counting
st.subheader("🔢 Understanding Tokens")

st.write("**Approximate token counts:**")
token_examples = {
    "1 token ≈": "4 characters or ¾ of a word",
    "100 tokens ≈": "75 words",
    "1000 tokens ≈": "750 words",
    "2000 tokens ≈": "1500 words (3-4 pages)"
}

for tokens, equiv in token_examples.items():
    st.write(f"- {tokens} {equiv}")

# Calculating usage
st.subheader("💭 Calculating Token Usage")

usage_example = """
# Total tokens used per request:
# Input tokens = System prompt + All messages in history
# Output tokens = AI response
# Total = Input + Output

messages = [
    {'role': 'system', 'content': '...'},      # ~50 tokens
    {'role': 'user', 'content': '...'},        # ~20 tokens
    {'role': 'assistant', 'content': '...'},   # ~100 tokens
    {'role': 'user', 'content': '...'},        # ~30 tokens
]

# Input: ~200 tokens
# Expected output: ~150 tokens
# Total: ~350 tokens
# Remaining: 4096 - 350 = 3746 tokens available
"""

st.code(usage_example, language="python")

# Strategies
st.subheader("🎯 Context Management Strategies")

st.write("**1. Fixed Window (Keep Last N Messages)**")
strategy1 = """
# Keep only last 10 messages
MAX_MESSAGES = 10

messages.append({'role': 'user', 'content': user_input})
messages = messages[-MAX_MESSAGES:]  # Trim to last N

response = ollama.chat(model='phi4-mini', messages=messages)
"""
st.code(strategy1, language="python")

st.write("**2. Token-Based Truncation**")
strategy2 = """
def estimate_tokens(text):
    # Rough estimate: 1 token ≈ 4 characters
    return len(text) // 4

def trim_messages(messages, max_tokens=3000):
    total = 0
    trimmed = []
    
    # Keep messages from most recent backwards
    for msg in reversed(messages):
        tokens = estimate_tokens(msg['content'])
        if total + tokens <= max_tokens:
            trimmed.insert(0, msg)
            total += tokens
        else:
            break
    
    return trimmed

messages = trim_messages(messages, max_tokens=3000)
"""
st.code(strategy2, language="python")

st.write("**3. Summarization**")
strategy3 = """
def summarize_history(messages):
    # Create summary of old messages
    old_messages = messages[:-5]  # All but last 5
    
    summary_prompt = {
        'role': 'system',
        'content': f'Summarize this conversation: {old_messages}'
    }
    
    summary = ollama.chat(
        model='phi4-mini',
        messages=[summary_prompt]
    )
    
    # Replace old messages with summary
    return [
        {'role': 'system', 'content': summary['message']['content']},
        *messages[-5:]  # Keep recent messages
    ]

if len(messages) > 15:
    messages = summarize_history(messages)
"""
st.code(strategy3, language="python")

st.write("**4. Conversation Splitting**")
strategy4 = """
# Split conversation when topic changes
if user_starts_new_topic:
    # Save old conversation
    old_conversation = messages.copy()
    
    # Start fresh
    messages = [
        {'role': 'system', 'content': system_prompt}
    ]
    
    st.info("Started new conversation")
"""
st.code(strategy4, language="python")

# Interactive demo
st.subheader("🎮 Token Counter Demo")

sample_text = st.text_area(
    "Enter text to estimate tokens:",
    "The quick brown fox jumps over the lazy dog.",
    height=100
)

if sample_text:
    # Rough estimation: 1 token ≈ 4 characters
    estimated_tokens = len(sample_text) // 4
    words = len(sample_text.split())
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Characters", len(sample_text))
    col2.metric("Words", words)
    col3.metric("Est. Tokens", estimated_tokens)
    
    # Calculate percentage of different model limits
    st.write("**Percentage of model context windows:**")
    for model, limit in {"phi4-mini": 4096, "mistral": 8192}.items():
        limit_num = int(limit)
        percentage = (estimated_tokens / limit_num) * 100
        st.progress(min(percentage / 100, 1.0), text=f"{model}: {percentage:.1f}%")

# Warning signs
st.subheader("⚠️ Context Overflow Warning Signs")

warnings = """
Common errors when context is too large:

1. "context length exceeded" error
2. Truncated responses
3. Model ignores early messages
4. Slower response times
5. Incomplete or nonsensical answers

Solutions:
- Trim message history
- Use shorter system prompts
- Implement sliding window
- Summarize old context
"""

st.code(warnings)

# Best practices
st.subheader("💡 Best Practices")

st.info("""
**Efficient Context Usage:**
- Keep system prompts concise (< 100 tokens)
- Remove formatting/whitespace from messages
- Prioritize recent messages over old ones
- Clear context when switching topics

**Monitoring:**
- Track approximate token usage
- Log when trimming occurs
- Monitor response quality degradation

**User Experience:**
- Inform users when history is cleared
- Provide "New conversation" button
- Show context usage indicator
""")

# Advanced pattern
st.subheader("📋 Advanced: Hybrid Approach")

hybrid = """
class ConversationManager:
    def __init__(self, max_tokens=3000):
        self.messages = []
        self.max_tokens = max_tokens
        self.system_prompt = None
    
    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})
        self._manage_context()
    
    def _estimate_tokens(self, messages):
        return sum(len(m['content']) // 4 for m in messages)
    
    def _manage_context(self):
        while self._estimate_tokens(self.messages) > self.max_tokens:
            if len(self.messages) > 5:
                # Remove oldest non-system message
                for i, msg in enumerate(self.messages):
                    if msg['role'] != 'system':
                        self.messages.pop(i)
                        break
            else:
                break
    
    def get_messages(self):
        if self.system_prompt:
            return [self.system_prompt] + self.messages
        return self.messages

# Usage
manager = ConversationManager(max_tokens=3000)
manager.system_prompt = {'role': 'system', 'content': 'Be helpful'}
manager.add_message('user', 'Hello')
messages = manager.get_messages()
"""

st.code(hybrid, language="python")

# Tips
st.subheader("⚡ Quick Tips")

st.success("""
- Start with simple fixed window (last 10-20 messages)
- Monitor and adjust based on your use case
- Longer context ≠ better responses always
- Focus on relevant, recent context
- Test with your specific model and prompts
""")
