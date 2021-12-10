from typing import List

INPUT_FILE_NAME = "input.txt"


def parse_input(file_name: str) -> List[str]:
    second_numbers = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            second_numbers.append(line.strip("\n").split(" | ")[1])

    return second_numbers


def main():

    input_numbers = parse_input(INPUT_FILE_NAME)

    one = 0
    four = 0
    seven = 0
    eight = 0

    for numbers in input_numbers:
        for number in numbers.split(" "):
            if len(number) == 2:
                one += 1
            elif len(number) == 4:
                four += 1
            elif len(number) == 3:
                seven += 1
            elif len(number) == 7:
                eight += 1

    print(one + four + seven + eight)


if __name__ == "__main__":
    main()
