# Problem 2
class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.credits = credits

    def compute_tuition(self):
        if self.district_code == "I":
            rate = 250
        else:
            rate = 500

        return self.credits * rate

    def display(self):
        print("Student:", self.first_name, self.last_name)
        print("District Code:", self.district_code)
        print("Credits:", self.credits)
        print("Tuition Owed: $", self.compute_tuition())


# Test the class
student1 = Student("Jane", "Doe", "I", 12)

student1.display()
