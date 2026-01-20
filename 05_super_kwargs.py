# 05_super_kwargs.py
# Advanced OOP: super() + kwargs

class Teacher:
    def __init__(self, name, subject, **kwargs):
        self.name = name
        self.subject = subject
        super().__init__(**kwargs)

    def info(self):
        print(f"Hi! I'm {self.name}. I teach {self.subject}.")

class Trainer:
    def __init__(self, course, **kwargs):
        self.course = course
        super().__init__(**kwargs)

    def teach(self):
        print(f"I'm a Data Science trainer. I teach the {self.course} course.")

class SeniorTrainer(Teacher, Trainer):
    def __init__(self, experience, name, subject, course):
        super().__init__(name=name, subject=subject, course=course)
        self.experience = experience

    def performance(self):
        print(f"I'm a senior Data Scientist with {self.experience} years of experience.")

# Example usage
experience = int(input("Enter your industrial experience (years): "))
name = input("Enter your name: ")
subject = input("Enter your subject: ")
course = input("Enter your course: ")

senior = SeniorTrainer(experience, name, subject, course)
senior.info()
senior.teach()
senior.performance()
