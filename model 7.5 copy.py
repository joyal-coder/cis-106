# Program 5

file = open("students.txt", "r")

total_tuition = 0
student_count = 0

while True:
    lastname = file.readline().strip()

    if lastname == "":
        break

    district = file.readline().strip()
    credits = int(file.readline())

    if district.upper() == "I":
        cost = 250
    else:
        cost = 500

    tuition = credits * cost

    total_tuition += tuition
    student_count += 1

    print("Student:", lastname)
    print("Credits:", credits)
    print("Tuition: $", format(tuition, ".2f"))
    print()

file.close()

print("Total Tuition: $", format(total_tuition, ".2f"))
print("Number of Students:", student_count)
