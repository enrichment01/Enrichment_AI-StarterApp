"""
Tag 3: Ollama

Lokale KI-Modelle mit Ollama nutzen
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_streamlit import show_code, add_select_model
from lib.helper_ollama import check_ollama_status, get_available_models

st.set_page_config(
    page_title="Tag 3: Ollama",
    page_icon="🦙",
    layout="wide"
)

st.title("🦙 Tag 3: Ollama")
st.markdown("**Lokale KI-Modelle mit Ollama nutzen**")

# Tabs
TAB_OVERVIEW = "Übersicht"
TAB_SETUP = "Setup"
TAB_MODELS = "Modelle"
TAB_API_BASICS = "API Basics"
TAB_CHAT = "Chat"
TAB_STREAMING = "Streaming"
TAB_INTEGRATION = "Integration"
TAB_EXERCISES = "Übungen"

TAB_NAMES = [
    TAB_OVERVIEW,
    TAB_SETUP,
    TAB_MODELS,
    TAB_API_BASICS,
    TAB_CHAT,
    TAB_STREAMING,
    TAB_INTEGRATION,
    TAB_EXERCISES,
]

tabs = st.tabs(TAB_NAMES)

def get_tab_index(name):
    try:
        return TAB_NAMES.index(name)
    except ValueError:
        return -1

# Tab 1: Übersicht
with tabs[get_tab_index(TAB_OVERVIEW)]:
    st.header("📋 Kursübersicht Tag 3")
    
    st.markdown("""
    ### Lernziele
    Am Ende von Tag 3 können Sie:
    - ✅ Ollama installieren und konfigurieren
    - ✅ KI-Modelle verwalten
    - ✅ Ollama Python API nutzen
    - ✅ Text generieren und chatten
    - ✅ Streamlit mit Ollama verbinden
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Themen
        1. **Was ist Ollama?**
           - Lokale LLMs
           - Vorteile
           - Use Cases
        
        2. **Installation & Setup**
           - Ollama installieren
           - Server starten
           - Status prüfen
        
        3. **Modell-Management**
           - Modelle installieren
           - Modelle auflisten
           - Modelle löschen
        
        4. **Python API**
           - Generate
           - Chat
           - Streaming
           - Embeddings
        """)
    
    with col2:
        st.markdown("""
        ### ⏱️ Zeitplan
        - **09:00 - 10:00**: Installation & Setup
        - **10:00 - 10:15**: Pause
        - **10:15 - 11:30**: Modell-Management
        - **11:30 - 12:00**: API Grundlagen
        - **12:00 - 13:00**: Mittagspause
        - **13:00 - 14:00**: Chat & Streaming
        - **14:00 - 15:00**: Streamlit Integration
        
        ### 🔗 Links
        - [ollama.ai](https://ollama.ai)
        - [Modelle](https://ollama.ai/library)
        - [GitHub](https://github.com/ollama/ollama)
        """)

# Tab 2: Setup
with tabs[get_tab_index(TAB_SETUP)]:
    st.header("1️⃣ Ollama Setup")
    
    st.markdown("""
    ### Was ist Ollama?
    Ollama ermöglicht es, **Large Language Models (LLMs)** lokal auf Ihrem Computer auszuführen.
    
    **Vorteile:**
    - 🔒 **Privatsphäre**: Daten bleiben lokal
    - 💰 **Kostenlos**: Keine API-Kosten
    - ⚡ **Schnell**: Keine Netzwerk-Latenz
    - 🔌 **Offline**: Keine Internetverbindung nötig
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📥 Installation
        
        **macOS:**
        ```bash
        curl https://ollama.ai/install.sh | sh
        ```
        
        **Linux:**
        ```bash
        curl https://ollama.ai/install.sh | sh
        ```
        
        **Windows:**
        Laden Sie den Installer von [ollama.ai](https://ollama.ai) herunter.
        
        ### ✅ Verifizierung
        ```bash
        ollama --version
        ```
        
        ### 🚀 Server starten
        ```bash
        ollama serve
        ```
        Der Server läuft auf `http://localhost:11434`
        """)
    
    with col2:
        st.markdown("""
        ### 🐍 Python SDK installieren
        ```bash
        pip install ollama
        ```
        
        ### 📝 Erster Test
        ```python
        import ollama

        response = ollama.generate(
            model='llama3.2',
            prompt='Hello!'
        )
        print(response['response'])
        ```
        """)
        
        st.divider()
        
        st.markdown("### 🔌 Status prüfen")
        
        if st.button("Ollama Status prüfen", key="check_status"):
            with st.spinner("Prüfe Ollama..."):
                status = check_ollama_status()
                
                if status['status'] == 'success':
                    st.success(f"✅ {status['message']}")
                    st.metric("Installierte Modelle", len(status['models']))
                else:
                    st.error(f"❌ {status['message']}")
                    st.info("Stellen Sie sicher, dass Ollama installiert und gestartet ist.")

# Tab 3: Modelle
with tabs[get_tab_index(TAB_MODELS)]:
    st.header("2️⃣ Modell-Management")
    
    st.markdown("### 📦 Beliebte Modelle")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Allzweck-Modelle:**
        
        | Modell | Größe | Beschreibung |
        |--------|-------|--------------|
        | llama3.2 | 2GB | Schnell, gut für Chat |
        | llama3.1 | 4.7GB | Größer, präziser |
        | mistral | 4GB | Ausgewogen |
        | phi3 | 2GB | Leichtgewicht |
        
        **Spezialisierte Modelle:**
        
        | Modell | Größe | Spezialisierung |
        |--------|-------|-----------------|
        | codellama | 4GB | Programmierung |
        | llava | 4.7GB | Vision (Bilder) |
        | gemma2 | 5GB | Google Modell |
        """)
    
    with col2:
        st.markdown("""
        ### 📥 Modell installieren
        ```bash
        ollama pull llama3.2
        ollama pull mistral
        ollama pull codellama
        ```
        
        ### 📋 Modelle auflisten
        ```bash
        ollama list
        ```
        
        ### 🗑️ Modell löschen
        ```bash
        ollama rm llama3.2
        ```
        
        ### 🧪 Modell testen
        ```bash
        ollama run llama3.2 "Hallo!"
        ```
        """)
    
    st.divider()
    
    st.markdown("### 📊 Ihre Modelle")
    
    if st.button("Modelle neu laden", key="reload_models"):
        st.rerun()
    
    available_models = get_available_models()
    
    if available_models:
        st.success(f"✅ {len(available_models)} Modelle gefunden")
        
        import pandas as pd
        models_list = []
        
        try:
            import ollama
            for model_name in available_models:
                try:
                    info = ollama.show(model_name)
                    size = info.get('size', 0)
                    models_list.append({
                        'Modell': model_name,
                        'Größe': f"{size / (1024**3):.2f} GB" if size > 0 else "N/A"
                    })
                except:
                    models_list.append({
                        'Modell': model_name,
                        'Größe': "N/A"
                    })
            
            if models_list:
                st.dataframe(pd.DataFrame(models_list), use_container_width=True)
        except Exception as e:
            st.error(f"Fehler beim Laden der Modelldetails: {e}")
            # Fallback: Nur Namen anzeigen
            for model in available_models:
                st.write(f"- {model}")
    else:
        st.warning("⚠️ Keine Modelle gefunden")
        st.info("Installieren Sie ein Modell mit `ollama pull llama3.2`")

# Tab 4: API Basics
with tabs[get_tab_index(TAB_API_BASICS)]:
    st.header("3️⃣ Ollama Python API")
    
    st.markdown("### 📝 Generate - Text generieren")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''import ollama

# Einfache Generierung
response = ollama.generate(
    model='llama3.2',
    prompt='Erkläre Python in einem Satz'
)

print(response['response'])

# Mit Optionen
response = ollama.generate(
    model='llama3.2',
    prompt='Schreibe ein Gedicht',
    options={
        'temperature': 0.9,  # Kreativität
        'top_p': 0.9,
        'top_k': 40,
        'num_predict': 200   # Max Tokens
    }
)

print(response['response'])
''', language='python')
    
    with col2:
        st.markdown("**Live Test:**")
        
        available_models = get_available_models()
        
        if available_models:
            gen_model = st.selectbox("Modell:", available_models, key="gen_model")
            gen_prompt = st.text_area(
                "Prompt:",
                "Erkläre Ollama in einem Satz",
                height=100,
                key="gen_prompt"
            )
            
            gen_temp = st.slider("Temperature:", 0.0, 2.0, 0.7, 0.1, key="gen_temp")
            
            if st.button("Generieren", key="gen_button"):
                with st.spinner("Generiere..."):
                    try:
                        import ollama
                        response = ollama.generate(
                            model=gen_model,
                            prompt=gen_prompt,
                            options={'temperature': gen_temp}
                        )
                        st.success("✅ Antwort:")
                        st.write(response['response'])
                    except Exception as e:
                        st.error(f"❌ Fehler: {e}")
        else:
            st.warning("Keine Modelle verfügbar")
    
    st.divider()
    
    st.markdown("### ⚙️ Parameter-Guide")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Temperature**
        - `0.0-0.3`: Faktisch, deterministisch
        - `0.4-0.7`: Ausgewogen (Standard)
        - `0.8-2.0`: Kreativ, variabel
        
        *Für Code: 0.1-0.3*  
        *Für Stories: 0.8-1.5*
        """)
    
    with col2:
        st.markdown("""
        **Top P** (Nucleus Sampling)
        - Werte: `0.0-1.0`
        - Standard: `0.9`
        - Steuert Token-Auswahl
        
        *Höher = mehr Vielfalt*
        """)
    
    with col3:
        st.markdown("""
        **Num Predict**
        - Max. generierte Tokens
        - Standard: variiert
        - Begrenzt Antwortlänge
        
        *100 = kurze Antwort*  
        *1000 = lange Antwort*
        """)

# Tab 5: Chat
with tabs[get_tab_index(TAB_CHAT)]:
    st.header("4️⃣ Chat API")
    
    st.markdown("### 💬 Chat mit Konversations-History")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''import ollama

# Chat mit History
messages = [
    {
        'role': 'system',
        'content': 'Du bist ein hilfreicher Assistent.'
    },
    {
        'role': 'user',
        'content': 'Hallo, wer bist du?'
    }
]

response = ollama.chat(
    model='llama3.2',
    messages=messages
)

# Antwort ausgeben
print(response['message']['content'])

# Antwort zur History hinzufügen
messages.append(response['message'])

# Nächste Frage
messages.append({
    'role': 'user',
    'content': 'Was kannst du?'
})

response = ollama.chat(
    model='llama3.2',
    messages=messages
)
''', language='python')
    
    with col2:
        st.markdown("**Live Chat:**")
        
        available_models = get_available_models()
        
        if available_models:
            chat_model = st.selectbox("Modell:", available_models, key="chat_model")
            
            # System Prompt
            system_prompt = st.text_area(
                "System Prompt:",
                "Du bist ein hilfreicher Assistent.",
                height=80,
                key="system_prompt"
            )
            
            # Chat History
            if 'simple_chat' not in st.session_state:
                st.session_state.simple_chat = []
            
            # Display messages
            for msg in st.session_state.simple_chat:
                role_icon = "👤" if msg["role"] == "user" else "🤖"
                st.markdown(f"{role_icon} **{msg['role'].title()}:** {msg['content']}")
            
            # Input
            chat_input = st.text_input("Nachricht:", key="chat_input")
            
            col_send, col_clear = st.columns(2)
            
            with col_send:
                if st.button("Senden", key="send_btn"):
                    if chat_input:
                        st.session_state.simple_chat.append({
                            "role": "user",
                            "content": chat_input
                        })
                        
                        with st.spinner("Denke nach..."):
                            try:
                                import ollama
                                messages = [{"role": "system", "content": system_prompt}]
                                messages.extend(st.session_state.simple_chat)
                                
                                response = ollama.chat(
                                    model=chat_model,
                                    messages=messages
                                )
                                
                                st.session_state.simple_chat.append({
                                    "role": "assistant",
                                    "content": response['message']['content']
                                })
                                
                                st.rerun()
                            except Exception as e:
                                st.error(f"Fehler: {e}")
            
            with col_clear:
                if st.button("Löschen", key="clear_btn"):
                    st.session_state.simple_chat = []
                    st.rerun()
        else:
            st.warning("Keine Modelle verfügbar")

# Tab 6: Streaming
with tabs[get_tab_index(TAB_STREAMING)]:
    st.header("5️⃣ Streaming")
    
    st.markdown("""
    ### ⚡ Streaming für bessere UX
    Streaming zeigt die Antwort **während der Generierung** - ähnlich wie ChatGPT.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''import ollama

# Streaming mit generate
stream = ollama.generate(
    model='llama3.2',
    prompt='Erzähle eine Geschichte',
    stream=True
)

# Token für Token ausgeben
for chunk in stream:
    if 'response' in chunk:
        print(chunk['response'], end='', flush=True)

print()  # Neue Zeile am Ende

# Streaming mit chat
stream = ollama.chat(
    model='llama3.2',
    messages=[{
        'role': 'user',
        'content': 'Erkläre KI'
    }],
    stream=True
)

for chunk in stream:
    if 'message' in chunk:
        content = chunk['message']['content']
        print(content, end='', flush=True)
''', language='python')
        
        st.divider()
        
        st.markdown("### 🎨 Streamlit Integration")
        st.code('''# Streaming in Streamlit
response_placeholder = st.empty()
full_response = ""

stream = ollama.generate(
    model='llama3.2',
    prompt=prompt,
    stream=True
)

for chunk in stream:
    if 'response' in chunk:
        full_response += chunk['response']
        # Cursor-Animation
        response_placeholder.markdown(full_response + "▌")

# Finales Ergebnis
response_placeholder.markdown(full_response)
''', language='python')
    
    with col2:
        st.markdown("**Live Streaming:**")
        
        available_models = get_available_models()
        
        if available_models:
            stream_model = st.selectbox("Modell:", available_models, key="stream_model")
            stream_prompt = st.text_input(
                "Prompt:",
                "Zähle von 1 bis 10",
                key="stream_prompt"
            )
            
            if st.button("Mit Streaming generieren", key="stream_btn"):
                response_placeholder = st.empty()
                full_response = ""
                
                try:
                    import ollama
                    stream = ollama.generate(
                        model=stream_model,
                        prompt=stream_prompt,
                        stream=True
                    )
                    
                    for chunk in stream:
                        if 'response' in chunk:
                            full_response += chunk['response']
                            response_placeholder.markdown(full_response + "▌")
                    
                    response_placeholder.markdown(full_response)
                    
                except Exception as e:
                    st.error(f"Fehler: {e}")
        else:
            st.warning("Keine Modelle verfügbar")

# Tab 7: Integration
with tabs[get_tab_index(TAB_INTEGRATION)]:
    st.header("6️⃣ Streamlit + Ollama Integration")
    
    st.markdown("### 🎯 Vollständiges Chat-Beispiel")
    
    st.code('''import streamlit as st
import ollama

st.title("🤖 KI Chat-Assistent")

# Sidebar
with st.sidebar:
    st.header("Einstellungen")
    model = st.selectbox("Modell:", ["llama3.2", "mistral"])
    temperature = st.slider("Temperature:", 0.0, 2.0, 0.7, 0.1)

# Chat History
if 'messages' not in st.session_state:
    st.session_state.messages = []

# System Prompt
system_prompt = st.text_area(
    "System Prompt:",
    "Du bist ein hilfreicher Assistent."
)

# Nachrichten anzeigen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input
if prompt := st.chat_input("Nachricht..."):
    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Assistant response mit Streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(st.session_state.messages)
        
        stream = ollama.chat(
            model=model,
            messages=messages,
            stream=True,
            options={'temperature': temperature}
        )
        
        for chunk in stream:
            if 'message' in chunk:
                full_response += chunk['message']['content']
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response
        })

# Clear Button
if st.button("🗑️ Chat löschen"):
    st.session_state.messages = []
    st.rerun()
''', language='python')
    
    st.divider()
    
    st.markdown("### 💡 Best Practices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Performance:**
        - ⚡ Streaming für bessere UX
        - 🎯 Niedrige Temperature für faktische Antworten
        - 🧠 Kleine Modelle (2-4GB) für schnelle Antworten
        - 📦 Große Modelle (7GB+) für komplexe Aufgaben
        """)
    
    with col2:
        st.markdown("""
        **Fehlerbehandlung:**
        - ✅ Ollama Status prüfen
        - 🔄 Try-Except Blöcke
        - 💬 Benutzer-Feedback
        - 🔌 Connection Timeouts
        """)
    
    st.divider()
    
    st.markdown("### 🎯 Übungen")
    
    # Sub-Tabs für jede Übung
    exercise_tabs = st.tabs([
        "📄 Zusammenfassung",
        "🌍 Übersetzer",
        "💻 Code-Erklärer",
        "📖 Story-Generator"
    ])
    
    # Text-Zusammenfassung
    with exercise_tabs[0]:
        st.markdown("""
        ### 📄 Text-Zusammenfassung
        Erstellen Sie ein Tool zur automatischen Text-Zusammenfassung.
        
        **Anforderungen:**
        1. Text-Area für langen Text
        2. Längen-Auswahl (kurz/mittel/lang)
        3. Ollama zur Zusammenfassung nutzen
        4. Wortanzahl vor/nach anzeigen
        """)
        st.markdown("""
        **Erstellen Sie ein Tool zur Text-Zusammenfassung:**
        1. Text-Area für langen Text
        2. Längen-Auswahl (kurz/mittel/lang)
        3. Ollama zur Zusammenfassung nutzen
        4. Wortanzahl vor/nach anzeigen
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Ihre Lösung:**")
            
            available_models = get_available_models()
            
            if available_models:
                summary_text = st.text_area(
                    "Text zum Zusammenfassen:",
                    "Python ist eine interpretierte Hochsprache. Sie wurde von Guido van Rossum entwickelt. Python unterstützt mehrere Programmierparadigmen. Die Sprache ist sehr beliebt für Data Science und Machine Learning.",
                    height=150,
                    key="ex1_text"
                )
                
                summary_length = st.radio(
                    "Länge:",
                    ["Sehr kurz (1 Satz)", "Kurz (2-3 Sätze)", "Mittel (1 Absatz)"],
                    key="ex1_length"
                )
                
                if st.button("Zusammenfassen", key="ex1_btn"):
                    with st.spinner("Fasse zusammen..."):
                        try:
                            import ollama
                            
                            prompt = f"Fasse diesen Text zusammen ({summary_length}): {summary_text}"
                            
                            response = ollama.generate(
                                model=available_models[0],
                                prompt=prompt,
                                options={'temperature': 0.3}
                            )
                            
                            st.success("✅ Zusammenfassung:")
                            st.write(response['response'])
                            
                            col_a, col_b = st.columns(2)
                            col_a.metric("Original", f"{len(summary_text.split())} Wörter")
                            col_b.metric("Zusammenfassung", f"{len(response['response'].split())} Wörter")
                            
                        except Exception as e:
                            st.error(f"❌ Fehler: {e}")
            else:
                st.warning("Keine Modelle verfügbar")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''import streamlit as st
import ollama

text = st.text_area("Text:")
length = st.radio("Länge:", ["Kurz", "Mittel", "Lang"])

if st.button("Zusammenfassen"):
    prompt = f"Fasse zusammen ({length}): {text}"
    
    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
    
    # Statistiken
    original = len(text.split())
    summary = len(response['response'].split())
    st.metric("Reduktion", f"{(1 - summary/original)*100:.0f}%")
''', language='python')
    
    st.divider()
    
    st.markdown("#### Sprach-Übersetzer")
    
    with st.expander("Aufgabe"):
        st.markdown("""
        **Erstellen Sie einen KI-Übersetzer:**
        1. Text-Eingabe
        2. Zielsprache auswählen
        3. Mit Ollama übersetzen
        4. Übersetzung anzeigen
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Ihre Lösung:**")
            
            available_models = get_available_models()
            
            if available_models:
                translate_text = st.text_area(
                    "Text:",
                    "Hello, how are you today?",
                    key="ex2_text"
                )
                
                target_lang = st.selectbox(
                    "Übersetzen nach:",
                    ["Deutsch", "Französisch", "Spanisch", "Italienisch", "Japanisch"],
                    key="ex2_lang"
                )
                
                if st.button("Übersetzen", key="ex2_btn"):
                    with st.spinner("Übersetze..."):
                        try:
                            import ollama
                            
                            prompt = f"Übersetze diesen Text nach {target_lang}: {translate_text}"
                            
                            response = ollama.generate(
                                model=available_models[0],
                                prompt=prompt,
                                options={'temperature': 0.3}
                            )
                            
                            st.success("✅ Übersetzung:")
                            st.write(response['response'])
                            
                        except Exception as e:
                            st.error(f"❌ Fehler: {e}")
            else:
                st.warning("Keine Modelle verfügbar")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''import streamlit as st
import ollama

text = st.text_area("Text zum Übersetzen:")
target = st.selectbox(
    "Zielsprache:",
    ["Deutsch", "Englisch", "Französisch"]
)

if st.button("Übersetzen"):
    prompt = f"Übersetze nach {target}: {text}"
    
    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.success("Übersetzung:")
    st.write(response['response'])
''', language='python')
    
    # Code-Erklärer
    with exercise_tabs[2]:
        st.markdown("""
        ### 💻 Code-Erklärer
        Erstellen Sie einen intelligenten Code-Erklärer.
        
        **Anforderungen:**
        1. Code-Input (Text Area)
        2. Programmiersprache wählen
        3. Ollama zur Erklärung nutzen
        4. Erklärung anzeigen
        """)
        st.markdown("""
        **Erstellen Sie einen Code-Erklärer:**
        1. Code-Input (Text Area)
        2. Programmiersprache wählen
        3. Ollama zur Erklärung nutzen
        4. Erklärung anzeigen
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Ihre Lösung:**")
            
            available_models = get_available_models()
            
            if available_models:
                code_input = st.text_area(
                    "Code:",
                    "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)",
                    height=150,
                    key="ex3_code"
                )
                
                lang = st.selectbox(
                    "Sprache:",
                    ["Python", "JavaScript", "Java", "C++"],
                    key="ex3_lang"
                )
                
                if st.button("Erklären", key="ex3_btn"):
                    with st.spinner("Analysiere Code..."):
                        try:
                            import ollama
                            
                            prompt = f"Erkläre diesen {lang} Code Zeile für Zeile:\n\n{code_input}"
                            
                            response = ollama.generate(
                                model=available_models[0],
                                prompt=prompt,
                                options={'temperature': 0.3}
                            )
                            
                            st.success("✅ Erklärung:")
                            st.write(response['response'])
                            
                        except Exception as e:
                            st.error(f"❌ Fehler: {e}")
            else:
                st.warning("Keine Modelle verfügbar")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''import streamlit as st
import ollama

code = st.text_area("Code:")
lang = st.selectbox("Sprache:", ["Python", "JavaScript"])

if st.button("Erklären"):
    prompt = f"Erkläre diesen {lang} Code:\\n\\n{code}"
    
    response = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
''', language='python')
    
    # Kreativ-Story-Generator
    with exercise_tabs[3]:
        st.markdown("""
        ### 📖 Kreativ-Story-Generator
        Erstellen Sie einen kreativen Story-Generator mit KI.
        
        **Anforderungen:**
        1. Genre auswählen
        2. Protagonist eingeben
        3. Setting auswählen
        4. Story-Länge wählen
        5. Mit Ollama kreative Geschichte generieren
        6. Streaming für bessere UX
        """)
        st.markdown("""
        **Erstellen Sie einen kreativen Story-Generator:**
        1. Genre auswählen
        2. Protagonist eingeben
        3. Setting auswählen
        4. Story-Länge wählen
        5. Mit Ollama kreative Geschichte generieren
        6. Streaming für bessere UX
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Ihre Lösung:**")
            
            available_models = get_available_models()
            
            if available_models:
                genre = st.selectbox(
                    "Genre:",
                    ["Science Fiction", "Fantasy", "Krimi", "Romance", "Abenteuer", "Horror"],
                    key="ex4_genre"
                )
                
                protagonist = st.text_input(
                    "Protagonist:",
                    "Alex",
                    key="ex4_protagonist"
                )
                
                setting = st.selectbox(
                    "Setting:",
                    ["Eine futuristische Stadt", "Ein magischer Wald", "Eine einsame Insel", 
                     "Eine Raumstation", "Ein altes Schloss"],
                    key="ex4_setting"
                )
                
                length = st.radio(
                    "Story-Länge:",
                    ["Kurz (100 Wörter)", "Mittel (300 Wörter)", "Lang (500 Wörter)"],
                    key="ex4_length"
                )
                
                if st.button("Story generieren", key="ex4_btn"):
                    with st.spinner("Schreibe Story..."):
                        try:
                            import ollama
                            
                            prompt = f"""Schreibe eine {length} {genre}-Geschichte über {protagonist}.
                            
Setting: {setting}
                            
Die Geschichte soll spannend sein und einen überraschenden Twist haben.
Schreibe kreativ und fesselnd!"""
                            
                            st.markdown("---")
                            st.markdown(f"**📖 {genre}-Story: {protagonist}**")
                            
                            response_placeholder = st.empty()
                            full_story = ""
                            
                            stream = ollama.generate(
                                model=available_models[0],
                                prompt=prompt,
                                stream=True,
                                options={'temperature': 0.9}  # Hohe Kreativität
                            )
                            
                            for chunk in stream:
                                if 'response' in chunk:
                                    full_story += chunk['response']
                                    response_placeholder.markdown(full_story + "▌")
                            
                            response_placeholder.markdown(full_story)
                            
                            # Statistiken
                            word_count = len(full_story.split())
                            st.metric("Wörter", word_count)
                            
                            # Download Option
                            st.download_button(
                                "📥 Story herunterladen",
                                full_story,
                                f"story_{protagonist}_{genre}.txt",
                                "text/plain"
                            )
                            
                        except Exception as e:
                            st.error(f"❌ Fehler: {e}")
            else:
                st.warning("Keine Modelle verfügbar")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''import streamlit as st
import ollama

genre = st.selectbox("Genre:", ["Sci-Fi", "Fantasy"])
protagonist = st.text_input("Protagonist:", "Alex")
setting = st.selectbox("Setting:", ["Stadt", "Wald"])
length = st.radio("Länge:", ["Kurz", "Lang"])

if st.button("Story generieren"):
    prompt = f"""Schreibe eine {length} {genre}-Story 
über {protagonist} in {setting}."""    
    
    placeholder = st.empty()
    full_story = ""
    
    # Streaming für bessere UX
    stream = ollama.generate(
        model='llama3.2',
        prompt=prompt,
        stream=True,
        options={'temperature': 0.9}  # Kreativ!
    )
    
    for chunk in stream:
        if 'response' in chunk:
            full_story += chunk['response']
            placeholder.markdown(full_story + "▌")
    
    placeholder.markdown(full_story)
    
    # Download-Option
    st.download_button(
        "📥 Herunterladen",
        full_story,
        "story.txt"
    )
''', language='python')

# Tab 8: Übungen
with tabs[get_tab_index(TAB_EXERCISES)]:
    st.header("7️⃣ Praktische Übungen")
    
    st.markdown("""
    Hier sind 4 praktische Übungen, um Ihr Ollama-Wissen zu festigen.
    Jede Übung enthält eine Aufgabenstellung und eine Lösung.
    """)
    
    # Übungen in Sub-Tabs
    exercise_tabs = st.tabs([
        "Zusammenfassung",
        "Übersetzer",
        "Code-Erklärer",
        "Story-Generator"
    ])
    
    # Text-Zusammenfassung
    with exercise_tabs[0]:
        st.subheader("📝 Text-Zusammenfassung")
        
        st.markdown("""
        **Aufgabe:**
        Erstellen Sie ein Streamlit-Tool, das einen langen Text zusammenfasst.
        
        **Anforderungen:**
        1. Text-Eingabefeld für längeren Text
        2. Auswahl der Zusammenfassungslänge (kurz/mittel/lang)
        3. Button zum Generieren der Zusammenfassung
        4. Anzeige der Zusammenfassung
        5. Bonus: Vergleich Original- vs. Zusammenfassungslänge
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💡 Live-Demo")
            
            # Model selector
            selected_model = add_select_model(key="practice_ex1_model")
            
            # Text input
            ex1_text = st.text_area(
                "Text zum Zusammenfassen:",
                """Künstliche Intelligenz (KI) hat in den letzten Jahren enorme Fortschritte gemacht. 
Maschinelles Lernen, ein Teilbereich der KI, ermöglicht es Computern, aus Daten zu lernen und 
Vorhersagen zu treffen, ohne explizit programmiert zu werden. Deep Learning, eine spezielle Form 
des maschinellen Lernens, verwendet künstliche neuronale Netze mit vielen Schichten. Diese 
Technologie hat Durchbrüche in Bereichen wie Bilderkennung, Sprachverarbeitung und autonomes 
Fahren ermöglicht. Large Language Models wie GPT können natürliche Sprache verstehen und 
generieren. Trotz dieser Fortschritte gibt es auch Herausforderungen: Ethische Fragen, 
Datenschutzbedenken und die Notwendigkeit, KI-Systeme transparent und erklärbar zu machen, 
sind wichtige Themen in der aktuellen Diskussion.""",
                height=200,
                key="practice_ex1_input"
            )
            
            # Length selection
            length = st.radio(
                "Zusammenfassungslänge:",
                ["Kurz (1-2 Sätze)", "Mittel (3-4 Sätze)", "Lang (5+ Sätze)"],
                key="practice_ex1_length"
            )
            
            if st.button("📝 Zusammenfassen", key="practice_ex1_button", type="primary"):
                if ex1_text:
                    length_map = {
                        "Kurz (1-2 Sätze)": "in 1-2 Sätzen",
                        "Mittel (3-4 Sätze)": "in 3-4 Sätzen",
                        "Lang (5+ Sätze)": "in 5 oder mehr Sätzen"
                    }
                    
                    prompt = f"Fasse den folgenden Text {length_map[length]} zusammen:\n\n{ex1_text}"
                    
                    with st.spinner("Zusammenfassung wird erstellt..."):
                        try:
                            import ollama
                            response = ollama.generate(
                                model=selected_model,
                                prompt=prompt,
                                options={'temperature': 0.3}
                            )
                            
                            st.success("✅ Zusammenfassung erstellt!")
                            st.markdown("**Zusammenfassung:**")
                            st.write(response['response'])
                            
                            # Stats
                            with st.expander("📊 Statistiken"):
                                original_words = len(ex1_text.split())
                                summary_words = len(response['response'].split())
                                reduction = ((original_words - summary_words) / original_words) * 100
                                
                                col_a, col_b, col_c = st.columns(3)
                                col_a.metric("Original", f"{original_words} Wörter")
                                col_b.metric("Zusammenfassung", f"{summary_words} Wörter")
                                col_c.metric("Reduktion", f"{reduction:.0f}%")
                        except Exception as e:
                            st.error(f"Fehler: {str(e)}")
                else:
                    st.warning("Bitte geben Sie einen Text ein.")
        
        with col2:
            st.markdown("### 💻 Lösung")
            st.code('''import streamlit as st
import ollama
from lib.helper_streamlit import add_select_model

st.title("Text-Zusammenfassung")

# Model selector
model = add_select_model()

# Text input
text = st.text_area("Text:", height=200)

# Length selection
length = st.radio(
    "Länge:",
    ["Kurz (1-2 Sätze)", "Mittel (3-4 Sätze)", "Lang (5+ Sätze)"]
)

if st.button("Zusammenfassen"):
    length_map = {
        "Kurz (1-2 Sätze)": "in 1-2 Sätzen",
        "Mittel (3-4 Sätze)": "in 3-4 Sätzen",
        "Lang (5+ Sätze)": "in 5 oder mehr Sätzen"
    }
    
    prompt = f"Fasse den folgenden Text {length_map[length]} zusammen:\\n\\n{text}"
    
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={'temperature': 0.3}
    )
    
    st.write(response['response'])
    
    # Statistiken
    original_words = len(text.split())
    summary_words = len(response['response'].split())
    reduction = ((original_words - summary_words) / original_words) * 100
    
    st.metric("Reduktion", f"{reduction:.0f}%")
''', language='python')
    
    # Übersetzer
    with exercise_tabs[1]:
        st.subheader("🌍 Multi-Sprachen-Übersetzer")
        
        st.markdown("""
        **Aufgabe:**
        Erstellen Sie einen Übersetzer, der Text in verschiedene Sprachen übersetzt.
        
        **Anforderungen:**
        1. Text-Eingabefeld
        2. Auswahl der Zielsprache (Englisch, Französisch, Spanisch, Italienisch)
        3. Button zum Übersetzen
        4. Anzeige der Übersetzung
        5. Bonus: Streaming für längere Texte
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💡 Live-Demo")
            
            selected_model = add_select_model(key="practice_ex2_model")
            
            ex2_text = st.text_area(
                "Text zum Übersetzen:",
                "Hallo, wie geht es dir? Ich lerne gerade, wie man Ollama mit Streamlit verwendet.",
                height=100,
                key="practice_ex2_input"
            )
            
            target_lang = st.selectbox(
                "Zielsprache:",
                ["Englisch", "Französisch", "Spanisch", "Italienisch", "Japanisch"],
                key="practice_ex2_lang"
            )
            
            use_streaming = st.checkbox("Streaming verwenden", value=True, key="practice_ex2_stream")
            
            if st.button("🌍 Übersetzen", key="practice_ex2_button", type="primary"):
                if ex2_text:
                    prompt = f"Übersetze den folgenden Text ins {target_lang}e. Gib nur die Übersetzung zurück, ohne zusätzliche Erklärungen:\n\n{ex2_text}"
                    
                    with st.spinner("Übersetzung läuft..."):
                        try:
                            import ollama
                            
                            if use_streaming:
                                st.markdown("**Übersetzung:**")
                                placeholder = st.empty()
                                translation = ""
                                
                                stream = ollama.generate(
                                    model=selected_model,
                                    prompt=prompt,
                                    stream=True
                                )
                                
                                for chunk in stream:
                                    if 'response' in chunk:
                                        translation += chunk['response']
                                        placeholder.markdown(translation + "▌")
                                
                                placeholder.markdown(translation)
                            else:
                                response = ollama.generate(
                                    model=selected_model,
                                    prompt=prompt
                                )
                                st.success("✅ Übersetzung abgeschlossen!")
                                st.markdown("**Übersetzung:**")
                                st.write(response['response'])
                        except Exception as e:
                            st.error(f"Fehler: {str(e)}")
                else:
                    st.warning("Bitte geben Sie einen Text ein.")
        
        with col2:
            st.markdown("### 💻 Lösung")
            st.code('''import streamlit as st
import ollama
from lib.helper_streamlit import add_select_model

st.title("Multi-Sprachen-Übersetzer")

model = add_select_model()

text = st.text_area("Text:", height=100)

target_lang = st.selectbox(
    "Zielsprache:",
    ["Englisch", "Französisch", "Spanisch", "Italienisch"]
)

use_streaming = st.checkbox("Streaming", value=True)

if st.button("Übersetzen"):
    prompt = f"Übersetze den folgenden Text ins {target_lang}e:\\n\\n{text}"
    
    if use_streaming:
        placeholder = st.empty()
        translation = ""
        
        stream = ollama.generate(
            model=model,
            prompt=prompt,
            stream=True
        )
        
        for chunk in stream:
            if 'response' in chunk:
                translation += chunk['response']
                placeholder.markdown(translation + "▌")
        
        placeholder.markdown(translation)
    else:
        response = ollama.generate(model=model, prompt=prompt)
        st.write(response['response'])
''', language='python')
    
    # Code-Erklärer
    with exercise_tabs[2]:
        st.subheader("💻 Code-Erklärer")
        
        st.markdown("""
        **Aufgabe:**
        Erstellen Sie ein Tool, das Code-Snippets analysiert und erklärt.
        
        **Anforderungen:**
        1. Code-Eingabefeld (mit Syntax-Highlighting)
        2. Auswahl der Programmiersprache
        3. Erklärungs-Level (Anfänger/Fortgeschritten/Experte)
        4. Button zum Analysieren
        5. Strukturierte Ausgabe der Erklärung
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💡 Live-Demo")
            
            selected_model = add_select_model(key="practice_ex3_model")
            
            prog_lang = st.selectbox(
                "Programmiersprache:",
                ["Python", "JavaScript", "Java", "C++", "SQL"],
                key="practice_ex3_lang"
            )
            
            ex3_code = st.text_area(
                "Code-Snippet:",
                '''def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(f"Fibonacci(10) = {result}")''',
                height=150,
                key="practice_ex3_input"
            )
            
            level = st.radio(
                "Erklärungs-Level:",
                ["Anfänger", "Fortgeschritten", "Experte"],
                key="practice_ex3_level"
            )
            
            if st.button("💡 Code erklären", key="practice_ex3_button", type="primary"):
                if ex3_code:
                    prompt = f"""Erkläre den folgenden {prog_lang}-Code für einen {level}. 
Strukturiere die Erklärung wie folgt:
1. Was macht der Code? (Kurze Zusammenfassung)
2. Schritt-für-Schritt Erklärung
3. Wichtige Konzepte
4. Mögliche Verbesserungen

Code:
{ex3_code}"""
                    
                    with st.spinner("Code wird analysiert..."):
                        try:
                            import ollama
                            response = ollama.generate(
                                model=selected_model,
                                prompt=prompt,
                                options={'temperature': 0.4}
                            )
                            
                            st.success("✅ Analyse abgeschlossen!")
                            st.markdown("**Code-Erklärung:**")
                            st.markdown(response['response'])
                        except Exception as e:
                            st.error(f"Fehler: {str(e)}")
                else:
                    st.warning("Bitte geben Sie ein Code-Snippet ein.")
        
        with col2:
            st.markdown("### 💻 Lösung")
            st.code('''import streamlit as st
import ollama
from lib.helper_streamlit import add_select_model

st.title("Code-Erklärer")

model = add_select_model()

prog_lang = st.selectbox(
    "Sprache:",
    ["Python", "JavaScript", "Java", "C++"]
)

code = st.text_area("Code:", height=150)

level = st.radio(
    "Erklärungs-Level:",
    ["Anfänger", "Fortgeschritten", "Experte"]
)

if st.button("Code erklären"):
    prompt = f"""Erkläre den folgenden {prog_lang}-Code 
für einen {level}. Strukturiere die Erklärung:
1. Was macht der Code?
2. Schritt-für-Schritt Erklärung
3. Wichtige Konzepte
4. Verbesserungen

Code:
{code}"""
    
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={'temperature': 0.4}
    )
    
    st.markdown(response['response'])
''', language='python')
    
    # Story-Generator
    with exercise_tabs[3]:
        st.subheader("📚 Kreativer Story-Generator")
        
        st.markdown("""
        **Aufgabe:**
        Erstellen Sie einen kreativen Story-Generator mit Streaming.
        
        **Anforderungen:**
        1. Eingabefelder für Genre, Hauptcharakter, Setting
        2. Slider für Story-Länge
        3. Temperature-Slider für Kreativität
        4. Streaming-Ausgabe der Geschichte
        5. Download-Button für die fertige Story
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💡 Live-Demo")
            
            selected_model = add_select_model(key="practice_ex4_model")
            
            col_a, col_b = st.columns(2)
            with col_a:
                genre = st.selectbox(
                    "Genre:",
                    ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror", "Abenteuer"],
                    key="practice_ex4_genre"
                )
            with col_b:
                length = st.select_slider(
                    "Story-Länge:",
                    ["Kurz", "Mittel", "Lang"],
                    value="Mittel",
                    key="practice_ex4_length"
                )
            
            character = st.text_input(
                "Hauptcharakter:",
                "Ein mutiger Astronaut",
                key="practice_ex4_char"
            )
            
            setting = st.text_input(
                "Setting/Ort:",
                "Auf einem fernen Planeten",
                key="practice_ex4_setting"
            )
            
            temperature = st.slider(
                "Kreativität (Temperature):",
                0.0, 2.0, 0.9, 0.1,
                key="practice_ex4_temp"
            )
            
            if st.button("📚 Story generieren", key="practice_ex4_button", type="primary"):
                length_map = {
                    "Kurz": "eine kurze Geschichte (ca. 100-150 Wörter)",
                    "Mittel": "eine mittellange Geschichte (ca. 200-300 Wörter)",
                    "Lang": "eine längere Geschichte (ca. 400-500 Wörter)"
                }
                
                prompt = f"""Schreibe {length_map[length]} im {genre}-Genre.

Hauptcharakter: {character}
Setting: {setting}

Die Geschichte sollte spannend sein und eine klare Struktur haben (Anfang, Konflikt, Lösung)."""
                
                with st.spinner("Story wird generiert..."):
                    try:
                        import ollama
                        
                        st.markdown("### 📖 Deine Story:")
                        st.markdown("---")
                        
                        placeholder = st.empty()
                        full_story = ""
                        
                        stream = ollama.generate(
                            model=selected_model,
                            prompt=prompt,
                            options={'temperature': temperature},
                            stream=True
                        )
                        
                        for chunk in stream:
                            if 'response' in chunk:
                                full_story += chunk['response']
                                placeholder.markdown(full_story + "▌")
                        
                        placeholder.markdown(full_story)
                        
                        st.markdown("---")
                        st.success("✅ Story abgeschlossen!")
                        
                        # Download
                        st.download_button(
                            "📥 Story herunterladen",
                            full_story,
                            f"story_{genre.lower()}.txt",
                            "text/plain"
                        )
                        
                        # Stats
                        word_count = len(full_story.split())
                        st.info(f"📊 Wortanzahl: {word_count} Wörter")
                    except Exception as e:
                        st.error(f"Fehler: {str(e)}")
        
        with col2:
            st.markdown("### 💻 Lösung")
            st.code('''import streamlit as st
import ollama
from lib.helper_streamlit import add_select_model

st.title("Story-Generator")

model = add_select_model()

genre = st.selectbox(
    "Genre:",
    ["Fantasy", "Sci-Fi", "Mystery", "Romance"]
)

length = st.select_slider(
    "Länge:",
    ["Kurz", "Mittel", "Lang"]
)

character = st.text_input("Hauptcharakter:", "Ein mutiger Held")
setting = st.text_input("Setting:", "In einem magischen Wald")

temperature = st.slider("Kreativität:", 0.0, 2.0, 0.9)

if st.button("Story generieren"):
    length_map = {
        "Kurz": "eine kurze Geschichte (100-150 Wörter)",
        "Mittel": "eine mittellange Geschichte (200-300 Wörter)",
        "Lang": "eine längere Geschichte (400-500 Wörter)"
    }
    
    prompt = f"""Schreibe {length_map[length]} im {genre}-Genre.
    
    Hauptcharakter: {character}
    Setting: {setting}
    
    Mit klarer Struktur (Anfang, Konflikt, Lösung)."""
    
    placeholder = st.empty()
    full_story = ""
    
    stream = ollama.generate(
        model=model,
        prompt=prompt,
        options={'temperature': temperature},
        stream=True
    )
    
    for chunk in stream:
        if 'response' in chunk:
            full_story += chunk['response']
            placeholder.markdown(full_story + "▌")
    
    placeholder.markdown(full_story)
    
    # Download
    st.download_button(
        "Herunterladen",
        full_story,
        f"story_{genre}.txt"
    )
''', language='python')
    
    # Tipps und Zusammenfassung
    st.divider()
    st.markdown("""
    ### 🎯 Übungsziele erreicht?
    
    Nach diesen Übungen sollten Sie:
    - ✅ Ollama für verschiedene Aufgaben einsetzen können
    - ✅ Prompts effektiv gestalten können
    - ✅ Streaming-Responses implementieren können
    - ✅ Parameter wie Temperature richtig nutzen können
    - ✅ Ollama mit Streamlit integrieren können
    
    ### 💡 Tipps für eigene Projekte:
    1. **Klare Prompts**: Je spezifischer, desto besser die Ergebnisse
    2. **Temperature**: 0.0-0.3 für faktische, 0.7-1.5 für kreative Aufgaben
    3. **Streaming**: Verbessert UX bei längeren Antworten
    4. **Error Handling**: Immer try-except für API-Calls verwenden
    5. **Model Selection**: Größere Modelle ≠ immer besser für alle Aufgaben
    """)

# Zusammenfassung
st.divider()
st.header("📚 Zusammenfassung Tag 3")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ✅ Gelernt
    - Ollama installieren
    - Modelle verwalten
    - Python API nutzen
    - Chat erstellen
    - Streaming implementieren
    """)

with col2:
    st.markdown("""
    ### 🎯 Key Methods
    - `ollama.generate()` - Text generieren
    - `ollama.chat()` - Chat mit History
    - `stream=True` - Streaming
    - `options={}` - Parameter
    - System Prompts
    """)

with col3:
    st.markdown("""
    ### 🚀 Tag 4
    - Vollständige Apps
    - Chat-Interfaces
    - Text-Generator
    - Code-Assistent
    - Best Practices
    """)

# =================================================================================================
show_code(__file__)
