# pt1_camp_cleanup.py -- adventOfCode2022 - day4 - part1


def process_input(filename: str) -> list:
    input = open(filename, "r")

    return input.readlines()


def overlap_checker(items: list) -> bool:
    if (items[0][0] >= items[1][0] and items[0][1] <= items[1][1]) or (
        items[1][0] >= items[0][0] and items[1][1] <= items[0][1]
    ):
        return True


def find_section_overlap(input_file: str) -> int:
    pairs = process_input(input_file)
    overlap = 0

    for pair in pairs:
        pair = pair.strip().split(",")
        processed = []
        for sections in pair:
            sections = sections.split("-")
            for section in sections:
                section = int(section)
                processed.append(section)
        processed = [processed[0], processed[1]], [processed[2], processed[3]]

        if overlap_checker(processed):
            overlap += 1

    return overlap


print(find_section_overlap("camp_cleanup.txt"))
