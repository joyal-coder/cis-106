# Problem 2: Stock Investment Calculator

# Input stock details
ticker = input("Enter the stock ticker symbol (e.g., MSFT): ").upper()
shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

# Compute total investment
amount_invested = shares * cost_per_share

# Display the result with dollar formatting
print(f"\nStock: {ticker}")
print(f"Total Amount Invested: ${amount_invested:.2f}")

