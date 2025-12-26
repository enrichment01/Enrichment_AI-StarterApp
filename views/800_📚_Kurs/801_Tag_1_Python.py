"""
Tag 1: Einführung Python

Grundlagen der Python-Programmierung für KI-Anwendungen
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lib.helper_streamlit import show_code

st.set_page_config(
    page_title="Tag 1: Einführung Python",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Tag 1: Einführung Python")
st.markdown("**Grundlagen der Python-Programmierung für KI-Anwendungen**")

# Tabs für verschiedene Themen
TAB_OVERVIEW = "Übersicht"
TAB_VARIABLES = "Variablen & Datentypen"
TAB_LISTS = "Listen & Dictionaries"
TAB_FUNCTIONS = "Funktionen"
TAB_CLASSES = "Klassen"
TAB_FILE_IO = "File I/O"
TAB_EXERCISES = "Übungen"

TAB_NAMES = [
    TAB_OVERVIEW,
    TAB_VARIABLES,
    TAB_LISTS,
    TAB_FUNCTIONS,
    TAB_CLASSES,
    TAB_FILE_IO,
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
    st.header("📋 Kursübersicht Tag 1")
    
    st.markdown("""
    ### Lernziele
    Am Ende von Tag 1 können Sie:
    - ✅ Python-Grundlagen verstehen und anwenden
    - ✅ Mit verschiedenen Datentypen arbeiten
    - ✅ Funktionen und Klassen erstellen
    - ✅ Dateien lesen und schreiben
    - ✅ Basis für KI-Anwendungen verstehen
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📚 Themen
        1. Variablen und Datentypen
        2. Listen und Dictionaries
        3. Funktionen
        4. Klassen und Objekte
        5. File I/O
        6. Praktische Übungen
        """)
    
    with col2:
        st.markdown("""
        ### ⏱️ Zeitplan
        - **09:00 - 10:30**: Grundlagen
        - **10:30 - 10:45**: Pause
        - **10:45 - 12:00**: Funktionen & Klassen
        - **12:00 - 13:00**: Mittagspause
        - **13:00 - 14:30**: File I/O & Übungen
        - **14:30 - 15:00**: Q&A
        """)
    
    st.info("💡 **Tipp**: Nutzen Sie die Tabs oben, um durch die verschiedenen Themen zu navigieren.")

# Tab 2: Variablen & Datentypen
with tabs[get_tab_index(TAB_VARIABLES)]:
    st.header("1️⃣ Variablen & Datentypen")
    
    st.markdown("""
    ### Grundlegende Datentypen in Python
    Python ist dynamisch typisiert - Sie müssen den Typ nicht explizit angeben.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Code")
        code = '''# Strings
name = "Alice"
greeting = 'Hello World'

# Numbers
age = 25
price = 19.99

# Boolean
is_active = True
has_license = False

# None
result = None

# Type checking
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(is_active)) # <class 'bool'>
'''
        st.code(code, language='python')
    
    with col2:
        st.subheader("🎯 Interaktiv")
        
        user_name = st.text_input("Ihr Name:", "Max")
        user_age = st.number_input("Ihr Alter:", min_value=0, max_value=120, value=25)
        is_student = st.checkbox("Student?", value=False)
        
        if st.button("Variablen anzeigen", key="var_show"):
            st.write(f"**Name:** {user_name} (Typ: {type(user_name).__name__})")
            st.write(f"**Alter:** {user_age} (Typ: {type(user_age).__name__})")
            st.write(f"**Student:** {is_student} (Typ: {type(is_student).__name__})")
    
    st.divider()
    
    st.markdown("""
    ### 🔄 Type Conversion (Typumwandlung)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# String to Int
age_str = "25"
age_int = int(age_str)

# Int to String
num = 42
num_str = str(num)

# String to Float
price = float("19.99")

# Bool Conversion
bool(1)      # True
bool(0)      # False
bool("")     # False
bool("text") # True
''', language='python')
    
    with col2:
        st.subheader("Probieren Sie es aus:")
        input_val = st.text_input("Eingabewert:", "123")
        
        if st.button("Konvertieren", key="convert"):
            try:
                st.success(f"Als Integer: {int(input_val)}")
                st.success(f"Als Float: {float(input_val)}")
                st.success(f"Als String: '{str(input_val)}'")
            except ValueError as e:
                st.error(f"Fehler: {e}")

# Tab 3: Listen & Dictionaries
with tabs[get_tab_index(TAB_LISTS)]:
    st.header("2️⃣ Listen & Dictionaries")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Listen")
        st.code('''# Listen erstellen
fruits = ["Apfel", "Banane", "Orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "text", True, 3.14]

# Zugriff
print(fruits[0])    # Apfel
print(fruits[-1])   # Orange

# Hinzufügen
fruits.append("Mango")

# Entfernen
fruits.remove("Banane")

# Länge
print(len(fruits))

# Slicing
print(numbers[1:3])  # [2, 3]

# List Comprehension
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
''', language='python')
    
    with col2:
        st.subheader("🎯 Interaktiv - Listen")
        
        if 'my_list' not in st.session_state:
            st.session_state.my_list = ["Apfel", "Banane"]
        
        new_item = st.text_input("Neues Element:", key="list_item")
        if st.button("Hinzufügen", key="list_add"):
            if new_item:
                st.session_state.my_list.append(new_item)
        
        st.write("**Aktuelle Liste:**")
        st.write(st.session_state.my_list)
        
        if st.button("Liste leeren", key="list_clear"):
            st.session_state.my_list = []
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Dictionaries")
        st.code('''# Dictionary erstellen
person = {
    "name": "Alice",
    "age": 25,
    "city": "Berlin"
}

# Zugriff
print(person["name"])     # Alice
print(person.get("age"))  # 25

# Hinzufügen/Ändern
person["email"] = "alice@example.com"
person["age"] = 26

# Keys und Values
print(person.keys())
print(person.values())

# Iterieren
for key, value in person.items():
    print(f"{key}: {value}")
''', language='python')
    
    with col2:
        st.subheader("🎯 Interaktiv - Dictionary")
        
        if 'my_dict' not in st.session_state:
            st.session_state.my_dict = {"name": "Max", "age": 25}
        
        dict_key = st.text_input("Key:", key="dict_key")
        dict_value = st.text_input("Value:", key="dict_value")
        
        if st.button("Hinzufügen", key="dict_add"):
            if dict_key and dict_value:
                st.session_state.my_dict[dict_key] = dict_value
        
        st.write("**Aktuelles Dictionary:**")
        st.json(st.session_state.my_dict)

# Tab 4: Funktionen
with tabs[get_tab_index(TAB_FUNCTIONS)]:
    st.header("3️⃣ Funktionen")
    
    st.markdown("""
    Funktionen sind wiederverwendbare Code-Blöcke, die eine bestimmte Aufgabe erfüllen.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Grundlagen")
        st.code('''# Einfache Funktion
def greet(name):
    return f"Hallo, {name}!"

# Funktion mit Standardwert
def greet_with_time(name, time="Tag"):
    return f"Guten {time}, {name}!"

# Multiple Return Values
def calculate(a, b):
    return a + b, a - b, a * b

# Lambda Funktion
square = lambda x: x ** 2

# Verwendung
result = greet("Alice")
sum_val, diff, prod = calculate(10, 5)
squared = square(4)
''', language='python')
    
    with col2:
        st.subheader("🎯 Interaktiv")
        
        st.markdown("**Temperaturumrechnung**")
        
        temp = st.number_input("Temperatur:", value=0.0)
        unit = st.radio("Einheit:", ["Celsius → Fahrenheit", "Fahrenheit → Celsius"])
        
        def celsius_to_fahrenheit(c):
            return (c * 9/5) + 32
        
        def fahrenheit_to_celsius(f):
            return (f - 32) * 5/9
        
        if st.button("Umrechnen", key="temp_convert"):
            if "Celsius" in unit:
                result = celsius_to_fahrenheit(temp)
                st.success(f"{temp}°C = {result:.2f}°F")
            else:
                result = fahrenheit_to_celsius(temp)
                st.success(f"{temp}°F = {result:.2f}°C")
    
    st.divider()
    
    st.markdown("### 🎯 Fortgeschrittene Funktionen")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Arbitrary Arguments
def sum_all(*args):
    return sum(args)

# Keyword Arguments
def create_profile(**kwargs):
    return kwargs

# Decorator
def uppercase_decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"hello, {name}"

# Verwendung
print(sum_all(1, 2, 3, 4))           # 10
print(create_profile(name="Max", age=25))
print(greet("alice"))                # HELLO, ALICE
''', language='python')
    
    with col2:
        st.markdown("**Praktisches Beispiel:**")
        st.code('''# Text-Verarbeitung
def process_text(text, 
                 uppercase=False,
                 remove_spaces=False,
                 reverse=False):
    result = text
    
    if uppercase:
        result = result.upper()
    
    if remove_spaces:
        result = result.replace(" ", "")
    
    if reverse:
        result = result[::-1]
    
    return result

# Test
text = "Hello World"
print(process_text(text, uppercase=True))
# HELLO WORLD
''', language='python')

# Tab 5: Klassen
with tabs[get_tab_index(TAB_CLASSES)]:
    st.header("4️⃣ Klassen und Objekte")
    
    st.markdown("""
    Objektorientierte Programmierung (OOP) hilft, Code zu strukturieren und wiederzuverwenden.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Grundlagen")
        st.code('''# Klasse definieren
class Person:
    # Konstruktor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Methode
    def greet(self):
        return f"Hallo, ich bin {self.name}"
    
    # Methode mit Parameter
    def birthday(self):
        self.age += 1
        return f"Jetzt bin ich {self.age}"

# Objekt erstellen
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Methoden aufrufen
print(person1.greet())
print(person1.birthday())
''', language='python')
    
    with col2:
        st.subheader("🎯 Beispiel: Bankkonto")
        st.code('''class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Eingezahlt: {amount}€"
        return "Ungültiger Betrag"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Abgehoben: {amount}€"
        return "Nicht genug Guthaben"
    
    def get_balance(self):
        return f"Kontostand: {self.balance}€"

# Verwendung
account = BankAccount("Max", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
''', language='python')
    
    st.divider()
    
    st.markdown("### 🎯 Vererbung")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.code('''# Basisklasse
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

# Vererbung
class Dog(Animal):
    def speak(self):
        return "Wuff!"

class Cat(Animal):
    def speak(self):
        return "Miau!"

# Verwendung
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, dog.speak())  # Buddy Wuff!
print(cat.name, cat.speak())  # Whiskers Miau!
''', language='python')
    
    with col2:
        st.markdown("**Praktisches KI-Beispiel:**")
        st.code('''class AIModel:
    def __init__(self, name):
        self.name = name
        self.trained = False
    
    def train(self, data):
        print(f"Training {self.name}...")
        self.trained = True
    
    def predict(self, input_data):
        if not self.trained:
            return "Modell nicht trainiert!"
        return f"Vorhersage für {input_data}"

class TextModel(AIModel):
    def __init__(self, name, language="de"):
        super().__init__(name)
        self.language = language
    
    def predict(self, text):
        if not self.trained:
            return "Modell nicht trainiert!"
        return f"Analyse von '{text}' in {self.language}"
''', language='python')

# Tab 6: File I/O
with tabs[get_tab_index(TAB_FILE_IO)]:
    st.header("5️⃣ Dateien lesen und schreiben")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Dateien lesen")
        st.code('''# Datei lesen (kompletter Inhalt)
with open('data.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# Zeile für Zeile lesen
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Alle Zeilen als Liste
with open('data.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# JSON lesen
import json
with open('data.json', 'r') as file:
    data = json.load(file)
''', language='python')
    
    with col2:
        st.subheader("✍️ Dateien schreiben")
        st.code('''# Datei schreiben (überschreiben)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Hallo Welt!\\n")
    file.write("Zweite Zeile")

# Datei schreiben (anhängen)
with open('log.txt', 'a') as file:
    file.write("Neuer Eintrag\\n")

# JSON schreiben
import json
data = {"name": "Alice", "age": 25}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

# CSV schreiben
import csv
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Alter"])
    writer.writerow(["Alice", 25])
''', language='python')
    
    st.divider()
    
    st.subheader("🎯 Interaktives Beispiel")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Datei erstellen**")
        filename = st.text_input("Dateiname:", "test.txt")
        file_content = st.text_area("Inhalt:", "Hallo Welt!\nDies ist ein Test.")
        
        if st.button("Datei speichern", key="save_file"):
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(file_content)
                st.success(f"✅ Datei '{filename}' gespeichert!")
            except Exception as e:
                st.error(f"❌ Fehler: {e}")
    
    with col2:
        st.markdown("**Datei lesen**")
        read_filename = st.text_input("Datei zum Lesen:", "test.txt", key="read_file")
        
        if st.button("Datei lesen", key="read_btn"):
            try:
                with open(read_filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                st.success("✅ Datei gelesen:")
                st.code(content)
            except FileNotFoundError:
                st.error(f"❌ Datei '{read_filename}' nicht gefunden!")
            except Exception as e:
                st.error(f"❌ Fehler: {e}")

# Tab 7: Übungen
with tabs[get_tab_index(TAB_EXERCISES)]:
    st.header("6️⃣ Praktische Übungen")
    
    # Sub-Tabs für jede Übung
    exercise_tabs = st.tabs([
        "📝 Wort-Zähler",
        "✅ To-Do Liste",
        "🔢 Fibonacci",
        "🔄 Palindrom",
        "🌡️ Temperatur",
        "🔐 Primzahl",
        "🔒 Passwort"
    ])
    
    # Wort-Zähler
    with exercise_tabs[0]:
        st.markdown("""
        ### 🎯 Wort-Zähler
        Schreiben Sie ein Programm, das einen Text analysiert.
        
        **Anforderungen:**
        1. Akzeptiert einen Text als Eingabe
        2. Zählt die Anzahl der Wörter
        3. Zählt die Anzahl der Zeichen
        4. Findet das längste Wort
        5. Gibt Statistiken aus
        """)
        st.markdown("""
        **Anforderungen:**
        1. Akzeptiert einen Text als Eingabe
        2. Zählt die Anzahl der Wörter
        3. Zählt die Anzahl der Zeichen
        4. Findet das längste Wort
        5. Gibt Statistiken aus
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Ihre Lösung:**")
            exercise_text = st.text_area(
                "Text eingeben:",
                "Python ist eine großartige Programmiersprache für KI und Machine Learning.",
                height=150,
                key="ex1_text"
            )
            
            if st.button("Analysieren", key="ex1_analyze"):
                words = exercise_text.split()
                word_count = len(words)
                char_count = len(exercise_text)
                longest_word = max(words, key=len) if words else ""
                
                st.success("✅ Ergebnisse:")
                st.write(f"**Wörter:** {word_count}")
                st.write(f"**Zeichen:** {char_count}")
                st.write(f"**Längstes Wort:** {longest_word} ({len(longest_word)} Zeichen)")
        
        with col2:
            st.markdown("**Lösungsvorschlag:**")
            st.code('''def analyze_text(text):
    words = text.split()
    
    stats = {
        "word_count": len(words),
        "char_count": len(text),
        "longest_word": max(words, key=len) if words else ""
    }
    
    return stats

# Verwendung
text = "Python ist großartig"
result = analyze_text(text)
print(result)
''', language='python')
    
    # To-Do Liste
    with exercise_tabs[1]:
        st.markdown("""
        ### ✅ To-Do Liste
        Erstellen Sie eine einfache To-Do Liste mit Session State.
        
        **Anforderungen:**
        1. Eingabefeld für neue Aufgaben
        2. Button zum Hinzufügen
        3. Liste aller Aufgaben anzeigen
        4. Checkbox für erledigte Aufgaben
        5. Löschen-Button für jede Aufgabe
        """)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktive To-Do Liste:**")
            
            if 'todos' not in st.session_state:
                st.session_state.todos = []
            
            new_todo = st.text_input("Neue Aufgabe:", key="new_todo")
            
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Hinzufügen", key="add_todo"):
                    if new_todo:
                        st.session_state.todos.append({"task": new_todo, "done": False})
            
            with col_b:
                if st.button("Alle löschen", key="clear_todos"):
                    st.session_state.todos = []
            
            st.markdown("**Meine Aufgaben:**")
            for idx, todo in enumerate(st.session_state.todos):
                col_check, col_task = st.columns([1, 4])
                with col_check:
                    done = st.checkbox("", value=todo["done"], key=f"todo_{idx}")
                    st.session_state.todos[idx]["done"] = done
                with col_task:
                    style = "text-decoration: line-through;" if done else ""
                    st.markdown(f"<p style='{style}'>{todo['task']}</p>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Lösungsvorschlag (Klasse):**")
            st.code('''class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({
            "task": task,
            "done": False
        })
    
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    
    def show_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task["done"] else "○"
            print(f"{i}: [{status}] {task['task']}")

# Verwendung
todo = TodoList()
todo.add_task("Python lernen")
todo.add_task("Projekt starten")
todo.mark_done(0)
todo.show_tasks()
''', language='python')
    
    # Fibonacci
    with exercise_tabs[2]:
        st.markdown("""
        ### 🔢 Fibonacci-Folge
        Generieren Sie die Fibonacci-Folge.
        
        **Aufgabe:**
        - Generieren Sie die ersten n Fibonacci-Zahlen
        - Zeigen Sie die Zahlen als Liste an
        - Visualisieren Sie die Folge als Diagramm
        """)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Generator:**")
            
            n = st.number_input("Anzahl Fibonacci-Zahlen:", 1, 50, 10, key="fib_n")
            
            if st.button("Generieren", key="gen_fib"):
                def fibonacci(n):
                    fib = [0, 1]
                    for i in range(2, n):
                        fib.append(fib[i-1] + fib[i-2])
                    return fib[:n]
                
                result = fibonacci(n)
                st.success("✅ Fibonacci-Folge:")
                st.write(result)
                
                # Visualisierung
                import pandas as pd
                df = pd.DataFrame({'Index': range(len(result)), 'Wert': result})
                st.line_chart(df.set_index('Index'))
        
        with col2:
            st.markdown("**Lösungsvorschlag:**")
            st.code('''def fibonacci(n):
    """Generiert die ersten n Fibonacci-Zahlen"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib

# Verwendung
print(fibonacci(10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Rekursive Version
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
''', language='python')
    
    # Palindrom
    with exercise_tabs[3]:
        st.markdown("""
        ### 🔄 Palindrom-Checker
        Prüfen Sie, ob ein Wort ein Palindrom ist.
        
        **Aufgabe:**
        - Eingabe eines Wortes
        - Prüfung, ob es vorwärts und rückwärts gleich ist
        - Anzeige des umgekehrten Wortes
        """)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Checker:**")
            
            word = st.text_input("Wort eingeben:", "Otto", key="palindrome_word").lower()
            
            if st.button("Prüfen", key="check_palindrome"):
                is_palindrome = word == word[::-1]
                
                if is_palindrome:
                    st.success(f"✅ '{word}' ist ein Palindrom!")
                else:
                    st.error(f"❌ '{word}' ist kein Palindrom.")
                
                st.info(f"Rückwärts: {word[::-1]}")
        
        with col2:
            st.markdown("**Lösungsvorschlag:**")
            st.code('''def is_palindrome(text):
    """Prüft, ob ein Text ein Palindrom ist"""
    # In Kleinbuchstaben konvertieren
    text = text.lower()
    
    # Leerzeichen und Sonderzeichen entfernen
    cleaned = ''.join(c for c in text if c.isalnum())
    
    # Vergleich mit umgekehrtem Text
    return cleaned == cleaned[::-1]

# Test
print(is_palindrome("Otto"))      # True
print(is_palindrome("Anna"))      # True
print(is_palindrome("Python"))    # False
print(is_palindrome("A man a plan a canal Panama"))  # True
''', language='python')
    
    # Temperatur-Konverter
    with exercise_tabs[4]:
        st.markdown("""
        ### 🌡️ Temperatur-Konverter
        Konvertieren Sie zwischen Celsius, Fahrenheit und Kelvin.
        
        **Aufgabe:**
        - Eingabe einer Temperatur
        - Auswahl der Quell-Einheit
        - Auswahl der Ziel-Einheit
        - Berechnung und Anzeige des Ergebnisses
        """)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Konverter:**")
            
            temp_value = st.number_input("Temperatur:", -273.15, 10000.0, 20.0, key="temp_value")
            
            from_unit = st.selectbox("Von:", ["Celsius", "Fahrenheit", "Kelvin"], key="from_unit")
            to_unit = st.selectbox("Nach:", ["Celsius", "Fahrenheit", "Kelvin"], key="to_unit")
            
            if st.button("Konvertieren", key="convert_temp"):
                # Konvertierung
                if from_unit == "Celsius":
                    celsius = temp_value
                elif from_unit == "Fahrenheit":
                    celsius = (temp_value - 32) * 5/9
                else:  # Kelvin
                    celsius = temp_value - 273.15
                
                if to_unit == "Celsius":
                    result = celsius
                elif to_unit == "Fahrenheit":
                    result = celsius * 9/5 + 32
                else:  # Kelvin
                    result = celsius + 273.15
                
                st.success(f"✅ {temp_value}° {from_unit} = {result:.2f}° {to_unit}")
        
        with col2:
            st.markdown("**Lösungsvorschlag:**")
            st.code('''class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

# Verwendung
conv = TemperatureConverter()
print(conv.celsius_to_fahrenheit(20))  # 68.0
print(conv.celsius_to_kelvin(20))      # 293.15
''', language='python')
    
    # Primzahl-Checker
    with exercise_tabs[5]:
        st.markdown("""
        ### 🔐 Primzahl-Checker
        Prüfen Sie, ob eine Zahl eine Primzahl ist.
        
        **Aufgabe:**
        - Eingabe einer Zahl
        - Prüfung, ob es eine Primzahl ist
        - Anzeige der Teiler bei Nicht-Primzahlen
        """)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Checker:**")
            
            number = st.number_input("Zahl eingeben:", min_value=2, max_value=10000, value=17, step=1, key="prime_num")
            
            if st.button("Prüfen", key="check_prime"):
                def is_prime(n):
                    if n < 2:
                        return False
                    for i in range(2, int(n ** 0.5) + 1):
                        if n % i == 0:
                            return False
                    return True
                
                if is_prime(number):
                    st.success(f"✅ {number} ist eine Primzahl!")
                else:
                    st.error(f"❌ {number} ist keine Primzahl.")
                    
                    # Teiler finden
                    divisors = [i for i in range(2, number) if number % i == 0]
                    if divisors:
                        st.info(f"Teiler: {divisors[:5]}{'...' if len(divisors) > 5 else ''}")
        
        with col2:
            st.markdown("**Lösungsvorschlag:**")
            st.code('''def is_prime(n):
    """Prüft, ob eine Zahl eine Primzahl ist"""
    if n < 2:
        return False
    
    # Nur bis zur Wurzel prüfen (Optimierung)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Test
print(is_prime(17))   # True
print(is_prime(20))   # False
print(is_prime(97))   # True

# Primzahlen bis n finden
def primes_up_to(n):
    return [i for i in range(2, n+1) if is_prime(i)]

print(primes_up_to(20))
# [2, 3, 5, 7, 11, 13, 17, 19]
''', language='python')
    
    # Passwort-Generator
    with exercise_tabs[6]:
        st.markdown("""
        ### 🔒 Passwort-Generator
        Generieren Sie sichere Passwörter.
        
        **Aufgabe:**
        - Auswahl der Passwortlänge
        - Optionen für verschiedene Zeichentypen
        - Generierung eines zufälligen Passworts
        - Bewertung der Passwort-Stärke
        """)
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Interaktiver Generator:**")
            
            pw_length = st.slider("Passwortlänge:", 8, 32, 16, key="pw_length")
            
            col_a, col_b = st.columns(2)
            with col_a:
                use_upper = st.checkbox("Großbuchstaben", value=True, key="pw_upper")
                use_lower = st.checkbox("Kleinbuchstaben", value=True, key="pw_lower")
            with col_b:
                use_digits = st.checkbox("Zahlen", value=True, key="pw_digits")
                use_special = st.checkbox("Sonderzeichen", value=True, key="pw_special")
            
            if st.button("Passwort generieren", key="gen_pw"):
                import random
                import string
                
                chars = ""
                if use_upper:
                    chars += string.ascii_uppercase
                if use_lower:
                    chars += string.ascii_lowercase
                if use_digits:
                    chars += string.digits
                if use_special:
                    chars += "!@#$%^&*()_+-="
                
                if chars:
                    password = ''.join(random.choice(chars) for _ in range(pw_length))
                    st.success("✅ Generiertes Passwort:")
                    st.code(password)
                    
                    # Stärke bewerten
                    strength = 0
                    if use_upper: strength += 1
                    if use_lower: strength += 1
                    if use_digits: strength += 1
                    if use_special: strength += 1
                    if pw_length >= 12: strength += 1
                    
                    if strength >= 4:
                        st.success("💪 Stark")
                    elif strength >= 3:
                        st.warning("⚠️ Mittel")
                    else:
                        st.error("❌ Schwach")
                else:
                    st.warning("Wählen Sie mindestens eine Option!")
        
        with col2:
            st.markdown("**Lösungsvorschlag:**")
            st.code('''import random
import string

def generate_password(length=16, 
                     use_upper=True,
                     use_lower=True,
                     use_digits=True,
                     use_special=True):
    """Generiert ein sicheres Passwort"""
    
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += "!@#$%^&*()_+-="
    
    if not chars:
        raise ValueError("Mindestens eine Option wählen!")
    
    password = ''.join(random.choice(chars) 
                      for _ in range(length))
    
    return password

# Verwendung
print(generate_password(16))
print(generate_password(12, use_special=False))
''', language='python')

# Zusammenfassung
st.divider()
st.header("📚 Zusammenfassung Tag 1")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### ✅ Gelernt
    - Python Grundlagen
    - Datentypen & Variablen
    - Listen & Dictionaries
    - Funktionen
    - Klassen & OOP
    - File I/O
    """)

with col2:
    st.markdown("""
    ### 🎯 Nächste Schritte
    - Übungen wiederholen
    - Eigene Projekte starten
    - **Tag 2 vorbereiten:**
      - Streamlit
      - Ollama
    """)

with col3:
    st.markdown("""
    ### 📖 Ressourcen
    - [Python Docs](https://docs.python.org/3/)
    - [Real Python](https://realpython.com/)
    - [Python Tutorial](https://www.python-tutorial.org/)
    """)

# =================================================================================================
show_code(__file__)
