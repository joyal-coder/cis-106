# Problem 6: Stock Value Return Calculator

# Input stock metrics
purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = float(input("Enter the quantity of stock shares: "))

# Compute the value change
value_change = (current_price - purchase_price) * quantity

# Display results based on whether it is a profit or loss
if value_change >= 0:
    print(f"Value Increase: ${value_change:.2f}")
else:
    print(f"Value Decrease: -${abs(value_change):.2f} (Losing money)")

