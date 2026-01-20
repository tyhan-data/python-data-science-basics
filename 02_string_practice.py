# 02_string_practice.py
# String Manipulation Practice

# Function to count vowels
def count_vowels(text):
    """Returns number of vowels in a string"""
    vowels = "aeiou"
    return sum(1 for char in text if char.lower() in vowels)

text = "Data Science is fun"
print(f"Number of vowels in '{text}':", count_vowels(text))
