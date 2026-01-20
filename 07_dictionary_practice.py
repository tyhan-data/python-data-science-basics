# 07_dictionary_practice.py
# Dictionary Practice

data = {'John': 25, 'Alice': 30, 'Bob': 19}

# All names
names = [name for name in data]
print("Names:", names)

# Names with age > 20
filtered = [(name, age) for name, age in data.items() if age > 20]
print("Names with age > 20:", filtered)
