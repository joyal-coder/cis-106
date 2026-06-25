# Problem 4

principal = float(input("Enter principal amount: "))
years = int(input("Enter years to maturity: "))

if principal > 100000 and years == 5:
    rate = 0.06
elif principal >= 50000 and principal <= 100000 and years == 10:
    rate = 0.05
elif principal >= 50000 and principal <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principal * rate

print("\nCD Investment Summary")
print(f"{'Principal:':20}${principal:>12.2f}")
print(f"{'Interest Rate:':20}{rate:>11.2%}")
print(f"{'1st Year Interest:':20}${interest:>12.2f}")
