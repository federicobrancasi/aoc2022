# open the file
file = open("input.txt", "r")

# initialize the sum and the greatest sum
sum = 0
greatest_sum = 0

# read the file line by line
for line in file:
    # if the line is not blank
    if line != "\n":
        # add the number to the sum
        sum += int(line)
    # if the line is blank
    else:
        # if the sum is greater than the greatest sum
        if sum > greatest_sum:
            # update the greatest sum
            greatest_sum = sum
        # reset the sum
        sum = 0

# print the greatest sum
print(greatest_sum)

# close the file
file.close()
