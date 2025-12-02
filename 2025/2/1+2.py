import typing as t
from pathlib import Path

INPUT_FILE_NAME = "input.txt"

counter_1 = 0
counter_2 = 0

def parse_input() -> t.Iterator[tuple[int, int]]:
    content = Path(INPUT_FILE_NAME).read_text().replace("\n", "").strip()

    for range_ in content.split(","):
        start, end = range_.split("-")
        yield int(start), int(end)

def is_invalid_1(number: str) -> bool:
    if len(number) % 2 != 0:
        return False

    mid = len(number) // 2
    return number[:mid] == number[mid:]


def is_invalid_2(number: str) -> bool:
     doubled = number + number
     return number in doubled[1:-1]


def main() -> None:
    checksum_1 = 0
    checksum_2 = 0

    for start, end in parse_input():
        for number in range(start, end + 1):
            number_str = str(number)

            if is_invalid_1(number_str):
                checksum_1 += number

            if is_invalid_2(number_str):
                checksum_2 += number

    print(checksum_1)
    print(checksum_2)

if __name__ == "__main__":
    main()