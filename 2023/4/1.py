import re

INPUT_FILE_NAME = "input.txt"


def parse_input() -> tuple[list[str], list[str]]:
    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            find_line = re.search(r"Card\s*\d*: (.*)", line)

            winning_numbers, all_numbers = find_line.group(1).split("|")

            yield [item for item in winning_numbers.strip().split(" ") if item], [
                item for item in all_numbers.strip().split(" ") if item
            ]


def get_matches_points(matches: int) -> int:
    if matches == 0:
        return 0

    if matches == 1:
        return 1

    points = 2
    for i in range(2, matches):
        points = points * 2

    return points


def main():
    worth_points = 0

    for winning_numbers, all_numbers in parse_input():
        matches = 0

        for number in winning_numbers:
            if number in all_numbers:
                matches += 1

        worth_points += get_matches_points(matches)

    print(worth_points)


if __name__ == "__main__":
    main()
