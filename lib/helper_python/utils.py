"""
Python utilities and example functions.
Extracted from pages/python_basics.py
"""


def greet(name, greeting="Hello"):
    """Greet a person with a customizable greeting."""
    return f"{greeting}, {name}!"


def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width


def get_stats(numbers):
    """Calculate statistics for a list of numbers."""
    return {
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }


class Person:
    """A simple Person class for OOP demonstration."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        """Return an introduction string."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def have_birthday(self):
        """Increment age and return a birthday message."""
        self.age += 1
        return f"Happy birthday! Now {self.age}"


def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def demonstrate_data_types():
    """Create and return examples of basic Python data types."""
    return {
        "integer_num": 42,
        "float_num": 3.14,
        "text": "Hello, Python!",
        "is_active": True,
        "fruits": ["apple", "banana", "cherry"],
        "person": {"name": "John", "age": 30, "city": "New York"},
        "coordinates": (10, 20)
    }


def demonstrate_list_operations():
    """Demonstrate various list operations."""
    numbers = [1, 2, 3, 4, 5]
    numbers.append(6)
    squares = [x**2 for x in numbers]
    first_three = numbers[:3]
    evens = [x for x in numbers if x % 2 == 0]
    
    return {
        "numbers": numbers,
        "squares": squares,
        "first_three": first_three,
        "evens": evens
    }


def demonstrate_loops():
    """Demonstrate for and while loops."""
    # For loop
    result = []
    for i in range(5):
        result.append(i * 2)
    
    # While loop
    countdown = []
    count = 5
    while count > 0:
        countdown.append(count)
        count -= 1
    
    # Enumerate
    fruits = ["apple", "banana", "cherry"]
    indexed_fruits = []
    for idx, fruit in enumerate(fruits):
        indexed_fruits.append(f"{idx}: {fruit}")
    
    return {
        "for_result": result,
        "countdown": countdown,
        "indexed_fruits": indexed_fruits
    }
