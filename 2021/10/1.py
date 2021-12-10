from typing import List, Dict

INPUT_FILE_NAME = "input.txt"

PAIRS: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse_input(file_name: str) -> List[str]:
    input_syntax = []

    with open(file_name, "r") as f:
        for line in f.readlines():
            input_syntax.append(line.strip("\n"))

    return input_syntax


def count_corrupted(syntax: str) -> int:
    while True:
        found = False
        if "()" in syntax:
            syntax = syntax.replace("()", "", 1)
            found = True

        if "[]" in syntax:
            syntax = syntax.replace("[]", "", 1)
            found = True

        if "{}" in syntax:
            syntax = syntax.replace("{}", "", 1)
            found = True

        if "<>" in syntax:
            syntax = syntax.replace("<>", "", 1)
            found = True

        if not found:
            break

    for item in syntax:
        if item in PAIRS:
            return PAIRS[item]

    return 0


def main():
    count = 0
    input_syntax = parse_input(INPUT_FILE_NAME)
    for syntax in input_syntax:
        count += count_corrupted(syntax)

    print(count)


if __name__ == "__main__":
    main()
