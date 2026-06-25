# Problem 1

quantity = int(input("Enter quantity: "))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print("\nItem Purchase Summary")
print(f"{'Quantity:':20}{quantity:>10}")
print(f"{'Unit Price:':20}${unit_price:>9.2f}")
print(f"{'Extended Price:':20}${extended_price:>9.2f}")
print(f"{'Tax:':20}${tax:>9.2f}")
print(f"{'Total:':20}${total:>9.2f}")

