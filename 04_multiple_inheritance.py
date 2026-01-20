# 04_multiple_inheritance.py
# Multiple Inheritance Example

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print(f"I'm {self.name}, an employee in the Data Sector. Salary: {self.salary}.")

class Volunteer:
    def __init__(self, number):
        self.number = number

    def volunteer_count(self):
        print(f"There are {self.number} volunteers in the company.")

class EventCoordinator(Employee, Volunteer):
    def __init__(self, skill, name, salary, number):
        Employee.__init__(self, name, salary)
        Volunteer.__init__(self, number)
        self.skill = skill

    def skills(self):
        print(f"{self.name} has excellent skill in {self.skill} and manages both employees and volunteers.")

boss = EventCoordinator("Professional Management", "Tyhan Hasan", 50000, 2000)
boss.info()
boss.volunteer_count()
boss.skills()
