# 08_mini_data_science.py
# Mini Data Science Exercises

marks = [45, 78, 90, 33, 67, 88]

# Average
average = sum(marks) / len(marks)
print("Average marks:", round(average, 2))

# Number of students passed (>=50)
passed_count = sum(1 for mark in marks if mark >= 50)
print("Number of students passed:", passed_count)

# Highest mark
highest = max(marks)
print("Highest mark:", highest)

# Sorted descending
sorted_marks = sorted(marks, reverse=True)
print("Marks sorted (descending):", sorted_marks)
