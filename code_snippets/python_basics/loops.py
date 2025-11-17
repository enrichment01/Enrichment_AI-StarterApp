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
