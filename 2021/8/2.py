from typing import List
import itertools

INPUT_FILE_NAME = "input.txt"

ZERO_INDEX = [0, 1, 2, 4, 5, 6]
ONE_INDEX = [2, 5]
TWO_INDEX = [0, 2, 3, 4, 6]
THREE_INDEX = [0, 2, 3, 5, 6]
FOUR_INDEX = [1, 2, 3, 5]
FIVE_INDEX = [0, 1, 3, 5, 6]
SIX_INDEX = [0, 1, 3, 4, 5, 6]
SEVEN_INDEX = [0, 2, 5]
EIGHT_INDEX = [0, 1, 2, 3, 4, 5, 6]
NINE_INDEX = [0, 1, 2, 3, 5, 6]

ALL_INDEXES = [
    ZERO_INDEX,
    ONE_INDEX,
    TWO_INDEX,
    THREE_INDEX,
    FOUR_INDEX,
    FIVE_INDEX,
    SIX_INDEX,
    SEVEN_INDEX,
    EIGHT_INDEX,
    NINE_INDEX,
]

PERM_PATTERN = "abcdefg"


def generate_all_options():
    options = []

    for perm in itertools.permutations(PERM_PATTERN):
        option = []
        for number in ALL_INDEXES:
            temp_option = ""
            for index in number:
                temp_option += perm[index]

            sorted_temp = sorted(temp_option)
            option.append("".join(sorted_temp))

        options.append(option)

    return options


def split_and_sort_numbers(input_numbers: str):
    splited = input_numbers.split(" ")

    numbers = []
    for item in splited:
        sorted_numbers = sorted(item)
        numbers.append("".join(sorted_numbers))

    return numbers


def parse_input(file_name: str) -> List[List[List[str]]]:
    input_numbers = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            split_input = line.strip("\n").split(" | ")

            example = split_and_sort_numbers(split_input[0])
            result = split_and_sort_numbers(split_input[1])

            input_numbers.append([example, result])

    return input_numbers


def parse_numbers_from_option(numbers, option) -> int:
    result = ""
    for number in numbers:
        result += str(option.index(number))

    return int(result)


def main():

    input_numbers = parse_input(INPUT_FILE_NAME)
    all_options = generate_all_options()

    sum_results = 0

    for list_numbers in input_numbers:
        for option in all_options:
            found = True
            for number in list_numbers[0]:
                if number not in option:
                    found = False

            if found:
                sum_results += parse_numbers_from_option(list_numbers[1], option)
                break

    print(sum_results)


if __name__ == "__main__":
    main()
