# open the file
file = open("input_puzzle2.txt", "r")

# initialize the sum and the greatest sums
sum = 0
greatest_sums = [0, 0, 0]

# read the file line by line
for line in file:
    # if the line is not blank
    if line != "\n":
        # add the number to the sum
        sum += int(line)
    # if the line is blank
    else:
        # if the sum is greater than the greatest sums
        if sum > greatest_sums[0]:
            greatest_sums[0] = sum
            greatest_sums.sort()
        # reset the sum
        sum = 0

# print the greatest sums
print(greatest_sums[0] + greatest_sums[1] + greatest_sums[2])

# close the file
file.close()
