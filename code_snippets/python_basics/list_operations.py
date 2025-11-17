# Creating a list
numbers = [1, 2, 3, 4, 5]

# Append
numbers.append(6)

# List comprehension
squares = [x**2 for x in numbers]

# Slicing
first_three = numbers[:3]

# Filter
evens = [x for x in numbers if x % 2 == 0]
