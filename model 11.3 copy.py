def forecast(month, sales):
    month = month.lower()

    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    else:
        percent = 0.25

    return sales * (1 + percent)


while True:
    answer = input("Do you want to enter data? (Yes/No): ")

    if answer.lower() != "yes":
        break

    last_name = input("Last name: ")
    month = input("Month: ")
    sales = float(input("Sales: "))

    next_month = forecast(month, sales)

    print("Employee:", last_name)
    print("Forecast Sales:", round(next_month, 2))
    print()
