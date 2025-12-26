#!/usr/bin/env python

import streamlit as st
import ollama

st.title("🧠 Lokales LLM mit Ollama")

prompt = st.text_input("Frage eingeben:")

if st.button("Senden") and prompt.strip():
    r = ollama.chat(model="gemma3:1b", messages=[{"role":"user","content":prompt}])

    st.write(r["message"]["content"])