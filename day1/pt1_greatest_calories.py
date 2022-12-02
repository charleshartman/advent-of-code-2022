# pt1_greatest_calories.py -- adventOfCode2022 - day1 - part1

"""
algorithm
- read input into list
- declare greatestElf = 0
- declare currentElf = 0
- iterate through list
    - strip item of newline
    - if item is False ('')
        - if currentElf > greatestElf
            - greatestElf = currentElf
        - currentElf = 0
    - else
        - convert item to number and add it to currentElf
- return greatestElf
"""


def processInput(filename: str) -> list:
    input = open(filename, "r")
    return input.readlines()


def getMostCalories(inputFile: str) -> int:
    items = processInput(inputFile)
    greatestElf = 0
    currentElf = 0

    for item in items:
        item = item.strip()
        if not item:
            if currentElf > greatestElf:
                greatestElf = currentElf
            currentElf = 0
        else:
            currentElf += int(item)

    return greatestElf


print(getMostCalories("elves_input.txt"))
