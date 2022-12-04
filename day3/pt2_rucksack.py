# pt2_rucksack.py -- adventOfCode2022 - day3 - part2

"""
algorithm
- (main)
    - declare (LETTERS) 'a..zA..Z'
    - build (letterValue) - dictionary a..z + A..Z keys and appropriate values
    - read input and assign to (lines) list
    - break into 3 element subarrays [write (makeGroups) function]
    - declare (score) to 0
    - iterate through groups
        - call (unique) on first element to eliminate duplicates, assign
          to (keychain)
        - iterate through keychain
            - if letter is present in group[1] and group[2]
                - add that letter_value to score
        
    - return (score)


- (unique) takes str\n and returns string with duplicate letters removed
    - strip \n from string
    - build (unique_letters) without duplicate letters
    - return (unique_letters)

- (makeGroups) 
    - take master input list and slices into subarrays of given length
    - return array of subarrays
"""

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def buildLetterValues(str: str, start: int) -> dict:
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


def processInput(filename: str) -> list:
    input = open(filename, "r")

    return input.readlines()


def makeGroups(lines: list, step: int) -> list:
    groups = [lines[i : i + step] for i in range(0, len(lines), step)]

    return groups


def rucksackScore(input_file: str) -> int:
    letter_values = buildLetterValues(LETTERS, 1)
    lines = processInput(input_file)
    groups = makeGroups(lines, 3)
    score = 0

    for group in groups:
        keystring = unique(group[0])
        for letter in keystring:
            if letter in group[1] and letter in group[2]:
                score += letter_values[letter]

    return score


print(rucksackScore("rucksack_input.txt"))
