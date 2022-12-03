# function get_priority for getting the priority of the given character
def get_priority(character):
    # if the character is a lower case letter then return its ascii value - 96
    if character.islower():
        return ord(character) - 96
    # if the character is an upper case letter then return its ascii value - 38
    elif character.isupper():
        return ord(character) - 38


# initialize the sum of the priorities
priority_sum = 0

# open the file
with open('input.txt') as f:
    # read the lines of the file
    lines = f.readlines()

    # for each line
    for line in lines:
        # get the length of the line
        length = len(line)
        # get the first half of the line
        first_half = line[:length // 2]
        # get the second half of the line
        second_half = line[length // 2:]

        # for each character in the first half
        for char in first_half:
            # if the character is in the second half
            if char in second_half:
                # sum the priorities
                priority_sum += get_priority(char)
                # break the loop
                break

# print the sum
print(priority_sum)

# close the file
f.close()
