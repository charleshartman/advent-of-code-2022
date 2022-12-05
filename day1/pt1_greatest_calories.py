# pt1_greatest_calories.py -- adventOfCode2022 - day1 - part1


def process_input(filename: str) -> list:
    input = open(filename, "r")
    return input.readlines()


def get_most_calories(input_file: str) -> int:
    items = process_input(input_file)
    greatest_elf = 0
    current_elf = 0

    for item in items:
        item = item.strip()
        if not item:
            if current_elf > greatest_elf:
                greatest_elf = current_elf
            current_elf = 0
        else:
            current_elf += int(item)

    return greatest_elf


print(get_most_calories("elves_input.txt"))
