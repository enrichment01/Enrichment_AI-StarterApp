"""
Tag 3: Streamlit Ollama Apps

Entwicklung vollständiger KI-Anwendungen
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_streamlit import show_code, add_select_model
from lib.helper_ollama import get_available_models
import ollama

st.set_page_config(
    page_title="Tag 3: Streamlit Ollama Apps",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Tag 3: Streamlit Ollama Apps")
st.markdown("**Entwicklung vollständiger KI-Anwendungen**")

# Sidebar
with st.sidebar:
    st.header("⚙️ Konfiguration")
    selected_model = add_select_model()
    
    st.divider()
    
    temperature = st.slider("Temperature:", 0.0, 2.0, 0.7, 0.1)
    max_tokens = st.number_input("Max Tokens:", 50, 2000, 500, 50)

# Tabs
TAB_OVERVIEW = "Übersicht"
TAB_CHAT_APP = "Chat-App"
TAB_TEXT_GENERATOR = "Text-Generator"
TAB_CODE_ASSISTANT = "Code-Assistent"
TAB_SUMMARY_TOOL = "Zusammenfassung-Tool"
TAB_MULTI_MODEL = "Multi-Model"
TAB_BEST_PRACTICES = "Best Practices"

TAB_NAMES = [
    TAB_OVERVIEW,
    TAB_CHAT_APP,
    TAB_TEXT_GENERATOR,
    TAB_CODE_ASSISTANT,
    TAB_SUMMARY_TOOL,
    TAB_MULTI_MODEL,
    TAB_BEST_PRACTICES,
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
    - ✅ Vollständige Chat-Anwendungen erstellen
    - ✅ Streaming-Responses implementieren
    - ✅ Verschiedene App-Typen entwickeln
    - ✅ Multi-Model-Vergleiche durchführen
    - ✅ Best Practices anwenden
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Projekte
        1. **Chat-App** - Interaktiver Assistent
        2. **Text-Generator** - Kreative Inhalte
        3. **Code-Assistent** - Programmierhilfe
        4. **Zusammenfassung** - Text-Analyse
        5. **Multi-Model** - Modellvergleich
        """)
    
    with col2:
        st.markdown("""
        ### ⏱️ Zeitplan
        - **09:00 - 10:30**: Chat-App
        - **10:30 - 10:45**: Pause
        - **10:45 - 12:00**: Generator & Code
        - **12:00 - 13:00**: Mittagspause
        - **13:00 - 14:30**: Tools & Vergleich
        - **14:30 - 15:00**: Best Practices
        """)

# Tab 2: Chat-App
with tabs[get_tab_index(TAB_CHAT_APP)]:
    st.header("💬 Chat-App mit History")
    
    st.markdown("""
    ### Vollständige Chat-Anwendung
    Eine professionelle Chat-App mit Nachrichtenverlauf, System-Prompts und Streaming.
    """)
    
    # System Prompt
    system_prompt = st.text_area(
        "System Prompt:",
        "Du bist ein hilfreicher KI-Assistent, der präzise und freundliche Antworten gibt.",
        height=100,
        key="chat_system"
    )
    
    # Chat History initialisieren
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    
    # Nachrichten anzeigen
    st.markdown("### 💬 Konversation")
    
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Chat Input
    if prompt := st.chat_input("Ihre Nachricht..."):
        # User message hinzufügen und anzeigen
        st.session_state.chat_messages.append({
            "role": "user",
            "content": prompt
        })
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Assistant response mit Streaming
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Messages für API vorbereiten
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(st.session_state.chat_messages)
                
                # Streaming Response
                stream = ollama.chat(
                    model=selected_model,
                    messages=messages,
                    stream=True,
                    options={
                        'temperature': temperature,
                        'num_predict': max_tokens
                    }
                )
                
                for chunk in stream:
                    if 'message' in chunk and 'content' in chunk['message']:
                        full_response += chunk['message']['content']
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # Response zur History hinzufügen
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
            except Exception as e:
                st.error(f"❌ Fehler: {e}")
    
    # Controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🗑️ Chat löschen", key="clear_chat"):
            st.session_state.chat_messages = []
            st.rerun()
    
    with col2:
        if st.button("💾 Exportieren", key="export_chat"):
            if st.session_state.chat_messages:
                import json
                chat_export = json.dumps(st.session_state.chat_messages, indent=2, ensure_ascii=False)
                st.download_button(
                    "📥 Download JSON",
                    chat_export,
                    "chat_export.json",
                    "application/json"
                )
    
    with col3:
        msg_count = len(st.session_state.chat_messages)
        st.metric("Nachrichten", msg_count)

# Tab 3: Text-Generator
with tabs[get_tab_index(TAB_TEXT_GENERATOR)]:
    st.header("✍️ Text-Generator")
    
    st.markdown("### Kreative Texte generieren")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("⚙️ Einstellungen")
        
        text_type = st.selectbox(
            "Text-Art:",
            ["Blog-Post", "Geschichte", "Gedicht", "Email", "Produktbeschreibung", "Social Media"],
            key="text_type"
        )
        
        text_topic = st.text_input(
            "Thema:",
            "Künstliche Intelligenz",
            key="text_topic"
        )
        
        text_length = st.select_slider(
            "Länge:",
            options=["Kurz", "Mittel", "Lang"],
            value="Mittel",
            key="text_length"
        )
        
        text_tone = st.selectbox(
            "Ton:",
            ["Professionell", "Freundlich", "Formal", "Humorvoll", "Informativ"],
            key="text_tone"
        )
        
        additional_instructions = st.text_area(
            "Zusätzliche Anweisungen:",
            placeholder="z.B. 'Verwende einfache Sprache' oder 'Füge Beispiele hinzu'",
            height=100,
            key="additional_instr"
        )
        
        if st.button("✨ Generieren", type="primary", key="generate_text"):
            # Prompt zusammenstellen
            length_map = {"Kurz": "kurzen", "Mittel": "mittellangen", "Lang": "langen"}
            
            prompt = f"""Schreibe einen {length_map[text_length]} {text_type} zum Thema: {text_topic}.

Ton: {text_tone}

{f'Zusätzliche Anweisungen: {additional_instructions}' if additional_instructions else ''}

Bitte generiere qualitativ hochwertigen Inhalt."""
            
            with col2:
                st.subheader("📄 Generierter Text")
                
                with st.spinner("Generiere..."):
                    try:
                        response_placeholder = st.empty()
                        full_text = ""
                        
                        stream = ollama.generate(
                            model=selected_model,
                            prompt=prompt,
                            stream=True,
                            options={
                                'temperature': temperature,
                                'num_predict': max_tokens
                            }
                        )
                        
                        for chunk in stream:
                            if 'response' in chunk:
                                full_text += chunk['response']
                                response_placeholder.markdown(full_text + "▌")
                        
                        response_placeholder.markdown(full_text)
                        
                        # Download Button
                        st.download_button(
                            "📥 Text herunterladen",
                            full_text,
                            f"{text_type}_{text_topic}.txt",
                            "text/plain"
                        )
                        
                    except Exception as e:
                        st.error(f"❌ Fehler: {e}")
    
    with col2:
        if 'generate_text' not in st.session_state or not st.session_state.get('generate_text'):
            st.subheader("📄 Generierter Text")
            st.info("👈 Konfigurieren Sie die Einstellungen und klicken Sie auf 'Generieren'")

# Tab 4: Code-Assistent
with tabs[get_tab_index(TAB_CODE_ASSISTANT)]:
    st.header("💻 Code-Assistent")
    
    st.markdown("### Programmierhilfe mit KI")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("🎯 Aufgabe")
        
        code_task = st.selectbox(
            "Was möchten Sie tun?",
            [
                "Code schreiben",
                "Code erklären",
                "Code debuggen",
                "Code optimieren",
                "Tests schreiben"
            ],
            key="code_task"
        )
        
        programming_language = st.selectbox(
            "Programmiersprache:",
            ["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
            key="prog_lang"
        )
        
        if code_task == "Code schreiben":
            code_description = st.text_area(
                "Beschreiben Sie, was der Code tun soll:",
                "Eine Funktion, die eine Liste von Zahlen sortiert",
                height=100,
                key="code_desc"
            )
            user_code = None
        else:
            code_description = st.text_area(
                "Zusätzliche Informationen:",
                height=50,
                key="code_info"
            )
            user_code = st.text_area(
                "Ihr Code:",
                height=200,
                key="user_code"
            )
        
        if st.button("🚀 Ausführen", type="primary", key="run_code_assistant"):
            with col2:
                st.subheader("💡 Ergebnis")
                
                # Prompt je nach Task
                task_prompts = {
                    "Code schreiben": f"Schreibe {programming_language} Code für: {code_description}. Füge Kommentare hinzu.",
                    "Code erklären": f"Erkläre diesen {programming_language} Code:\n\n{user_code}",
                    "Code debuggen": f"Finde und behebe Fehler in diesem {programming_language} Code:\n\n{user_code}\n\nZusätzliche Info: {code_description}",
                    "Code optimieren": f"Optimiere diesen {programming_language} Code:\n\n{user_code}\n\nZiel: {code_description}",
                    "Tests schreiben": f"Schreibe Unit-Tests für diesen {programming_language} Code:\n\n{user_code}"
                }
                
                prompt = task_prompts[code_task]
                
                with st.spinner("Verarbeite..."):
                    try:
                        response_placeholder = st.empty()
                        full_response = ""
                        
                        stream = ollama.generate(
                            model=selected_model,
                            prompt=prompt,
                            stream=True,
                            options={'temperature': 0.3}  # Niedrigere Temp für Code
                        )
                        
                        for chunk in stream:
                            if 'response' in chunk:
                                full_response += chunk['response']
                                response_placeholder.markdown(full_response + "▌")
                        
                        response_placeholder.markdown(full_response)
                        
                    except Exception as e:
                        st.error(f"❌ Fehler: {e}")
    
    with col2:
        if 'run_code_assistant' not in st.session_state or not st.session_state.get('run_code_assistant'):
            st.subheader("💡 Ergebnis")
            st.info("👈 Wählen Sie eine Aufgabe und klicken Sie auf 'Ausführen'")

# Tab 5: Zusammenfassung-Tool
with tabs[get_tab_index(TAB_SUMMARY_TOOL)]:
    st.header("📝 Zusammenfassung-Tool")
    
    st.markdown("### Texte automatisch zusammenfassen")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📄 Eingabe")
        
        input_text = st.text_area(
            "Text zum Zusammenfassen:",
            placeholder="Fügen Sie hier den Text ein, den Sie zusammenfassen möchten...",
            height=300,
            key="summary_input"
        )
        
        summary_length = st.select_slider(
            "Zusammenfassungslänge:",
            options=["Sehr kurz (1-2 Sätze)", "Kurz (3-5 Sätze)", "Mittel (1 Absatz)", "Detailliert (mehrere Absätze)"],
            value="Kurz (3-5 Sätze)",
            key="summary_length"
        )
        
        summary_style = st.selectbox(
            "Stil:",
            ["Bullet Points", "Fließtext", "Strukturiert"],
            key="summary_style"
        )
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("📊 Zusammenfassen", type="primary", key="summarize"):
                if input_text:
                    with col2:
                        st.subheader("📋 Zusammenfassung")
                        
                        prompt = f"""Fasse den folgenden Text zusammen.

Länge: {summary_length}
Stil: {summary_style}

Text:
{input_text}

Zusammenfassung:"""
                        
                        with st.spinner("Fasse zusammen..."):
                            try:
                                response_placeholder = st.empty()
                                full_summary = ""
                                
                                stream = ollama.generate(
                                    model=selected_model,
                                    prompt=prompt,
                                    stream=True,
                                    options={'temperature': 0.3}
                                )
                                
                                for chunk in stream:
                                    if 'response' in chunk:
                                        full_summary += chunk['response']
                                        response_placeholder.markdown(full_summary + "▌")
                                
                                response_placeholder.markdown(full_summary)
                                
                                # Statistiken
                                st.divider()
                                col_i, col_ii, col_iii = st.columns(3)
                                col_i.metric("Original Wörter", len(input_text.split()))
                                col_ii.metric("Zusammenfassung Wörter", len(full_summary.split()))
                                reduction = (1 - len(full_summary.split()) / len(input_text.split())) * 100
                                col_iii.metric("Reduktion", f"{reduction:.1f}%")
                                
                            except Exception as e:
                                st.error(f"❌ Fehler: {e}")
                else:
                    st.warning("Bitte geben Sie einen Text ein.")
        
        with col_b:
            if st.button("🔄 Beispieltext laden", key="load_example"):
                st.session_state.summary_input = """Python ist eine interpretierte, objektorientierte Programmiersprache mit dynamischer Semantik. 
Ihre high-level eingebauten Datenstrukturen, kombiniert mit dynamischer Typisierung und dynamischem Binding, machen sie sehr attraktiv für Rapid Application Development, 
sowie für die Verwendung als Scripting- oder Glue-Language, um bestehende Komponenten miteinander zu verbinden. Pythons einfache, leicht zu erlernende Syntax betont 
Lesbarkeit und reduziert daher die Kosten für Programm-Wartung. Python unterstützt Module und Pakete, was Modularität und Code-Wiederverwendung fördert."""
                st.rerun()
    
    with col2:
        if 'summarize' not in st.session_state or not st.session_state.get('summarize'):
            st.subheader("📋 Zusammenfassung")
            st.info("👈 Geben Sie einen Text ein und klicken Sie auf 'Zusammenfassen'")

# Tab 6: Multi-Model Vergleich
with tabs[get_tab_index(TAB_MULTI_MODEL)]:
    st.header("🔬 Multi-Model Vergleich")
    
    st.markdown("### Verschiedene Modelle vergleichen")
    
    available_models = get_available_models()
    
    if len(available_models) >= 2:
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("⚙️ Konfiguration")
            
            model1 = st.selectbox("Modell 1:", available_models, key="model1")
            model2 = st.selectbox("Modell 2:", available_models, key="model2", index=1 if len(available_models) > 1 else 0)
            
            compare_prompt = st.text_area(
                "Prompt:",
                "Erkläre Machine Learning in einfachen Worten.",
                height=100,
                key="compare_prompt"
            )
            
            if st.button("⚡ Vergleichen", type="primary", key="compare_models"):
                with col2:
                    st.subheader("📊 Ergebnisse")
                    
                    col_a, col_b = st.columns(2)
                    
                    # Modell 1
                    with col_a:
                        st.markdown(f"**{model1}**")
                        
                        with st.spinner(f"Generiere mit {model1}..."):
                            try:
                                import time
                                start_time = time.time()
                                
                                response1 = ollama.generate(
                                    model=model1,
                                    prompt=compare_prompt,
                                    options={'temperature': temperature}
                                )
                                
                                duration1 = time.time() - start_time
                                
                                st.markdown(response1['response'])
                                st.caption(f"⏱️ {duration1:.2f}s")
                                
                            except Exception as e:
                                st.error(f"Fehler: {e}")
                    
                    # Modell 2
                    with col_b:
                        st.markdown(f"**{model2}**")
                        
                        with st.spinner(f"Generiere mit {model2}..."):
                            try:
                                import time
                                start_time = time.time()
                                
                                response2 = ollama.generate(
                                    model=model2,
                                    prompt=compare_prompt,
                                    options={'temperature': temperature}
                                )
                                
                                duration2 = time.time() - start_time
                                
                                st.markdown(response2['response'])
                                st.caption(f"⏱️ {duration2:.2f}s")
                                
                            except Exception as e:
                                st.error(f"Fehler: {e}")
        
        with col2:
            if 'compare_models' not in st.session_state or not st.session_state.get('compare_models'):
                st.subheader("📊 Ergebnisse")
                st.info("👈 Wählen Sie zwei Modelle und klicken Sie auf 'Vergleichen'")
    
    else:
        st.warning("⚠️ Mindestens 2 Modelle erforderlich für Vergleich")
        st.info("Installieren Sie weitere Modelle mit `ollama pull <model-name>`")

# Tab 7: Best Practices
with tabs[get_tab_index(TAB_BEST_PRACTICES)]:
    st.header("✨ Best Practices")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 UI/UX Best Practices
        
        **1. Streaming verwenden**
        ```python
        # Besser: Mit Streaming
        stream = ollama.generate(..., stream=True)
        for chunk in stream:
            # Update UI progressiv
        ```
        
        **2. Ladeanzeigen**
        ```python
        with st.spinner("Generiere..."):
            response = ollama.generate(...)
        ```
        
        **3. Fehlerbehandlung**
        ```python
        try:
            response = ollama.generate(...)
        except Exception as e:
            st.error(f"Fehler: {e}")
            # Fallback-Option anbieten
        ```
        
        **4. Session State**
        ```python
        if 'history' not in st.session_state:
            st.session_state.history = []
        ```
        
        **5. Feedback geben**
        ```python
        st.success("✅ Erfolgreich!")
        st.info("ℹ️ Hinweis: ...")
        st.warning("⚠️ Achtung!")
        ```
        """)
    
    with col2:
        st.markdown("""
        ### ⚙️ Performance Best Practices
        
        **1. Optimale Parameter**
        - Temperature: 0.1-0.3 für faktische Antworten
        - Temperature: 0.7-0.9 für kreative Texte
        - Max Tokens begrenzen
        
        **2. Modell-Auswahl**
        - Kleine Modelle (2-4GB) für einfache Tasks
        - Große Modelle (7GB+) für komplexe Aufgaben
        
        **3. Caching**
        ```python
        @st.cache_data
        def get_model_list():
            return ollama.list()
        ```
        
        **4. Kontext-Management**
        - Konversations-History begrenzen
        - Alte Nachrichten zusammenfassen
        
        **5. Prompt Engineering**
        - Klare, spezifische Anweisungen
        - Beispiele im Prompt verwenden
        - System Prompts für Konsistenz
        """)
    
    st.divider()
    
    st.markdown("### 📋 Checkliste für Production-Apps")
    
    checklist = {
        "✅ Fehlerbehandlung implementiert": False,
        "✅ Streaming für bessere UX": False,
        "✅ Session State für Zustandsverwaltung": False,
        "✅ Benutzer-Feedback bei langen Operationen": False,
        "✅ Input-Validierung": False,
        "✅ Modell-Verfügbarkeit prüfen": False,
        "✅ Parameter konfigurierbar": False,
        "✅ Export-Funktionen": False,
        "✅ Responsive Design": False,
        "✅ Dokumentation": False
    }
    
    for item in checklist:
        st.checkbox(item, key=f"checklist_{item}")

# Zusammenfassung
st.divider()
st.header("📚 Zusammenfassung Tag 3")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ✅ Gelernt
    - Chat-Apps mit Streaming
    - Text-Generator
    - Code-Assistent
    - Zusammenfassungs-Tool
    - Multi-Model-Vergleich
    """)

with col2:
    st.markdown("""
    ### 🎯 Projekte
    - 5 vollständige Apps
    - Best Practices
    - Production-ready Code
    - Performance-Optimierung
    """)

with col3:
    st.markdown("""
    ### 🚀 Tag 4
    - Komplette Anwendung
    - Deployment
    - Erweiterte Features
    - Abschlussprojekt
    """)

# =================================================================================================
show_code(__file__)
