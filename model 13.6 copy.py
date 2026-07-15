# Problem 6

players = {}

file = open("players.txt", "r")

for line in file:
    data = line.split()
    players[data[0]] = float(data[1])

file.close()

def display_players(player_dict):

    print("Player\t\tBatting Average")
    print("--------------------------------")

    for player in player_dict:
        print(player, "\t\t", format(player_dict[player], ".3f"))

display_players(players)

