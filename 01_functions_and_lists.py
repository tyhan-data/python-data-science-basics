# 01_functions_lists.py
# Python Functions + List Practice

# Function to filter even numbers
def filter_even(numbers):
    """Returns a list of even numbers"""
    return [num for num in numbers if num % 2 == 0]

list_num = [12, 7, 9, 20, 33]
print("Even numbers:", filter_even(list_num))
