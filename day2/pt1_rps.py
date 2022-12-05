# pt1_rps.py -- adventOfCode2022 - day2 - part1

OUTCOMES = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}


def process_input(filename: str) -> list:
    input = open(filename, "r")
    return input.readlines()


def total_score(input_file: str) -> int:
    items = process_input(input_file)
    score = 0

    for item in items:
        score += OUTCOMES[item.strip()]

    return score


print(total_score("rps_input.txt"))
