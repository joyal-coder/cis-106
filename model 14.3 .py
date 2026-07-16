# Problem 3
class Student:
    tuition_rates = {
        "I": 250,
        "O": 500,
        "X": 800,
        "G": 250
    }

    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.credits = credits

    def compute_tuition(self):
        rate = Student.tuition_rates.get(self.district_code, 500)
        return self.credits * rate

    def display(self):
        print("------------------------")
        print("Student:", self.first_name, self.last_name)
        print("District Code:", self.district_code)
        print("Credits:", self.credits)
        print("Tuition Owed: $", self.compute_tuition())


# Instantiate one student of each district code

student1 = Student("Alice", "Brown", "I", 12)
student2 = Student("Bob", "Smith", "O", 12)
student3 = Student("Carlos", "Lopez", "X", 12)
student4 = Student("Diana", "Jones", "G", 12)

student1.display()
student2.display()
student3.display()
student4.display()
