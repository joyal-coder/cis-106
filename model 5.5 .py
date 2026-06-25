# Problem 5

tickets = int(input("Enter number of tickets: "))

if tickets >= 25:
    price_per_ticket = 50.00
elif tickets >= 10:
    price_per_ticket = 60.00
elif tickets >= 5:
    price_per_ticket = 70.00
else:
    price_per_ticket = 75.00

total_cost = tickets * price_per_ticket

print("\nConcert Ticket Summary")
print(f"{'Tickets:':20}{tickets:>10}")
print(f"{'Price Per Ticket:':20}${price_per_ticket:>9.2f}")
print(f"{'Total Cost:':20}${total_cost:>9.2f}")
