def compute_discount(qty, price, rate):
    total = qty * price
    discount_amount = total * rate
    discounted_price = total - discount_amount

    return discount_amount, discounted_price


while True:
    qty = input("Enter quantity (or Q to quit): ")

    if qty.upper() == "Q":
        break

    qty = float(qty)
    price = float(input("Enter price: "))
    rate = float(input("Enter discount rate (example .10): "))

    discount, final_price = compute_discount(qty, price, rate)

    print("Quantity:", qty)
    print("Price:", price)
    print("Discount Amount:", round(discount, 2))
    print("Discounted Price:", round(final_price, 2))
    print()

