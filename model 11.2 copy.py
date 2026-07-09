def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats


count = 0

while True:
    last_name = input("Enter last name (or Q to quit): ")

    if last_name.upper() == "Q":
        break

    hits = int(input("Enter hits: "))
    at_bats = int(input("Enter at bats: "))

    avg = batting_average(hits, at_bats)

    print("Player:", last_name)
    print("Batting Average:", round(avg, 3))
    print()

    count += 1

print("Number of players entered:", count)
