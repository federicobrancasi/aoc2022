DEBUG = False


# function to move to the current position
def move(pos, d):
    if d == "D":
        pos[0][1] += 1
    elif d == "U":
        pos[0][1] -= 1
    elif d == "L":
        pos[0][0] -= 1
    elif d == "R":
        pos[0][0] += 1
    return pos


# function to determine how many
# positions the tail has visited
def simulate_movement(moves):
    # define the array of the positions of the head and the tail (initially all 0)
    positions = [[0, 0] for _ in range(2)]

    # define the set of the visited positions
    # a set because it is faster to check if a position is already visited
    # (a set is a collection of unique elements)
    visited = set()

    # for every move
    for motion in moves:
        # initialize the direction and the length of the move (the number of steps)
        direction, steps = motion.split()

        if DEBUG:
            print("Current Motion ->", "direction:", direction, " steps:", steps)

        # for every step
        for _ in range(int(steps)):

            if DEBUG:
                print("positions before: ", positions)

            # add the current position to the set of visited positions
            visited.add(tuple(positions[-1]))

            if DEBUG:
                print("visited: ", visited)

            # move the current position
            move(positions, direction)

            if DEBUG:
                print("positions after: ", positions, " pos[1:]", positions[1:])

            # for every pair of positions (head and tail)
            # numerated from 0, move the element to the next position
            for i, ((head_x, head_y), (tail_x, tail_y)) in enumerate(zip(positions, positions[1:])):

                if DEBUG:
                    print("i: ", i, "hx: ", head_x, "hy: ", head_y, "tx: ", tail_x, "ty: ", tail_y)

                # if the tail has to follow the head
                # which has moved to the right or to the left
                if abs(head_x - tail_x) > 1:
                    if DEBUG:
                        print("head moves to the right or left")
                    if head_x > tail_x:
                        tail_x += 1
                    else:
                        tail_x -= 1
                    # if the tail has to follow the head
                    # which has also moved up or down
                    if abs(head_y - tail_y) > 0:
                        if DEBUG:
                            print("head moves up or down X")
                        if head_y > tail_y:
                            tail_y += 1
                        else:
                            tail_y -= 1

                # if the tail has to follow the head
                # which has moved up or down
                elif abs(head_y - tail_y) > 1:
                    if DEBUG:
                        print("head moves up or down")
                    if head_y > tail_y:
                        tail_y += 1
                    else:
                        tail_y -= 1
                    # if the tail has to follow the head
                    # which has also moved to the right or to the left
                    if abs(head_x - tail_x) > 0:
                        if DEBUG:
                            print("head moves to the right or left X")
                        if head_x > tail_x:
                            tail_x += 1
                        else:
                            tail_x -= 1

                # update the position of the tail
                positions[i + 1][0] = tail_x
                positions[i + 1][1] = tail_y

            if DEBUG:
                print("\n")

    # add the position of the tail (last element of the positions)
    # to the set of visited positions
    visited.add(tuple(positions[-1]))

    # return the number of visited positions
    return len(visited)


# open the file
with open("input.txt") as f:

    # read the input and save it in a list
    directions_and_steps = f.read().splitlines()

    if DEBUG:
        print(directions_and_steps, "\n")

    # initialize the number of visited positions
    answer = simulate_movement(directions_and_steps)

    # print the answer
    print(answer)
