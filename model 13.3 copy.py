# Problem 3

last_names = []
scores = []

file = open("students.txt", "r")

for line in file:
    data = line.split()
    last_names.append(data[0])
    scores.append(int(data[1]))

file.close()

def display_students(names, grades):
    print("Last Name\tScore")
    print("-----------------------")

    for i in range(len(names)):
        print(names[i], "\t\t", grades[i])

def highest_score(names, grades):
    high_var = 0
    high_index = 0

    for i in range(len(grades)):
        if grades[i] > high_var:
            high_var = grades[i]
            high_index = i

    print("\nHighest Score")
    print(names[high_index], high_var)

def lowest_score(names, grades):
    low_var = 999
    low_index = 0

    for i in range(len(grades)):
        if grades[i] < low_var:
            low_var = grades[i]
            low_index = i

    print("Lowest Score")
    print(names[low_index], low_var)

display_students(last_names, scores)
highest_score(last_names, scores)
lowest_score(last_names, scores)
