DEBUG = False

# read input
with open('input.txt', 'r') as f:
    commands = f.read().splitlines()
    commands = [command.split(' ') for command in commands]

if DEBUG:
    print('commands:', commands)

# initialize the cycle and the value of the X register
cycle = 1
X = 1

# initialize the list of the intensities of the signals
signals_strengths = []

# loop over the commands
for instruction in commands:

    if DEBUG:
        print('cycle:', cycle, 'X:', X, 'signals strength:', signals_strengths)

    # if the cycle is the number 20, 60, 100, 140, 180 or 220
    if cycle in [20, 60, 100, 140, 180, 220]:
        # add the value of the X register * number of cycles
        # to the list of the intensities of the signals
        signals_strengths.append(cycle * X)

    # if the command is 'addx'
    if instruction[0] == 'addx':
        # if the next cycle is the number 20, 60, 100, 140, 180 or 220
        if cycle + 1 in [20, 60, 100, 140, 180, 220]:
            # add the value of the X register * number of cycles + 1
            # to the list of the intensities of the signals
            signals_strengths.append((cycle + 1) * X)
        # update the value of the cycle
        cycle += 2
        # update the value of the X register
        X += int(instruction[1])

    # if the command is 'noop'
    elif instruction[0] == 'noop':
        # update the value of the cycle
        cycle += 1

# initialize the sum of the signals strengths
sum_signals_strengths = sum(signals_strengths)

# print the answer
print(sum_signals_strengths)
