def calculate_scores(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average


while True:
    last_name = input("Enter student last name (or Q to quit): ")

    if last_name.upper() == "Q":
        break

    exam1 = float(input("Exam 1: "))
    exam2 = float(input("Exam 2: "))
    exam3 = float(input("Exam 3: "))

    total, average = calculate_scores(exam1, exam2, exam3)

    print("Student:", last_name)
    print("Total Points:", total)
    print("Average:", round(average, 2))
    print()
