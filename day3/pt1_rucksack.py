# pt1_rucksack.py -- adventOfCode2022 - day3 - part1

"""
algorithm
- (main)
    - declare (LETTERS) 'a..zA..Z'
    - build (letterValue) - dictionary a..z + A..Z keys and appropriate values
    - read input and assign to (items) list
    - declare (score) to 0
    - iterate through (items)
        - call item processor function on each item and assign return to (halves)
        - assign (Letter_values) to a..zA..Z 0 value dictionary
        - iterate through halves[1] str
            - if the letter is not in (halve[0])
                - add that (letter_value) to (score)
                - break
    - return (score)


- (itemProcessor) takes str and returns list with two strings
    - strip \n from string
    - get midpoint index of string
    - return list of two elements, first_half and second_half


- overkill and not necessary here, but saving from first pass:
```
import collections
compartment = collections.Counter(halves[0])
print(compartment)
for letter in halves[1]:
    if compartment[letter] != 0:
        score += letter_values[letter]
        sanity_check.append(letter)
        continue
```
"""

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def buildLetterValues(str: str, start: int) -> dict:
    letter_values = {}
    count = start
    for l in str:
        letter_values[l] = count
        count += 1

    return letter_values


def itemProcessor(line: str) -> list:
    line = line.strip()
    mid = int(len(line) / 2)

    return [line[:mid], line[mid:]]


def processInput(filename: str) -> list:
    input = open(filename, "r")

    return input.readlines()


def rucksackScore(input_file: str) -> int:
    letter_values = buildLetterValues(LETTERS, 1)
    items = processInput(input_file)
    score = 0

    for item in items:
        halves = itemProcessor(item)
        for letter in halves[1]:
            if letter in halves[0]:
                score += letter_values[letter]
                break

    return score


print(rucksackScore("rucksack_input.txt"))
