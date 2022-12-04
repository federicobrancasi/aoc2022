def create_array(string):
    # split the string by the - character
    split_string = string.split("-")
    # create an array with the numbers in the range
    array = range(int(split_string[0]), int(split_string[1]) + 1)
    # return the array
    return array


# initialize the sum of the priorities
pair_sum = 0

# open the file
with open('input.txt') as f:
    # read the lines
    lines = f.readlines()

    # iterate over the lines
    for line in lines:
        # remove "\n" from the line
        line = line.replace("\n", "")

        # check if the two arrays overlaps each other
        if set(create_array(line.split(",")[0])).intersection(create_array(line.split(",")[1])):
            # add one to the pair sum
            pair_sum += 1

# print the sum
print(pair_sum)

# close the file
f.close()
