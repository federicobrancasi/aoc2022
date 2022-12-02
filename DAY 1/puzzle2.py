# open the file
file = open("input.txt", "r")

# create a list of the lines (calories) in the file
numbers = file.read().splitlines()
# initialize the current sum
current_sum = 0
# initialize the array of the sums
sums = []

# for each number in the list of numbers
for number in numbers:
    # add the number to the current sum if it is not blank
    if number != '':
        current_sum += int(number)
    # if the number is blank append the current sum to the array of sums
    else:
        sums.append(current_sum)
        current_sum = 0

# sort the array of sums
sums.sort()

# print the sum of the greatest 3 sums
print(sums[-1] + sums[-2] + sums[-3])

# close the file
file.close()

