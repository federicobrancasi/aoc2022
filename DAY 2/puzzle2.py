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

    # if player1 chose rock
    if player1 == "A":  # rock
        if player2 == "X":  # lose
            score += 3  # play scissors
        elif player2 == "Y":  # draw
            score += 4  # play rock
        elif player2 == "Z":  # win
            score += 8  # play paper
    # if player1 chose paper
    elif player1 == "B":  # paper
        if player2 == "X":  # lose
            score += 1  # play rock
        elif player2 == "Y":  # draw
            score += 5  # play paper
        elif player2 == "Z":  # win
            score += 9  # play scissors
    # if player1 chose scissors
    elif player1 == "C":  # scissors
        if player2 == "X":  # lose
            score += 2  # play paper
        elif player2 == "Y":  # draw
            score += 6  # play scissors
        elif player2 == "Z":  # win
            score += 7  # play rock

# print the score
print(score)

# close the file
file.close()
