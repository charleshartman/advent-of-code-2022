# pt1_rucksack.py -- adventOfCode2022 - day3 - part1


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def build_letter_values(str: str, start: int) -> dict:
    letter_values = {}
    count = start
    for l in str:
        letter_values[l] = count
        count += 1

    return letter_values


def item_processor(line: str) -> list:
    line = line.strip()
    mid = int(len(line) / 2)

    return [line[:mid], line[mid:]]


def process_input(filename: str) -> list:
    input = open(filename, "r")

    return input.readlines()


def rucksack_score(input_file: str) -> int:
    letter_values = build_letter_values(LETTERS, 1)
    items = process_input(input_file)
    score = 0

    for item in items:
        halves = item_processor(item)
        for letter in halves[1]:
            if letter in halves[0]:
                score += letter_values[letter]
                break

    return score


print(rucksack_score("rucksack_input.txt"))
