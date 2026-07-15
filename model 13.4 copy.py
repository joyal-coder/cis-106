# Problem 4

students = {
    "Smith":88,
    "Johnson":92,
    "Williams":75,
    "Brown":83,
    "Jones":95
}

total = 0

print("Student\t\tGrade")
print("----------------------")

for name in students:
    print(name, "\t\t", students[name])
    total += students[name]

average = total / len(students)

print("----------------------")
print("Class Average =", round(average,2))
