# Problem 2

quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10.00
elif quantity >= 5000:
    price = 20.00
else:
    price = 30.00

extended_price = quantity * price
tax = extended_price * 0.07
total = extended_price + tax

print("\nWidget Order Summary")
print(f"{'Extended Price:':20}${extended_price:>12.2f}")
print(f"{'Tax:':20}${tax:>12.2f}")
print(f"{'Total:':20}${total:>12.2f}")

