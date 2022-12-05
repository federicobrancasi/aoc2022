# create the array of the crates
array = []
for i in range(9):
    array.append([])

# initialize the index of the array
index = 0
# initialize the var for reading the input file
read_only_the_first_10_lines_and_skip_the_last_2 = 0

# open the file
with open('input.txt') as f:
    # read the lines
    lines = f.readlines()
    # print(lines)

    # for each line
    for line in lines:
        # if the line is one of the first 10 lines
        if read_only_the_first_10_lines_and_skip_the_last_2 != 10:
            # and if the line is not the last 2 lines of the first 10 lines
            if read_only_the_first_10_lines_and_skip_the_last_2 != 8 and read_only_the_first_10_lines_and_skip_the_last_2 != 9:
                # remove "\n" from the line
                line = line.replace("\n", "")
                # every 4 spaces there could possibly be an element of the array
                for i in range(0, len(line), 4):
                    # get the element
                    element = line[i:i + 4].replace(" ", "")
                    # if the element is not empty
                    if element != "":
                        # add the element to the array
                        element = element.replace("[", "").replace("]", "")
                        array[index].append(element)
                    # increment the index of the array
                    index += 1
                # reset the index of the array for each line
                index = 0
            read_only_the_first_10_lines_and_skip_the_last_2 += 1
        else:
            # if the line is after the first 10 lines
            # save the instructions for moving the crates
            instruction = [int(s) for s in line.split() if s.isdigit()]

            # the first number is the number of the crate to move
            number_of_objects = instruction[0]
            # the second number is the array from which the crate will be moved
            index_first_array = instruction[1]
            # the third number is the array to which the crate will be moved
            index_second_array = instruction[2]
            # move the crates from the first array to the second array
            for i in range(number_of_objects):
                array[index_second_array - 1].insert(0, array[index_first_array - 1][number_of_objects - 1])
                array[index_first_array - 1].pop(number_of_objects - 1)
                # decrement the number of crates to move because we moved one crate
                number_of_objects -= 1

# for each pile append the first crate to the message
message = ''.join(s[0] for s in array[0:])

# print the message
print(message)

# close the file
f.close()
