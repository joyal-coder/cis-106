# Problem 2

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Wilson", "Moore"
]

scores = [88, 92, 75, 83, 95, 79, 90, 86, 91, 84]

def display_students(names, grades):
    print("Last Name\tScore")
    print("------------------------")

    for i in range(len(names)):
        print(names[i], "\t\t", grades[i])

def display_reverse(names, grades):
    print("\nReverse Order")
    print("Last Name\tScore")
    print("------------------------")

    for i in range(len(names)-1, -1, -1):
        print(names[i], "\t\t", grades[i])

display_students(last_names, scores)
display_reverse(last_names, scores)
