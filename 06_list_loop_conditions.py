# 06_list_loop_conditions.py
# List + Loops + Conditional Practice

numbers = [10, 23, 45, 66, 89, 90]

# Average
average = sum(numbers) / len(numbers)
print("Average:", round(average, 2))

# Maximum
max_number = max(numbers)
print("Maximum:", max_number)

# Maximum without max()
max_manual = numbers[0]
for num in numbers:
    if num > max_manual:
        max_manual = num
print("Maximum (manual):", max_manual)

# Numbers greater than 50
numbers_above_50 = [num for num in numbers if num > 50]
print("Numbers above 50:", numbers_above_50)
