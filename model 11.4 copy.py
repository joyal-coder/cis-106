def out_the_door(msrp, make, model, electric):
    if electric.upper() == "Y":
        discount = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        discount = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount = 0.15
    else:
        discount = 0.05

    discounted = msrp * (1 - discount)
    total = discounted * 1.07

    return total


total_msrp = 0
total_sales = 0

while True:
    answer = input("Do you want to enter a vehicle? (Yes/No): ")

    if answer.lower() != "yes":
        break

    make = input("Make: ")
    model = input("Model: ")
    electric = input("Electric Vehicle (Y/N): ")
    msrp = float(input("MSRP: "))

    sales_price = out_the_door(msrp, make, model, electric)

    print("Sales Price:", round(sales_price, 2))
    print()

    total_msrp += msrp
    total_sales += sales_price

print("Total MSRP:", round(total_msrp, 2))
print("Total Sales Price:", round(total_sales, 2))
