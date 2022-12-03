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

    # read 3 lines at a time (they identify a group)
    for line1, line2, line3 in zip(lines[::3], lines[1::3], lines[2::3]):
        # find the common character that appears in all 3 lines
        common_char = set(line1).intersection(line2, line3)
        # and eliminate the elements that are not letters (i.e. the newline character)
        common_char = [char for char in common_char if char.isalpha()]
        # if there is a common character (must be only one)
        if common_char:
            # sum the priorities
            priority_sum += get_priority(common_char[0])

# print the sum
print(priority_sum)

# close the file
f.close()
