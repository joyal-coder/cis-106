# Problem 3

part_number = input("Enter part number: ")
quantity = int(input("Enter quantity: "))

if part_number == "10" or part_number == "55":
    unit_cost = 1.00
elif part_number == "99":
    unit_cost = 2.00
elif part_number == "80" or part_number == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00

total_cost = quantity * unit_cost

print("\nPart Order Summary")
print(f"{'Part Number:':20}{part_number:>10}")
print(f"{'Unit Cost:':20}${unit_cost:>9.2f}")
print(f"{'Total Cost:':20}${total_cost:>9.2f}")

