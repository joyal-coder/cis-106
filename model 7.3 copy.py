# Program 3

file = open("employees.txt", "r")

total_bonus = 0

while True:
    lastname = file.readline().strip()

    if lastname == "":
        break

    salary = float(file.readline())

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate
    total_bonus += bonus

    print("Name:", lastname)
    print("Salary: $", format(salary, ".2f"))
    print("Bonus: $", format(bonus, ".2f"))
    print()

file.close()

print("Total Bonuses Paid: $", format(total_bonus, ".2f"))
