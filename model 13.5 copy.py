# Problem 5

students = {
    "Smith":[88,91,85],
    "Johnson":[92,95,90],
    "Williams":[75,78,80],
    "Brown":[83,85,87],
    "Jones":[95,94,98]
}

def create_average_list(student_dict):

    averages = []

    for name in student_dict:

        grades = student_dict[name]

        total = 0

        for grade in grades:
            total += grade

        average = total / len(grades)

        averages.append([name, average])

    return averages

average_list = create_average_list(students)

print("Student\t\tAverage")
print("---------------------------")

for item in average_list:
    print(item[0], "\t\t", round(item[1],2))

grade1 = 0
grade2 = 0
grade3 = 0

count = len(students)

for grades in students.values():
    grade1 += grades[0]
    grade2 += grades[1]
    grade3 += grades[2]

print("\nClass Average for Grade 1 =", round(grade1/count,2))
print("Class Average for Grade 2 =", round(grade2/count,2))
print("Class Average for Grade 3 =", round(grade3/count,2))

