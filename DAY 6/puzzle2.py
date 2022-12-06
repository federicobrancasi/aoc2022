# open the file
file = open("input.txt", "r")

# read whole file to a string
data = file.read()

# loop through the string until you find a
# sequence of 14 characters that are all different
for i in range(len(data) - 14):
    # if all characters are different
    if len(set(data[i:i + 14])) == 14:
        print("FOUND: " + data[i:i + 14])
        # print the position of the last character
        print(i + 14)
        break

# close the file
file.close()
