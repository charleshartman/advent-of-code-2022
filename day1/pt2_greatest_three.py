# pt2_greatest_three.py -- adventOfCode2022 - day1 - part2

"""
algorithm
- read input into list
- declare calories = []
- declare currentELf = 0

- iterate through list
    - strip item of newline
    - if item is False ('')
        - push value of current elf into elves carrying
        - currentElf = 0
    - else
        - convert item to number and add it to currentElf

- sort calories
- return the sum of the last three elements in calories
"""


def processInput(filename: str) -> list:
    input = open(filename, "r")
    return input.readlines()


def getMostCalories(inputFile: str) -> int:
    items = processInput(inputFile)
    calories = []
    currentElf = 0

    for item in items:
        item = item.strip()
        if not item:
            calories.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(item)

    calories.sort()
    return calories[-1] + calories[-2] + calories[-3]


print(getMostCalories("elves_input.txt"))
