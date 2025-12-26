import streamlit as st
import ollama

st.title("Ollama streaming demo")

prompt = st.text_input("Prompt", "Tell me a story")

if st.button("Generate"):
    placeholder = st.empty()
    full_text = ""

    try:
        stream = ollama.chat(
            model="gemma3:1b",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        for chunk in stream:
            token = ""
            if "message" in chunk and chunk["message"] and "content" in chunk["message"]:
                token = chunk["message"]["content"] or ""
            elif "delta" in chunk and chunk["delta"] and "content" in chunk["delta"]:
                token = chunk["delta"]["content"] or ""

            if token:
                full_text += token
                placeholder.markdown(full_text)

        st.success("Done")

    except Exception as e:
        st.error(f"Error: {e}")
