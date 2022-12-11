from dataclasses import dataclass
import re

DEBUG = False


# monkey dataclass to store data
@dataclass
class Monkey:
    items: list[int]
    operation: str
    divisible_by: int
    targets: tuple[int, int]


# parse monkey from instructions
def parse_monkey(instructions):
    # create a list of monkeys
    monkeys: list[Monkey] = []
    # for each instruction create a monkey and add it to the list
    for i, monkey in enumerate(instructions.split("\n\n")):
        lines = monkey.splitlines()
        monkeys.append(
            Monkey(
                # get the items from the first line
                get_ints_from_instructions(lines[1]),
                # get the operation from the second line
                lines[2].split(" = ")[1],
                # get the divisible by number from the third line
                get_ints_from_instructions(lines[3])[0],
                # get the targets from the fourth line
                (
                    get_ints_from_instructions(lines[5])[0],
                    get_ints_from_instructions(lines[4])[0],
                ),
            )
        )
    # return the list of monkeys
    return monkeys


# get integers from every instruction
def get_ints_from_instructions(instruction):
    return list(map(int, re.findall(r"-?[0-9]+", instruction)))


# open the file
file = open("input.txt", "r")

# create a list of monkeys from the instructions in the file
monkeys = parse_monkey(file.read())

if DEBUG:
    print(monkeys)

# for each monkey in the list create a list of items
# that they are possessing (initially 0)
objects_for_each_monkey = [0] * len(monkeys)

# 20 rounds
for _ in range(20):
    # for each monkey
    for i, monkey in enumerate(monkeys):
        # for each item in the monkey's possession
        for item in monkey.items:
            objects_for_each_monkey[i] += 1

            # evaluate the operation
            worry_level = eval(monkey.operation.replace("old", str(item)))

            # divide by 3 the worry level
            worry_level = worry_level // 3

            # items with a certain worry level are thrown to
            # the monkeys that are in the target range
            # (this based on the monkey's divisible by number)
            monkeys[
                monkey.targets[worry_level % monkey.divisible_by == 0]
            ].items.append(worry_level)

        # delete the items from the monkey's possession
        # after they have been distributed
        monkey.items.clear()

# sort the items in each monkey's possession
# from smallest to largest
objects_for_each_monkey.sort()

if DEBUG:
    print("objects for every monkey: ", objects_for_each_monkey)

# get the multiplication of the
# two monkeys with the most items
answer = objects_for_each_monkey[-1] * objects_for_each_monkey[-2]

# print the answer
print(answer)
