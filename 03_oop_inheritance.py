# 03_oop_inheritance.py
# OOP Inheritance Example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! I'm {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"My roll number is {self.student_id}")

student_1 = Student(870255, 'Tyhan', 20)
student_1.introduce()
