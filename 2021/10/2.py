from typing import List, Dict

INPUT_FILE_NAME = "input.txt"

PAIRS: Dict[str, int] = {"(": 1, "[": 2, "{": 3, "<": 4}


def parse_input(file_name: str) -> List[str]:
    input_syntax = []

    with open(file_name, "r") as f:
        for line in f.readlines():
            input_syntax.append(line.strip("\n"))

    return input_syntax


def delete_pairs(syntax: str) -> str:
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

    return syntax


def is_corrupted(syntax: str) -> bool:
    for item in syntax:
        if item in ")]}>":
            return True

    return False


def count_score(syntax: str) -> int:
    count = 0
    for item in syntax[::-1]:
        count *= 5
        count += PAIRS[item]

    return count


def main():
    counts = []
    input_syntax = parse_input(INPUT_FILE_NAME)
    for syntax in input_syntax:
        new_syntax = delete_pairs(syntax)
        if not is_corrupted(new_syntax):
            counts.append(count_score(new_syntax))

    counts.sort()
    print(counts[len(counts) // 2])


if __name__ == "__main__":
    main()
