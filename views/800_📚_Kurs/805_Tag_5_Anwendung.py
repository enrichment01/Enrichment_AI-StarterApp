"""
Tag 4: Komplette Anwendung

Entwicklung einer vollständigen, produktionsreifen KI-Anwendung
"""

import streamlit as st
import sys
from pathlib import Path
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_streamlit import show_code, add_select_model
from lib.helper_ollama import get_available_models, list_models_by_capability
import ollama

st.set_page_config(
    page_title="Tag 4: Komplette Anwendung",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Tag 4: Komplette Anwendung")
st.markdown("**Von der Idee zur produktionsreifen KI-Anwendung**")

# Tabs
TAB_OVERVIEW = "Übersicht"
TAB_PROJECT_SETUP = "Projekt-Setup"
TAB_AI_ASSISTANT = "KI-Assistent Pro"
TAB_DEPLOYMENT = "Deployment"
TAB_TESTING = "Testing"
TAB_EXTENSIONS = "Erweiterungen"
TAB_CONCLUSION = "Abschluss"

TAB_NAMES = [
    TAB_OVERVIEW,
    TAB_PROJECT_SETUP,
    TAB_AI_ASSISTANT,
    TAB_DEPLOYMENT,
    TAB_TESTING,
    TAB_EXTENSIONS,
    TAB_CONCLUSION,
]

tabs = st.tabs(TAB_NAMES)

def get_tab_index(name):
    try:
        return TAB_NAMES.index(name)
    except ValueError:
        return -1

# Tab 1: Übersicht
with tabs[get_tab_index(TAB_OVERVIEW)]:
    st.header("📋 Tag 4: Komplette Anwendung")
    
    st.markdown("""
    ### 🎯 Projektziel
    Entwicklung einer vollständigen, produktionsreifen KI-Assistenten-Anwendung mit:
    - Multi-Funktionalität (Chat, Generation, Analyse)
    - Benutzerprofile und Einstellungen
    - Export- und Import-Funktionen
    - Fehlerbehandlung und Logging
    - Professionelles UI/UX Design
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Features
        1. **Chat-Interface**
           - Multi-Turn Conversations
           - System Prompts
           - Conversation History
        
        2. **Content Generation**
           - Texte
           - Code
           - Zusammenfassungen
        
        3. **Analyse-Tools**
           - Sentiment-Analyse
           - Keyword-Extraktion
           - Text-Statistiken
        
        4. **Management**
           - Benutzerprofile
           - Einstellungen speichern
           - Export/Import
        """)
    
    with col2:
        st.markdown("""
        ### ⏱️ Zeitplan
        - **09:00 - 10:00**: Projekt-Setup
        - **10:00 - 10:15**: Pause
        - **10:15 - 12:00**: Hauptanwendung
        - **12:00 - 13:00**: Mittagspause
        - **13:00 - 14:00**: Features & Testing
        - **14:00 - 14:30**: Deployment
        - **14:30 - 15:00**: Präsentation & Abschluss
        
        ### 🎓 Abschlussprojekt
        - Präsentation der Anwendung
        - Code-Review
        - Diskussion & Feedback
        - Zertifikat
        """)

# Tab 2: Projekt-Setup
with tabs[get_tab_index(TAB_PROJECT_SETUP)]:
    st.header("⚙️ Projekt-Setup")
    
    st.markdown("""
    ### 📁 Projektstruktur
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''ki_assistent_pro/
│
├── app.py                 # Hauptanwendung
├── requirements.txt       # Dependencies
├── README.md             # Dokumentation
│
├── lib/
│   ├── __init__.py
│   ├── chat.py           # Chat-Funktionen
│   ├── generator.py      # Text-Generierung
│   ├── analyzer.py       # Analyse-Tools
│   └── utils.py          # Hilfsfunktionen
│
├── config/
│   └── settings.py       # Konfiguration
│
├── data/
│   ├── profiles/         # Benutzerprofile
│   └── history/          # Chat-History
│
└── tests/
    └── test_app.py       # Unit Tests
''', language='text')
    
    with col2:
        st.markdown("### 📦 requirements.txt")
        st.code('''streamlit>=1.28.0
ollama>=0.1.0
pandas>=2.0.0
python-dotenv>=1.0.0
pytest>=7.0.0
''', language='text')
        
        st.markdown("### 🔧 config/settings.py")
        st.code('''# Ollama Configuration
OLLAMA_HOST = "http://localhost:11434"
DEFAULT_MODEL = "llama3.2"

# App Configuration
APP_TITLE = "KI-Assistent Pro"
APP_ICON = "🤖"

# Model Settings
DEFAULT_TEMPERATURE = 0.7
MAX_TOKENS = 2000
TOP_P = 0.9

# File Settings
DATA_DIR = "data"
PROFILES_DIR = "data/profiles"
HISTORY_DIR = "data/history"
''', language='python')

# Tab 3: KI-Assistent Pro
with tabs[get_tab_index(TAB_AI_ASSISTANT)]:
    st.header("🤖 KI-Assistent Pro")
    
    st.markdown("### Vollständige, produktionsreife Anwendung")
    
    # Sidebar Configuration
    with st.sidebar:
        st.header("⚙️ Einstellungen")
        
        # Benutzer-Profil
        st.subheader("👤 Profil")
        if 'username' not in st.session_state:
            st.session_state.username = "Benutzer"
        
        username = st.text_input("Benutzername:", st.session_state.username, key="profile_name")
        st.session_state.username = username
        
        st.divider()
        
        # Modell-Auswahl
        st.subheader("🤖 Modell")
        model = add_select_model()
        
        st.divider()
        
        # Parameter
        st.subheader("🎚️ Parameter")
        temperature = st.slider("Temperature:", 0.0, 2.0, 0.7, 0.1, key="pro_temp")
        max_tokens = st.number_input("Max Tokens:", 50, 4000, 2000, 100, key="pro_max")
        
        st.divider()
        
        # Statistiken
        st.subheader("📊 Statistiken")
        if 'pro_stats' not in st.session_state:
            st.session_state.pro_stats = {
                'messages': 0,
                'generations': 0,
                'analyses': 0
            }
        
        col_a, col_b = st.columns(2)
        col_a.metric("Nachrichten", st.session_state.pro_stats['messages'])
        col_b.metric("Generierungen", st.session_state.pro_stats['generations'])
        st.metric("Analysen", st.session_state.pro_stats['analyses'])
    
    # Main App
    app_tab = st.tabs(["💬 Chat", "✍️ Generator", "📊 Analyse", "💾 Management"])
    
    # Chat Tab
    with app_tab[0]:
        st.subheader("💬 Chat-Assistent")
        
        # System Prompt
        with st.expander("⚙️ System Prompt konfigurieren"):
            system_prompt = st.text_area(
                "System Prompt:",
                f"Du bist ein hilfreicher KI-Assistent für {username}. Antworte präzise und freundlich.",
                height=100,
                key="pro_system"
            )
        
        # Chat History
        if 'pro_chat' not in st.session_state:
            st.session_state.pro_chat = []
        
        # Display messages
        for msg in st.session_state.pro_chat:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
                if "timestamp" in msg:
                    st.caption(msg["timestamp"])
        
        # Chat input
        if prompt := st.chat_input("Nachricht eingeben..."):
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            # Add user message
            st.session_state.pro_chat.append({
                "role": "user",
                "content": prompt,
                "timestamp": timestamp
            })
            
            with st.chat_message("user"):
                st.markdown(prompt)
                st.caption(timestamp)
            
            # Generate response
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                try:
                    messages = [{"role": "system", "content": system_prompt}]
                    messages.extend([{"role": m["role"], "content": m["content"]} 
                                   for m in st.session_state.pro_chat])
                    
                    stream = ollama.chat(
                        model=model,
                        messages=messages,
                        stream=True,
                        options={'temperature': temperature, 'num_predict': max_tokens}
                    )
                    
                    for chunk in stream:
                        if 'message' in chunk and 'content' in chunk['message']:
                            full_response += chunk['message']['content']
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                    
                    response_timestamp = datetime.now().strftime("%H:%M:%S")
                    st.caption(response_timestamp)
                    
                    st.session_state.pro_chat.append({
                        "role": "assistant",
                        "content": full_response,
                        "timestamp": response_timestamp
                    })
                    
                    st.session_state.pro_stats['messages'] += 1
                    
                except Exception as e:
                    st.error(f"❌ Fehler: {e}")
        
        # Chat Controls
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🗑️ Chat löschen", key="pro_clear"):
                st.session_state.pro_chat = []
                st.rerun()
        
        with col2:
            if st.button("💾 Speichern", key="pro_save_chat"):
                if st.session_state.pro_chat:
                    filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    st.download_button(
                        "📥 Download",
                        json.dumps(st.session_state.pro_chat, ensure_ascii=False, indent=2),
                        filename,
                        "application/json"
                    )
        
        with col3:
            st.metric("Nachrichten", len(st.session_state.pro_chat))
    
    # Generator Tab
    with app_tab[1]:
        st.subheader("✍️ Content Generator")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            gen_type = st.selectbox(
                "Content-Typ:",
                ["Blog-Post", "Email", "Code", "Story", "Social Media", "Dokumentation"],
                key="pro_gen_type"
            )
            
            gen_prompt = st.text_area(
                "Beschreibung:",
                placeholder="Beschreiben Sie, was generiert werden soll...",
                height=200,
                key="pro_gen_prompt"
            )
            
            if st.button("✨ Generieren", type="primary", key="pro_generate"):
                if gen_prompt:
                    with col2:
                        with st.spinner("Generiere..."):
                            try:
                                response_placeholder = st.empty()
                                full_text = ""
                                
                                stream = ollama.generate(
                                    model=model,
                                    prompt=f"Erstelle {gen_type}: {gen_prompt}",
                                    stream=True,
                                    options={'temperature': temperature}
                                )
                                
                                for chunk in stream:
                                    if 'response' in chunk:
                                        full_text += chunk['response']
                                        response_placeholder.markdown(full_text + "▌")
                                
                                response_placeholder.markdown(full_text)
                                
                                st.session_state.pro_stats['generations'] += 1
                                
                                st.download_button(
                                    "📥 Download",
                                    full_text,
                                    f"{gen_type}_{datetime.now().strftime('%Y%m%d')}.txt",
                                    "text/plain"
                                )
                                
                            except Exception as e:
                                st.error(f"❌ Fehler: {e}")
        
        with col2:
            st.info("👈 Konfigurieren und klicken Sie auf 'Generieren'")
    
    # Analyse Tab
    with app_tab[2]:
        st.subheader("📊 Text-Analyse")
        
        analysis_text = st.text_area(
            "Text zur Analyse:",
            placeholder="Text hier eingeben...",
            height=200,
            key="pro_analysis_text"
        )
        
        analysis_types = st.multiselect(
            "Analyse-Typen:",
            ["Zusammenfassung", "Sentiment", "Keywords", "Statistiken"],
            default=["Zusammenfassung", "Statistiken"],
            key="pro_analysis_types"
        )
        
        if st.button("🔍 Analysieren", key="pro_analyze"):
            if analysis_text:
                col1, col2 = st.columns(2)
                
                # Statistiken
                if "Statistiken" in analysis_types:
                    with col1:
                        st.markdown("**📊 Statistiken:**")
                        words = analysis_text.split()
                        chars = len(analysis_text)
                        sentences = analysis_text.count('.') + analysis_text.count('!') + analysis_text.count('?')
                        
                        met1, met2, met3 = st.columns(3)
                        met1.metric("Wörter", len(words))
                        met2.metric("Zeichen", chars)
                        met3.metric("Sätze", sentences)
                
                # KI-Analysen
                analyses = []
                if "Zusammenfassung" in analysis_types:
                    analyses.append(("Zusammenfassung", f"Fasse diesen Text kurz zusammen: {analysis_text}"))
                if "Sentiment" in analysis_types:
                    analyses.append(("Sentiment", f"Analysiere das Sentiment (positiv/negativ/neutral): {analysis_text}"))
                if "Keywords" in analysis_types:
                    analyses.append(("Keywords", f"Extrahiere die 5 wichtigsten Keywords: {analysis_text}"))
                
                for title, prompt in analyses:
                    with col2 if "Statistiken" in analysis_types else col1:
                        st.markdown(f"**{title}:**")
                        
                        try:
                            response = ollama.generate(
                                model=model,
                                prompt=prompt,
                                options={'temperature': 0.3}
                            )
                            st.write(response['response'])
                            
                        except Exception as e:
                            st.error(f"Fehler bei {title}: {e}")
                
                st.session_state.pro_stats['analyses'] += 1
    
    # Management Tab
    with app_tab[3]:
        st.subheader("💾 Daten-Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📤 Export")
            
            export_data = {
                "username": st.session_state.username,
                "chat_history": st.session_state.pro_chat,
                "statistics": st.session_state.pro_stats,
                "settings": {
                    "model": model,
                    "temperature": temperature,
                    "max_tokens": max_tokens
                },
                "export_date": datetime.now().isoformat()
            }
            
            st.download_button(
                "📥 Alle Daten exportieren",
                json.dumps(export_data, ensure_ascii=False, indent=2),
                f"ki_assistent_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                "application/json"
            )
        
        with col2:
            st.markdown("### 📥 Import")
            
            uploaded_file = st.file_uploader("Daten importieren", type=['json'])
            
            if uploaded_file:
                try:
                    import_data = json.load(uploaded_file)
                    
                    if st.button("✅ Daten wiederherstellen"):
                        if 'username' in import_data:
                            st.session_state.username = import_data['username']
                        if 'chat_history' in import_data:
                            st.session_state.pro_chat = import_data['chat_history']
                        if 'statistics' in import_data:
                            st.session_state.pro_stats = import_data['statistics']
                        
                        st.success("✅ Daten erfolgreich importiert!")
                        st.rerun()
                        
                except Exception as e:
                    st.error(f"❌ Import-Fehler: {e}")

# Tab 4: Deployment
with tabs[get_tab_index(TAB_DEPLOYMENT)]:
    st.header("🚀 Deployment")
    
    st.markdown("""
    ### Anwendung deployen
    
    #### Option 1: Streamlit Cloud (Kostenlos)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Schritte:**
        1. Code auf GitHub pushen
        2. Bei [share.streamlit.io](https://share.streamlit.io) anmelden
        3. Repository verbinden
        4. App deployen
        
        **Vorteile:**
        - ✅ Kostenlos
        - ✅ Einfach
        - ✅ Automatische Updates
        
        **Nachteile:**
        - ❌ Ollama nicht verfügbar (Cloud-only)
        - ❌ Begrenzte Ressourcen
        """)
    
    with col2:
        st.markdown("""
        **requirements.txt für Cloud:**
        ```
        streamlit>=1.28.0
        pandas>=2.0.0
        openai  # Für Cloud-KI-APIs
        ```
        
        **Tipp:** Für Cloud-Deployment OpenAI API o.ä. verwenden statt Ollama
        """)
    
    st.divider()
    
    st.markdown("""
    #### Option 2: Docker (Lokal/Server)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Dockerfile:**")
        st.code('''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501"]
''', language='dockerfile')
    
    with col2:
        st.markdown("**docker-compose.yml:**")
        st.code('''version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
    depends_on:
      - ollama
  
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama

volumes:
  ollama_data:
''', language='yaml')

# Tab 5: Testing
with tabs[get_tab_index(TAB_TESTING)]:
    st.header("🧪 Testing & Qualitätssicherung")
    
    st.markdown("""
    ### Unit Tests mit pytest
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**tests/test_app.py:**")
        st.code('''import pytest
from lib.chat import format_message
from lib.analyzer import count_words

def test_format_message():
    """Test message formatting"""
    result = format_message("user", "Hello")
    assert result["role"] == "user"
    assert result["content"] == "Hello"

def test_count_words():
    """Test word counting"""
    text = "Hello world test"
    assert count_words(text) == 3

def test_empty_input():
    """Test empty input handling"""
    assert count_words("") == 0

# Run with: pytest tests/
''', language='python')
    
    with col2:
        st.markdown("**Manuelle Tests:**")
        st.markdown("""
        1. **Funktionalität**
           - Chat funktioniert
           - Generierung erfolgreich
           - Analyse korrekt
        
        2. **UI/UX**
           - Buttons reagieren
           - Fehler werden angezeigt
           - Loading-States sichtbar
        
        3. **Performance**
           - Schnelle Antwortzeiten
           - Keine Crashes
           - Memory-Usage ok
        
        4. **Edge Cases**
           - Leere Eingaben
           - Sehr lange Texte
           - Sonderzeichen
        """)

# Tab 6: Erweiterungen
with tabs[get_tab_index(TAB_EXTENSIONS)]:
    st.header("🔧 Mögliche Erweiterungen")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📈 Feature-Ideen
        
        **1. Multimodale Features**
        - 🖼️ Bild-Analyse (Vision Models)
        - 🎤 Sprach-Ein/Ausgabe
        - 📄 PDF-Verarbeitung
        
        **2. Erweiterte KI**
        - 🔗 RAG (Retrieval Augmented Generation)
        - 🧠 Long-term Memory
        - 🤝 Multi-Agent Systems
        
        **3. Collaboration**
        - 👥 Team-Features
        - 📤 Sharing von Chats
        - 💬 Kommentare
        
        **4. Personalisierung**
        - 🎨 Themes
        - ⚙️ Custom Workflows
        - 🔖 Favoriten & Templates
        """)
    
    with col2:
        st.markdown("""
        ### 💡 Technische Verbesserungen
        
        **1. Datenbank**
        ```python
        import sqlite3
        # oder PostgreSQL für Production
        ```
        
        **2. Authentication**
        ```python
        import streamlit_authenticator
        # Benutzer-Login
        ```
        
        **3. Caching**
        ```python
        @st.cache_data
        def expensive_computation():
            ...
        ```
        
        **4. Logging**
        ```python
        import logging
        logging.basicConfig(level=logging.INFO)
        ```
        
        **5. API-Integration**
        - OpenAI API
        - Anthropic Claude
        - Google Gemini
        """)

# Tab 7: Abschluss
with tabs[get_tab_index(TAB_CONCLUSION)]:
    st.header("🎓 Kurs-Abschluss")
    
    st.success("🎉 **Herzlichen Glückwunsch!** Sie haben den KI-Entwicklungs-Kurs erfolgreich abgeschlossen!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Was Sie gelernt haben
        
        **Tag 1: Python**
        - ✅ Python-Grundlagen
        - ✅ Datenstrukturen
        - ✅ OOP & Funktionen
        
        **Tag 2: Streamlit & Ollama**
        - ✅ Web-Apps erstellen
        - ✅ Lokale KI-Modelle
        - ✅ Integration
        
        **Tag 3: Apps entwickeln**
        - ✅ Chat-Interfaces
        - ✅ Content-Generation
        - ✅ Code-Tools
        
        **Tag 4: Production**
        - ✅ Vollständige App
        - ✅ Testing & Deployment
        - ✅ Best Practices
        """)
    
    with col2:
        st.markdown("""
        ### 🚀 Nächste Schritte
        
        **1. Weiterentwickeln**
        - Eigene Features hinzufügen
        - UI verbessern
        - Performance optimieren
        
        **2. Lernen**
        - Ollama Dokumentation
        - Streamlit Docs
        - Python Deep Dives
        
        **3. Community**
        - GitHub Repos teilen
        - Blog-Posts schreiben
        - Projekte präsentieren
        
        **4. Portfolio**
        - Apps deployen
        - Showcase erstellen
        - LinkedIn updaten
        """)
    
    st.divider()
    
    st.markdown("""
    ### 📚 Ressourcen & Links
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Python**
        - [Python.org](https://python.org)
        - [Real Python](https://realpython.com)
        - [Python Docs](https://docs.python.org)
        """)
    
    with col2:
        st.markdown("""
        **Streamlit**
        - [Streamlit.io](https://streamlit.io)
        - [Docs](https://docs.streamlit.io)
        - [Gallery](https://streamlit.io/gallery)
        """)
    
    with col3:
        st.markdown("""
        **Ollama**
        - [Ollama.ai](https://ollama.ai)
        - [GitHub](https://github.com/ollama/ollama)
        - [Models](https://ollama.ai/library)
        """)
    
    st.divider()
    
    st.markdown("""
    ### 💬 Feedback
    """)
    
    feedback = st.text_area(
        "Ihr Feedback zum Kurs:",
        placeholder="Was hat Ihnen gefallen? Was könnte verbessert werden?",
        height=150
    )
    
    rating = st.slider("Gesamtbewertung:", 1, 5, 5)
    
    if st.button("📤 Feedback senden", type="primary"):
        st.success("✅ Vielen Dank für Ihr Feedback!")
        st.balloons()
    
    st.divider()
    
    st.markdown("""
    ### 🎖️ Zertifikat
    """)
    
    st.info("""
    **KI-Entwicklungs-Kurs Zertifikat**
    
    Hiermit bestätigen wir, dass **{username}** erfolgreich am 4-tägigen
    KI-Entwicklungs-Kurs teilgenommen und folgende Kompetenzen erworben hat:
    
    - Python-Programmierung für KI-Anwendungen
    - Streamlit Web-App-Entwicklung
    - Ollama lokale KI-Modell-Integration
    - Produktionsreife Anwendungsentwicklung
    
    Datum: {datum}
    """.format(
        username=st.session_state.get('username', 'Teilnehmer'),
        datum=datetime.now().strftime("%d.%m.%Y")
    ))

# Zusammenfassung
st.divider()
st.header("🎯 Projekt-Checkliste")

checklist_items = [
    "✅ Python-Grundlagen verstanden",
    "✅ Streamlit-Apps erstellen können",
    "✅ Ollama lokal nutzen",
    "✅ Chat-Interface implementiert",
    "✅ Content-Generator erstellt",
    "✅ Analyse-Tools entwickelt",
    "✅ Fehlerbehandlung eingebaut",
    "✅ Tests geschrieben",
    "✅ Deployment-Option gewählt",
    "✅ Dokumentation erstellt"
]

cols = st.columns(2)
for idx, item in enumerate(checklist_items):
    with cols[idx % 2]:
        st.checkbox(item, key=f"final_check_{idx}")

# =================================================================================================
show_code(__file__)
