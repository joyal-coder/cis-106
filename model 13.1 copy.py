# Problem 1

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Wilson", "Moore"
]

def display_names(names):
    print("Last Names")
    print("----------")
    for i in range(len(names)):
        print(names[i])

def display_reverse(names):
    print("\nLast Names (Reverse)")
    print("--------------------")
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

display_names(last_names)
display_reverse(last_names)

