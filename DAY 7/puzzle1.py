from collections import defaultdict

DEBUG = False

# open the file
with open("input.txt") as f:
    # create a defaultdict (dictionary) of directories
    directories = defaultdict(int)

    # initialize the array to store the current directory
    current_directories = []

    # loop through each line
    for line in f.read().splitlines():
        if DEBUG:
            print(line)  # debug

        # if is a command and it's changing directory
        if line.startswith("$ cd"):
            # get the directory name
            directory = line.replace("$ cd ", "")
            # if the command is NOT cd .. add the directory to the list
            if directory != "..":
                current_directories.append(directory)
            # else remove the last directory from the list
            else:
                current_directories.pop()
            if DEBUG:
                print("CD COMMAND", current_directories, "\n")  # debug

        # if is a command and it's listing the files
        elif line.startswith("$ ls"):
            continue

        # if is not a command then, or it's a file or a directory
        else:
            if DEBUG:
                print("FILE", line.split()[0], "\n")  # debug
        try:
            # if it's a file
            directories["/".join(current_directories)] += int(line.split()[0])
        except ValueError:
            # if it's a directory
            pass

if DEBUG:
    print(directories)
    print(sorted(directories.keys(), key=lambda x: x.count("/"), reverse=True))

# loop through the directories (sorted by the number of /, so the deepest directories are first)
for directory in sorted(directories.keys(), key=lambda x: x.count("/"), reverse=True):
    if DEBUG:
        print("father directory:", "/".join(directory.split("/")[:-1]), "\n",
              "current directory dimension: ", directories[directory], "\n")   # debug
    # sum the size of the current directory to the father directory
    directories["/".join(directory.split("/")[:-1])] += directories[directory]

# sum all the sizes of the directories smaller than 100MB
answer = sum(s for s in directories.values() if s <= 100000)

# print the answer
print(answer)
