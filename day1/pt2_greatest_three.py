# pt2_greatest_three.py -- adventOfCode2022 - day1 - part2


def process_input(filename: str) -> list:
    input = open(filename, "r")
    return input.readlines()


def get_most_calories(input_file: str) -> int:
    items = process_input(input_file)
    calories = []
    current_elf = 0

    for item in items:
        item = item.strip()
        if not item:
            calories.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(item)

    calories.sort()
    return calories[-1] + calories[-2] + calories[-3]


print(get_most_calories("elves_input.txt"))
