# Program 4

file = open("orders.txt", "r")

total = 0
count = 0

while True:
    item = file.readline().strip()

    if item == "":
        break

    quantity = int(file.readline())
    price = float(file.readline())

    extended = quantity * price

    total += extended
    count += 1

    print("Item:", item)
    print("Quantity:", quantity)
    print("Price: $", format(price, ".2f"))
    print("Extended Price: $", format(extended, ".2f"))
    print()

file.close()

average = total / count

print("Total Orders: $", format(total, ".2f"))
print("Number of Orders:", count)
print("Average Order: $", format(average, ".2f"))
