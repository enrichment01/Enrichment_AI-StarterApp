"""
Tag 2: Streamlit

Interaktive Web-Apps mit Python erstellen
"""

import streamlit as st
import sys
from pathlib import Path
import pandas as pd

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_streamlit import show_code

st.set_page_config(
    page_title="Tag 2: Streamlit",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Tag 2: Streamlit")
st.markdown("**Interaktive Web-Apps mit Python erstellen**")

# Tabs
TAB_OVERVIEW = "Übersicht"
TAB_BASICS = "Basics"
TAB_WIDGETS = "Widgets"
TAB_LAYOUT = "Layout"
TAB_SESSION_STATE = "Session State"
TAB_DATA = "Daten"
TAB_EXERCISES = "Übungen"

TAB_NAMES = [
    TAB_OVERVIEW,
    TAB_BASICS,
    TAB_WIDGETS,
    TAB_LAYOUT,
    TAB_SESSION_STATE,
    TAB_DATA,
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
    st.header("📋 Kursübersicht Tag 2")
    
    st.markdown("""
    ### Lernziele
    Am Ende von Tag 2 können Sie:
    - ✅ Streamlit-Apps erstellen und ausführen
    - ✅ Interaktive Widgets nutzen
    - ✅ Layouts gestalten
    - ✅ Session State verwalten
    - ✅ Daten anzeigen und verarbeiten
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Themen
        1. **Was ist Streamlit?**
           - Framework Overview
           - Erste App
           - App ausführen
        
        2. **Text & Markdown**
           - Titel, Header
           - Markdown-Formatierung
           - Code-Blöcke
        
        3. **Widgets**
           - Eingabe-Felder
           - Buttons & Sliders
           - Select-Boxen
        
        4. **Layout**
           - Spalten
           - Expander
           - Container
        """)
    
    with col2:
        st.markdown("""
        ### ⏱️ Zeitplan
        - **09:00 - 10:00**: Streamlit Basics
        - **10:00 - 10:15**: Pause
        - **10:15 - 11:30**: Widgets & Layout
        - **11:30 - 12:00**: Session State
        - **12:00 - 13:00**: Mittagspause
        - **13:00 - 14:00**: Daten & Visualisierung
        - **14:00 - 15:00**: Praktische Übungen
        
        ### 📦 Installation
        ```bash
        pip install streamlit
        streamlit run app.py
        ```
        """)

# Tab 2: Basics
with tabs[get_tab_index(TAB_BASICS)]:
    st.header("1️⃣ Streamlit Basics")
    
    st.markdown("""
    ### Was ist Streamlit?
    Streamlit ist ein Python-Framework zum Erstellen von interaktiven Web-Apps 
    **ohne HTML, CSS oder JavaScript**.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Erste App")
        st.code('''import streamlit as st

# Titel
st.title("Meine erste Streamlit App")

# Text
st.write("Hallo Welt!")
st.write("Das ist **sehr einfach**!")

# Markdown
st.markdown("""
### Features
- 🚀 Schnell zu lernen
- 💻 Nur Python
- 🎨 Schönes Design
""")

# Header & Subheader
st.header("Dies ist ein Header")
st.subheader("Dies ist ein Subheader")

# Code anzeigen
code = """
def greet(name):
    return f"Hello, {name}!"
"""
st.code(code, language='python')
''', language='python')
        
        st.markdown("""
        ### 🚀 App starten
        ```bash
        streamlit run app.py
        ```
        
        Die App öffnet sich automatisch im Browser auf `http://localhost:8501`
        """)
    
    with col2:
        st.subheader("🎯 Live Demo")
        
        st.markdown("**Text-Ausgabe:**")
        st.write("Normaler Text mit write()")
        st.write("Man kann auch", "**mehrere**", "Argumente", "übergeben!")
        
        st.divider()
        
        st.markdown("**Markdown:**")
        st.markdown("**Fetter Text** und *kursiver Text*")
        st.markdown("- Liste Item 1\n- Liste Item 2\n- Liste Item 3")
        
        st.divider()
        
        st.markdown("**Info-Boxen:**")
        st.success("✅ Das ist eine Success-Message")
        st.info("ℹ️ Das ist eine Info-Message")
        st.warning("⚠️ Das ist eine Warning-Message")
        st.error("❌ Das ist eine Error-Message")
    
    st.divider()
    
    st.markdown("### 📊 Daten anzeigen")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''import pandas as pd

# DataFrame erstellen
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Alter': [25, 30, 35],
    'Stadt': ['Berlin', 'Hamburg', 'München']
})

# DataFrame anzeigen
st.dataframe(df)

# Statische Tabelle
st.table(df)

# Metriken
st.metric("Temperatur", "25°C", "+2°C")

# JSON
st.json({"name": "Alice", "age": 25})
''', language='python')
    
    with col2:
        st.markdown("**DataFrame:**")
        df_demo = pd.DataFrame({
            'Produkt': ['Laptop', 'Mouse', 'Keyboard'],
            'Preis': [999, 29, 79],
            'Lager': [50, 200, 150]
        })
        st.dataframe(df_demo, use_container_width=True)
        
        st.markdown("**Metriken:**")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Verkäufe", "234", "+12%")
        col_b.metric("Besucher", "1.2k", "+5%")
        col_c.metric("Umsatz", "€15k", "-3%")

# Tab 3: Widgets
with tabs[get_tab_index(TAB_WIDGETS)]:
    st.header("2️⃣ Streamlit Widgets")
    
    st.markdown("### Eingabe-Widgets - Ihr Werkzeugkasten für Interaktivität")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Code")
        st.code('''# Text Input
name = st.text_input("Ihr Name:", "Max Mustermann")

# Text Area (mehrzeilig)
text = st.text_area("Ihr Text:", height=100)

# Number Input
age = st.number_input(
    "Ihr Alter:", 
    min_value=0, 
    max_value=120, 
    value=25,
    step=1
)

# Slider
temperature = st.slider(
    "Temperatur:", 
    min_value=0.0, 
    max_value=2.0, 
    value=0.7, 
    step=0.1
)

# Select Box (Dropdown)
model = st.selectbox(
    "Wählen Sie ein Modell:",
    ["Option A", "Option B", "Option C"]
)

# Multi Select
options = st.multiselect(
    "Wählen Sie mehrere:",
    ["Python", "JavaScript", "Java", "C++"],
    default=["Python"]
)

# Checkbox
agree = st.checkbox("Ich stimme zu")

# Radio Buttons
choice = st.radio(
    "Wählen Sie eine Option:",
    ["Option 1", "Option 2", "Option 3"]
)

# Button
if st.button("Klick mich"):
    st.write("Button wurde geklickt!")

# File Uploader
file = st.file_uploader(
    "Datei hochladen",
    type=['txt', 'csv', 'pdf']
)

# Date & Time
date = st.date_input("Datum wählen:")
time = st.time_input("Zeit wählen:")

# Color Picker
color = st.color_picker("Farbe wählen:", "#00f900")
''', language='python')
    
    with col2:
        st.subheader("🎯 Live Demo")
        
        demo_name = st.text_input("Ihr Name:", "Max", key="w_name")
        
        demo_age = st.number_input(
            "Ihr Alter:", 
            18, 100, 25, 
            key="w_age"
        )
        
        demo_slider = st.slider(
            "Bewertung:", 
            0, 10, 5, 
            key="w_slider"
        )
        
        demo_select = st.selectbox(
            "Lieblingsprogrammiersprache:",
            ["Python", "JavaScript", "Java", "C++"],
            key="w_select"
        )
        
        demo_multi = st.multiselect(
            "Ihre Interessen:",
            ["KI", "Web", "Mobile", "Data Science", "Gaming"],
            default=["KI"],
            key="w_multi"
        )
        
        demo_radio = st.radio(
            "Erfahrungslevel:",
            ["Anfänger", "Fortgeschritten", "Experte"],
            key="w_radio"
        )
        
        demo_check = st.checkbox("Newsletter abonnieren", key="w_check")
        
        if st.button("📋 Zusammenfassung zeigen", key="w_summary"):
            st.success("**Ihre Eingaben:**")
            st.write(f"- Name: {demo_name}")
            st.write(f"- Alter: {demo_age}")
            st.write(f"- Bewertung: {demo_slider}/10")
            st.write(f"- Sprache: {demo_select}")
            st.write(f"- Interessen: {', '.join(demo_multi)}")
            st.write(f"- Level: {demo_radio}")
            st.write(f"- Newsletter: {'✅ Ja' if demo_check else '❌ Nein'}")

# Tab 4: Layout
with tabs[get_tab_index(TAB_LAYOUT)]:
    st.header("3️⃣ Layout-Elemente")
    
    st.markdown("### Spalten (Columns)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Gleiche Breite
col1, col2 = st.columns(2)

with col1:
    st.write("Spalte 1")

with col2:
    st.write("Spalte 2")

# Unterschiedliche Breite
col1, col2, col3 = st.columns([3, 1, 1])

# Mit Ratio
col1, col2 = st.columns([2, 1])
''', language='python')
        
        st.divider()
        
        st.markdown("**Demo: 3 Spalten**")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("Spalte 1")
        with c2:
            st.success("Spalte 2")
        with c3:
            st.warning("Spalte 3")
    
    with col2:
        st.markdown("**Live Beispiel:**")
        c1, c2 = st.columns(2)
        
        with c1:
            st.metric("Benutzer", "1.234", "+12%")
            st.metric("Posts", "567", "+23")
        
        with c2:
            st.metric("Likes", "8.9k", "+15%")
            st.metric("Kommentare", "432", "-5")
    
    st.divider()
    
    st.markdown("### Expander & Container")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Expander (ausklappbar)
with st.expander("Details anzeigen"):
    st.write("Versteckter Inhalt")
    st.write("Wird beim Klick angezeigt")

# Container
with st.container():
    st.write("Container Inhalt")
    st.button("Button in Container")
    
# Container mit Border
with st.container(border=True):
    st.write("Container mit Rahmen")
''', language='python')
    
    with col2:
        st.markdown("**Live Demo:**")
        
        with st.expander("🔍 Klick zum Erweitern", expanded=False):
            st.write("Dies ist ausklappbarer Inhalt!")
            st.write("Perfekt für optionale Details.")
        
        with st.container(border=True):
            st.write("**Container mit Rahmen**")
            st.write("Gut für visuelle Gruppierung")
    
    st.divider()
    
    st.markdown("### Sidebar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Sidebar
with st.sidebar:
    st.header("Einstellungen")
    
    user = st.text_input("Benutzer:")
    model = st.selectbox("Modell:", ["A", "B"])
    
    st.divider()
    
    st.metric("Status", "Aktiv")

# Oder direkt:
st.sidebar.title("Meine Sidebar")
st.sidebar.button("Klick")
''', language='python')
    
    with col2:
        st.info("👈 Schauen Sie links in die Sidebar, um ein echtes Beispiel zu sehen!")
    
    st.divider()
    
    st.markdown("### Tabs")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Tabs erstellen
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Daten", "⚙️ Settings"])

with tab1:
    st.write("Home Content")

with tab2:
    st.write("Daten Content")

with tab3:
    st.write("Settings Content")
''', language='python')
    
    with col2:
        st.markdown("**Live Demo:**")
        t1, t2, t3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
        
        with t1:
            st.write("Inhalt von Tab 1")
        with t2:
            st.write("Inhalt von Tab 2")
        with t3:
            st.write("Inhalt von Tab 3")

# Tab 5: Session State
with tabs[get_tab_index(TAB_SESSION_STATE)]:
    st.header("4️⃣ Session State - Zustandsverwaltung")
    
    st.markdown("""
    ### Was ist Session State?
    Session State ermöglicht es, Daten **zwischen Reruns** zu speichern. 
    Streamlit führt das komplette Script bei jeder Interaktion neu aus - 
    Session State bewahrt Daten über diese Reruns hinweg.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Grundlagen")
        st.code('''# Session State initialisieren
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Wert ändern
st.session_state.counter += 1

# Wert auslesen
st.write(f"Counter: {st.session_state.counter}")

# Mehrere Werte speichern
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'name': '',
        'age': 0,
        'history': []
    }

# Werte ändern
st.session_state.user_data['name'] = "Alice"
st.session_state.user_data['history'].append("Login")

# Callbacks
def increment():
    st.session_state.counter += 1

# Button mit Callback
st.button("Increment", on_click=increment)
''', language='python')
    
    with col2:
        st.subheader("🎯 Live Counter")
        
        # Counter initialisieren
        if 'demo_counter' not in st.session_state:
            st.session_state.demo_counter = 0
        
        # Counter anzeigen
        st.metric("Aktueller Wert", st.session_state.demo_counter)
        
        # Buttons
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            if st.button("➕ +1", key="inc"):
                st.session_state.demo_counter += 1
                st.rerun()
        
        with col_b:
            if st.button("➖ -1", key="dec"):
                st.session_state.demo_counter -= 1
                st.rerun()
        
        with col_c:
            if st.button("🔄 Reset", key="reset"):
                st.session_state.demo_counter = 0
                st.rerun()
    
    st.divider()
    
    st.markdown("### 📝 Todo-Liste Beispiel")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Todo-Liste initialisieren
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Neues Todo hinzufügen
new_todo = st.text_input("Neues Todo:")

if st.button("Hinzufügen"):
    if new_todo:
        st.session_state.todos.append({
            'text': new_todo,
            'done': False
        })
        st.rerun()

# Todos anzeigen
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        done = st.checkbox(
            todo['text'],
            value=todo['done'],
            key=f"todo_{i}"
        )
        if done != todo['done']:
            st.session_state.todos[i]['done'] = done
    
    with col2:
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.todos.pop(i)
            st.rerun()
''', language='python')
    
    with col2:
        st.markdown("**Live Todo-Liste:**")
        
        # Initialisierung
        if 'demo_todos' not in st.session_state:
            st.session_state.demo_todos = []
        
        # Neues Todo
        new_todo = st.text_input("Neues Todo:", key="new_todo")
        
        if st.button("➕ Hinzufügen", key="add_todo"):
            if new_todo:
                st.session_state.demo_todos.append(new_todo)
                st.rerun()
        
        # Todos anzeigen
        if st.session_state.demo_todos:
            for i, todo in enumerate(st.session_state.demo_todos):
                col_t, col_d = st.columns([4, 1])
                with col_t:
                    st.write(f"• {todo}")
                with col_d:
                    if st.button("🗑️", key=f"del_todo_{i}"):
                        st.session_state.demo_todos.pop(i)
                        st.rerun()
        else:
            st.info("Keine Todos vorhanden")

# Tab 6: Daten
with tabs[get_tab_index(TAB_DATA)]:
    st.header("5️⃣ Daten & Visualisierung")
    
    st.markdown("### 📊 Charts & Diagramme")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''import streamlit as st
import pandas as pd
import numpy as np

# Daten erstellen
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Line Chart
st.line_chart(chart_data)

# Bar Chart
st.bar_chart(chart_data)

# Area Chart
st.area_chart(chart_data)

# Map (mit lat/lon Daten)
map_data = pd.DataFrame({
    'lat': [52.52, 53.55, 50.11],
    'lon': [13.40, 9.99, 8.68]
})
st.map(map_data)
''', language='python')
    
    with col2:
        st.markdown("**Live Beispiel:**")
        
        # Demo Daten
        import numpy as np
        chart_data = pd.DataFrame(
            np.random.randn(10, 2),
            columns=['Python', 'JavaScript']
        )
        
        st.line_chart(chart_data)
    
    st.divider()
    
    st.markdown("### 📁 Datei-Upload & Download")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# File Upload
uploaded_file = st.file_uploader(
    "Datei hochladen",
    type=['csv', 'txt', 'json']
)

if uploaded_file:
    # CSV lesen
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# Download Button
data_to_download = "Hello World"

st.download_button(
    label="📥 Download",
    data=data_to_download,
    file_name="data.txt",
    mime="text/plain"
)

# CSV Download
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
csv = df.to_csv(index=False)

st.download_button(
    "📥 Download CSV",
    csv,
    "data.csv",
    "text/csv"
)
''', language='python')
    
    with col2:
        st.markdown("**Live Demo:**")
        
        # Upload
        demo_file = st.file_uploader(
            "Datei hochladen:",
            type=['txt', 'csv'],
            key="demo_upload"
        )
        
        if demo_file:
            st.success(f"✅ Datei geladen: {demo_file.name}")
            content = demo_file.read()
            st.text_area("Inhalt:", content.decode(), height=100)
        
        # Download
        st.download_button(
            "📥 Beispiel herunterladen",
            "Dies ist ein Beispieltext",
            "beispiel.txt",
            "text/plain"
        )

# Tab 7: Übungen
with tabs[get_tab_index(TAB_EXERCISES)]:
    st.header("6️⃣ Praktische Übungen")
    
    # Sub-Tabs für jede Übung
    exercise_tabs = st.tabs([
        "⚖️ BMI-Rechner",
        "📝 Notiz-App",
        "❓ Quiz-App",
        "🔢 Taschenrechner",
        "⏱️ Timer",
        "💱 Währung"
    ])
    
    # BMI-Rechner
    with exercise_tabs[0]:
        st.markdown("""
        ### ⚖️ BMI-Rechner
        Erstellen Sie einen interaktiven BMI-Rechner.
        
        **Anforderungen:**
        1. Eingabefelder für Gewicht (kg) und Größe (cm)
        2. Button zum Berechnen
        3. Ergebnis anzeigen mit Bewertung:
           - < 18.5: Untergewicht
           - 18.5 - 24.9: Normalgewicht
           - 25 - 29.9: Übergewicht
           - >= 30: Adipositas
        """)
        st.markdown("""
        **Erstellen Sie einen BMI-Rechner:**
        1. Eingabefelder für Gewicht (kg) und Größe (cm)
        2. Button zum Berechnen
        3. Ergebnis anzeigen mit Bewertung:
           - < 18.5: Untergewicht
           - 18.5 - 24.9: Normalgewicht
           - 25 - 29.9: Übergewicht
           - >= 30: Adipositas
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Ihre Lösung:**")
            
            weight = st.number_input("Gewicht (kg):", 50.0, 200.0, 70.0, key="bmi_weight")
            height = st.number_input("Größe (cm):", 100.0, 250.0, 170.0, key="bmi_height")
            
            if st.button("BMI berechnen", key="calc_bmi"):
                bmi = weight / ((height / 100) ** 2)
                st.metric("Ihr BMI", f"{bmi:.1f}")
                
                if bmi < 18.5:
                    st.info("Untergewicht")
                elif bmi < 25:
                    st.success("Normalgewicht")
                elif bmi < 30:
                    st.warning("Übergewicht")
                else:
                    st.error("Adipositas")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''weight = st.number_input("Gewicht (kg):", min_value=30.0, max_value=200.0, value=70.0)
height = st.number_input("Größe (cm):", min_value=100.0, max_value=250.0, value=170.0)

if st.button("Berechnen"):
    # BMI = Gewicht / (Größe in m)²
    bmi = weight / ((height / 100) ** 2)
    
    st.metric("BMI", f"{bmi:.1f}")
    
    if bmi < 18.5:
        st.info("Untergewicht")
    elif bmi < 25:
        st.success("Normalgewicht")
    elif bmi < 30:
        st.warning("Übergewicht")
    else:
        st.error("Adipositas")
''', language='python')
    
    # Notiz-App
    with exercise_tabs[1]:
        st.markdown("""
        ### 📝 Notiz-App
        Erstellen Sie eine Notiz-App mit Session State.
        
        **Anforderungen:**
        1. Eingabefeld für neue Notizen
        2. Button zum Speichern
        3. Alle Notizen mit Timestamp anzeigen
        4. Löschen-Button für jede Notiz
        5. Nutzen Sie Session State
        """)
        st.markdown("""
        **Erstellen Sie eine Notiz-App mit:**
        1. Eingabefeld für neue Notizen
        2. Button zum Speichern
        3. Alle Notizen mit Timestamp anzeigen
        4. Löschen-Button für jede Notiz
        5. Nutzen Sie Session State
        """)
        
        st.code('''from datetime import datetime

if 'notes' not in st.session_state:
    st.session_state.notes = []

new_note = st.text_area("Neue Notiz:")

if st.button("Speichern"):
    if new_note:
        st.session_state.notes.append({
            'text': new_note,
            'time': datetime.now().strftime("%H:%M:%S")
        })
        st.rerun()

for i, note in enumerate(st.session_state.notes):
    col1, col2 = st.columns([5, 1])
    with col1:
        st.write(f"**{note['time']}**: {note['text']}")
    with col2:
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.notes.pop(i)
            st.rerun()
''', language='python')
    
    # Quiz-App
    with exercise_tabs[2]:
        st.markdown("""
        ### ❓ Quiz-App
        Erstellen Sie eine interaktive Quiz-App.
        
        **Anforderungen:**
        1. Mehrere Multiple-Choice Fragen
        2. Radio-Buttons für Antworten
        3. Score-Tracking mit Session State
        4. Ergebnis am Ende anzeigen
        """)
        st.markdown("""
        **Erstellen Sie eine interaktive Quiz-App:**
        1. Mehrere Multiple-Choice Fragen
        2. Radio-Buttons für Antworten
        3. Score-Tracking mit Session State
        4. Ergebnis am Ende anzeigen
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktives Quiz:**")
            
            if 'quiz_score' not in st.session_state:
                st.session_state.quiz_score = 0
                st.session_state.quiz_answered = set()
            
            questions = [
                {"q": "Was ist Streamlit?", "options": ["Framework", "Datenbank", "Browser"], "correct": 0},
                {"q": "Welche Sprache nutzt Streamlit?", "options": ["JavaScript", "Python", "Java"], "correct": 1},
                {"q": "st.button() gibt zurück:", "options": ["String", "Integer", "Boolean"], "correct": 2}
            ]
            
            for i, q in enumerate(questions):
                st.markdown(f"**Frage {i+1}:** {q['q']}")
                answer = st.radio("", q['options'], key=f"q{i}", index=None)
                
                if answer and i not in st.session_state.quiz_answered:
                    if q['options'].index(answer) == q['correct']:
                        st.success("✅ Richtig!")
                        st.session_state.quiz_score += 1
                    else:
                        st.error(f"❌ Falsch. Richtig: {q['options'][q['correct']]}")
                    st.session_state.quiz_answered.add(i)
            
            if len(st.session_state.quiz_answered) == len(questions):
                st.metric("Endergebnis", f"{st.session_state.quiz_score}/{len(questions)}")
                
                if st.button("Neu starten", key="restart_quiz"):
                    st.session_state.quiz_score = 0
                    st.session_state.quiz_answered = set()
                    st.rerun()
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''if 'score' not in st.session_state:
    st.session_state.score = 0

questions = [
    {"q": "2 + 2?", "options": ["3", "4", "5"], "correct": 1}
]

for i, q in enumerate(questions):
    st.write(q['q'])
    answer = st.radio("", q['options'], key=f"q{i}")
    
    if st.button("Prüfen", key=f"check{i}"):
        if q['options'].index(answer) == q['correct']:
            st.success("Richtig!")
            st.session_state.score += 1
        else:
            st.error("Falsch!")

st.metric("Score", st.session_state.score)
''', language='python')
    
    # Taschenrechner
    with exercise_tabs[3]:
        st.markdown("""
        ### 🔢 Taschenrechner
        Erstellen Sie einen interaktiven Taschenrechner.
        
        **Anforderungen:**
        1. Zwei Zahlen-Eingabefelder
        2. Operation wählen (+, -, *, /)
        3. Berechnen-Button
        4. Ergebnis anzeigen
        5. Fehlerbehandlung (Division durch 0)
        """)
        st.markdown("""
        **Erstellen Sie einen interaktiven Taschenrechner:**
        1. Zwei Zahlen-Eingabefelder
        2. Operation wählen (+, -, *, /)
        3. Berechnen-Button
        4. Ergebnis anzeigen
        5. Fehlerbehandlung (Division durch 0)
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Rechner:**")
            
            num1 = st.number_input("Erste Zahl:", value=10.0, key="calc_num1")
            operation = st.selectbox("Operation:", ["+", "-", "*", "/"], key="calc_op")
            num2 = st.number_input("Zweite Zahl:", value=5.0, key="calc_num2")
            
            if st.button("Berechnen", key="calc_btn"):
                try:
                    if operation == "+":
                        result = num1 + num2
                    elif operation == "-":
                        result = num1 - num2
                    elif operation == "*":
                        result = num1 * num2
                    else:  # /
                        if num2 == 0:
                            st.error("❌ Division durch 0 nicht möglich!")
                        else:
                            result = num1 / num2
                            st.success(f"✅ {num1} {operation} {num2} = {result}")
                    
                    if operation != "/" or num2 != 0:
                        st.success(f"✅ {num1} {operation} {num2} = {result}")
                except Exception as e:
                    st.error(f"❌ Fehler: {e}")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''num1 = st.number_input("Zahl 1:", value=0.0)
operation = st.selectbox("Operation:", ["+", "-", "*", "/"])
num2 = st.number_input("Zahl 2:", value=0.0)

if st.button("="):
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                st.error("Division durch 0!")
            else:
                result = num1 / num2
        
        st.success(f"Ergebnis: {result}")
    except Exception as e:
        st.error(f"Fehler: {e}")
''', language='python')
    
    # Countdown-Timer
    with exercise_tabs[4]:
        st.markdown("""
        ### ⏱️ Countdown-Timer
        Erstellen Sie einen interaktiven Countdown-Timer.
        
        **Anforderungen:**
        1. Eingabe für Sekunden
        2. Start-Button
        3. Countdown anzeigen
        4. Progress Bar
        5. Alert bei 0
        """)
        st.markdown("""
        **Erstellen Sie einen Countdown-Timer:**
        1. Eingabe für Sekunden
        2. Start-Button
        3. Countdown anzeigen
        4. Progress Bar
        5. Alert bei 0
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Timer:**")
            
            seconds = st.number_input("Sekunden:", min_value=1, max_value=300, value=10, step=1, key="timer_seconds")
            
            if st.button("Timer starten", key="start_timer"):
                import time
                
                placeholder = st.empty()
                progress_bar = st.progress(0)
                
                for i in range(seconds, 0, -1):
                    placeholder.metric("Countdown", f"{i} Sekunden")
                    progress_bar.progress((seconds - i) / seconds)
                    time.sleep(1)
                
                placeholder.metric("Countdown", "⏰ Zeit abgelaufen!")
                progress_bar.progress(1.0)
                st.balloons()
                st.success("✅ Timer beendet!")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''import streamlit as st
import time

seconds = st.number_input("Sekunden:", min_value=1, value=10)

if st.button("Start"):
    placeholder = st.empty()
    progress = st.progress(0)
    
    for i in range(seconds, 0, -1):
        placeholder.metric("Timer", f"{i}s")
        progress.progress((seconds - i) / seconds)
        time.sleep(1)
    
    placeholder.success("Fertig!")
    progress.progress(1.0)
    st.balloons()
''', language='python')
    
    # Währungsrechner
    with exercise_tabs[5]:
        st.markdown("""
        ### 💱 Währungsrechner
        Erstellen Sie einen interaktiven Währungsrechner.
        
        **Anforderungen:**
        1. Betrag eingeben
        2. Von-Währung wählen
        3. Nach-Währung wählen
        4. Wechselkurs (vereinfacht)
        5. Ergebnis anzeigen
        """)
        st.markdown("""
        **Erstellen Sie einen Währungsrechner:**
        1. Betrag eingeben
        2. Von-Währung wählen
        3. Nach-Währung wählen
        4. Wechselkurs (vereinfacht)
        5. Ergebnis anzeigen
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Rechner:**")
            
            # Vereinfachte Wechselkurse (zu EUR)
            exchange_rates = {
                "EUR": 1.0,
                "USD": 1.09,
                "GBP": 0.86,
                "JPY": 163.5,
                "CHF": 0.93
            }
            
            amount = st.number_input("Betrag:", min_value=0.0, value=100.0, step=10.0, key="curr_amount")
            
            from_currency = st.selectbox("Von:", list(exchange_rates.keys()), key="curr_from")
            to_currency = st.selectbox("Nach:", list(exchange_rates.keys()), index=1, key="curr_to")
            
            if st.button("Umrechnen", key="convert_curr"):
                # Zu EUR konvertieren, dann zur Zielwährung
                eur_amount = amount / exchange_rates[from_currency]
                result = eur_amount * exchange_rates[to_currency]
                
                st.success(f"✅ {amount:.2f} {from_currency} = {result:.2f} {to_currency}")
                
                # Wechselkurs anzeigen
                rate = exchange_rates[to_currency] / exchange_rates[from_currency]
                st.info(f"Kurs: 1 {from_currency} = {rate:.4f} {to_currency}")
        
        with col2:
            st.markdown("**Lösungsansatz:**")
            st.code('''import streamlit as st

# Wechselkurse (Beispiel)
rates = {
    "EUR": 1.0,
    "USD": 1.09,
    "GBP": 0.86
}

amount = st.number_input("Betrag:", value=100.0)
from_curr = st.selectbox("Von:", list(rates.keys()))
to_curr = st.selectbox("Nach:", list(rates.keys()))

if st.button("Umrechnen"):
    # Über EUR als Basis
    eur = amount / rates[from_curr]
    result = eur * rates[to_curr]
    
    st.success(f"{amount} {from_curr} = {result:.2f} {to_curr}")
    
    # Direkter Kurs
    rate = rates[to_curr] / rates[from_curr]
    st.info(f"Kurs: 1 {from_curr} = {rate:.4f} {to_curr}")
''', language='python')

# Zusammenfassung
st.divider()
st.header("📚 Zusammenfassung Tag 2")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ✅ Gelernt
    - Streamlit Apps erstellen
    - Widgets nutzen
    - Layout gestalten
    - Session State
    - Daten anzeigen
    """)

with col2:
    st.markdown("""
    ### 🎯 Key Concepts
    - `st.write()` - Universal
    - `st.button()` - Interaktion
    - `st.columns()` - Layout
    - `st.session_state` - State
    - `st.dataframe()` - Daten
    """)

with col3:
    st.markdown("""
    ### 🚀 Tag 3
    - Ollama installieren
    - KI-Modelle nutzen
    - API Integration
    - Chat-Interface
    """)

# =================================================================================================
show_code(__file__)
