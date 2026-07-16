# Problem 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee:", self.name)
        print("Salary: $", self.salary)

    def calculate_bonus(self, rate):
        return self.salary * rate


# Test the class
employee1 = Employee("John Smith", 60000)

employee1.display_info()

bonus_rate = float(input("Enter bonus rate (example 0.10 for 10%): "))

bonus = employee1.calculate_bonus(bonus_rate)

print("Bonus Amount: $", bonus)
