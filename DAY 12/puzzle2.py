DEBUG = False

# open the file
with open("input.txt", "r") as heightmap:
    data = heightmap.read()

# split heightmap into lines
heightmap_lines = [list(s) for s in data.split("\n")]

if DEBUG:
    print("Heightmap:")
    for line in heightmap_lines:
        print(line)
        print("") if line == heightmap_lines[-1] else None

# initialize the length of the heightmap and the
# width of the heightmap (length of the first line
# of the heightmap, because it's a square)
length_of_heightmap = len(heightmap_lines)
width_of_heightmap = len(heightmap_lines[0])

# initialize the matrix to check if a position has been visited
visited = [[False] * width_of_heightmap for i in range(length_of_heightmap)]

if DEBUG:
    print("visited: ")
    for i in range(length_of_heightmap):
        print(visited[i])
    print("")

# initialize the starting(s) and ending positions
starts = (0, 0, 0)
end = (0, 0)

# initialize the queue
queue = [starts]

# find the starting position and the ending position
for i in range(length_of_heightmap):
    for j in range(width_of_heightmap):
        # if the current position is the starting position
        if heightmap_lines[i][j] == "S" or heightmap_lines[i][j] == "a":
            # set the starting position
            starts = (i, j, 0)
            # append the starting position to the queue
            queue.append(starts)
            # mark the starting position as visited
            visited[i][j] = True
            # replace the starting position with the lowest height
            heightmap_lines[i][j] = "a"
        # if the current position is the ending position
        elif heightmap_lines[i][j] == "E":
            # set the ending position
            end = (i, j)
            # replace the ending position with the highest height
            heightmap_lines[i][j] = "z"


# initialize the fewest number of steps to reach the end
steps = -1

if DEBUG:
    print("visited: ")
    for i in range(length_of_heightmap):
        print(visited[i])
    print("")

while queue:
    # get the current position
    head = queue.pop(0)
    # get the current position's coordinates
    x, y, s = head

    # if the current position is the ending position
    if (x, y) == end:
        steps = s
        break

    # check the positions above, below, to the left, and to the right
    for (next_x, next_y) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        # get the next position's coordinates
        new_x = x + next_x
        new_y = y + next_y

        # if the next position is within the heightmap
        if 0 <= new_x < length_of_heightmap and 0 <= new_y < width_of_heightmap:
            # if the next position has not been visited and the next position is equal
            # to or higher than 1 unit the current position
            if not visited[new_x][new_y] and ord(heightmap_lines[new_x][new_y]) <= ord(heightmap_lines[x][y]) + 1:
                # add the next position to the queue
                queue.append((new_x, new_y, s + 1))
                # mark the next position as visited
                visited[new_x][new_y] = True

                if DEBUG:
                    print("new_x: " + str(new_x), "new_y: " + str(new_y), "s: " + str(s + 1))
                    print("visited: ")
                    for i in range(length_of_heightmap):
                        print(visited[i])
                    print("")

# print the answer
print(steps)
