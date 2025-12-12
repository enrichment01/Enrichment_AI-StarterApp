#!/usr/bin/env streamlit run

import streamlit as st
import requests

st.title("🧠 Lokales LLM mit Ollama")

prompt = st.text_input("Frage eingeben:")

if st.button("Senden") and prompt.strip():
    try:
        with st.spinner("Warte auf Antwort..."):
            response = requests.post(
                  "http://localhost:11434/api/generate",
                  json={
                     "model": "phi4-mini",
                     "prompt": prompt,
                     "stream": False
                  },
                  timeout=600
            )
      
            if response.status_code != 200:
                  st.error(f"Fehler: {response.status_code} - {response.text}")
            else:
                  data = response.json()
                  antwort = data.get("response") or data.get("message") or "Keine Antwort erhalten."
                  st.success("Antwort vom Modell:")
                  st.write(antwort)
    except Exception as e:
        st.error(f"Fehler: {e}")