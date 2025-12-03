import typing as t

INPUT_FILE_NAME = "input.txt"

def parse_input() -> t.Iterator[str]:
    with open(INPUT_FILE_NAME, "r") as f:
        for line in f:
            yield line.strip()


def find_correct_number(seq: str, digits: int) -> int:
    number = ""
    next_index = 0

    for i in range(digits, 0, -1):
        next_index, next_number = find_highest_number(seq, next_index, i)
        number = number + next_number

    return int(number)


def find_highest_number(seq: str, start: int, max_end: int) -> tuple[int, str]:
    highest = 0
    highest_index = 0

    for index in range(start, (len(seq) + 1) - max_end):
        number = int(seq[index])
        if number > highest:
            highest = number
            highest_index = index

    return highest_index + 1, str(highest)

def main() -> None:
    counter_1 = 0
    counter_2 = 0
    for line in parse_input():
        counter_1 += find_correct_number(line, 2)
        counter_2 += find_correct_number(line, 12)

    print(counter_1)
    print(counter_2)

if __name__ == "__main__":
    main()