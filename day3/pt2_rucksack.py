# pt2_rucksack.py -- adventOfCode2022 - day3 - part2


LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def build_letter_values(str: str, start: int) -> dict:
    letter_values = {}
    count = start
    for l in str:
        letter_values[l] = count
        count += 1

    return letter_values


def unique(line: str) -> str:
    line = line.strip()
    unique_letters = ""
    for letter in line:
        if letter not in unique_letters:
            unique_letters += letter

    return unique_letters


def process_input(filename: str) -> list:
    input = open(filename, "r")

    return input.readlines()


def make_groups(lines: list, step: int) -> list:
    groups = [lines[i : i + step] for i in range(0, len(lines), step)]

    return groups


def rucksack_score(input_file: str) -> int:
    letter_values = build_letter_values(LETTERS, 1)
    lines = process_input(input_file)
    groups = make_groups(lines, 3)
    score = 0

    for group in groups:
        keystring = unique(group[0])
        for letter in keystring:
            if letter in group[1] and letter in group[2]:
                score += letter_values[letter]

    return score


print(rucksack_score("rucksack_input.txt"))
