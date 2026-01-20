# 09_final_oop_challenge.py
# Final OOP Challenge

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, marks, name, age):
        super().__init__(name, age)
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

    def get_pass_fail(self):
        return "Passed" if self.average_marks() >= 40 else "Failed"

student_1 = Student([43, 53, 34, 63], 'Tyhan', 20)

print(f"{student_1.name}, your average marks are {student_1.average_marks():.2f} "
      f"and your exam result is {student_1.get_pass_fail()}.")
