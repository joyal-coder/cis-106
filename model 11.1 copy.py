def compute_total(qty, price):
    total = qty * price
    if total > 10000:
        total *= 0.90   # 10% discount
    return total


grand_total = 0

while True:
    qty = input("Enter quantity (or Q to quit): ")

    if qty.upper() == "Q":
        break

    qty = float(qty)
    price = float(input("Enter unit price: "))

    ext_price = compute_total(qty, price)

    print("Quantity:", qty)
    print("Price:", price)
    print("Extended Price:", round(ext_price, 2))
    print()

    grand_total += ext_price

print("Total Extended Price:", round(grand_total, 2))
