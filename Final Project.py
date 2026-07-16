# dogrescue.py

# Global list to store dogs
dogs = []


def main():
    menu()


def menu():
    while True:
        print("\n===== Dog Rescue Menu =====")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addDog()
        elif choice == "2":
            viewDogs()
        elif choice == "3":
            findDog()
        elif choice == "4":
            print("Thank you for using the Dog Rescue Application!")
            break
        else:
            print("Invalid choice. Please try again.")


def addDog():
    print("\nAdd a Dog")

    name = input("Dog Name: ")
    breed = input("Dog Breed: ")
    age = input("Dog Age: ")
    weight = input("Dog Weight: ")

    dog = {
        "Name": name,
        "Breed": breed,
        "Age": age,
        "Weight": weight
    }

    dogs.append(dog)
    print("Dog added successfully!")


def viewDogs():
    print("\n===== Dog List =====")

    if len(dogs) == 0:
        print("No dogs have been added.")
        return

    print("{:<15} {:<20} {:<10} {:<10}".format("Name", "Breed", "Age", "Weight"))
    print("-" * 60)

    for dog in dogs:
        print("{:<15} {:<20} {:<10} {:<10}".format(
            dog["Name"],
            dog["Breed"],
            dog["Age"],
            dog["Weight"]
        ))


def findDog():
    search = input("\nEnter dog name to search: ")

    found = False

    for dog in dogs:
        if dog["Name"].lower() == search.lower():
            print("\nDog Found!")
            print("Name:", dog["Name"])
            print("Breed:", dog["Breed"])
            print("Age:", dog["Age"])
            print("Weight:", dog["Weight"])
            found = True
            break

    if not found:
        print("Dog not found.")


# Start the program
main()
