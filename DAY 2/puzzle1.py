# open the file
file = open("input.txt", "r")
# initialize the score
score = 0

# read the file line by line (corresponds to a single game)
for line in file:
    # save the player1's choice
    player1 = line[0]
    # save the player2's choice
    player2 = line[2]

    # points for the choices
    if player2 == "X":  # rock
        score += 1
    if player2 == "Y":  # paper
        score += 2
    if player2 == "Z":  # scissors
        score += 3

    # if player1 chose rock
    if player1 == "A":  # rock
        if player2 == "X":  # rock
            score += 3
        elif player2 == "Y":  # paper
            score += 6
        elif player2 == "Z":  # scissors
            score += 0
    # if player1 chose paper
    elif player1 == "B":  # paper
        if player2 == "X":  # rock
            score += 0
        elif player2 == "Y":  # paper
            score += 3
        elif player2 == "Z":  # scissors
            score += 6
    # if player1 chose scissors
    elif player1 == "C":  # scissors
        if player2 == "X":  # rock
            score += 6
        elif player2 == "Y":  # paper
            score += 0
        elif player2 == "Z":  # scissors
            score += 3

# print the score
print(score)

# close the file
file.close()
