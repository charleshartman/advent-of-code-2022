# pt2_rps.py -- adventOfCode2022 - day2 - part2

OUTCOMES = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}


def processInput(filename: str) -> list:
    input = open(filename, "r")
    return input.readlines()


def totalScore(inputFile: str) -> int:
    items = processInput(inputFile)
    score = 0

    for item in items:
        score += OUTCOMES[item.strip()]

    return score


print(totalScore("rps_input.txt"))
