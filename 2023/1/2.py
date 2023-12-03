import typing as t


INPUT_FILE_NAME = "input.txt"

STR_TO_DIGIT = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def parse_input() -> t.List[str]:
    input_list = []

    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            input_list.append(line)

    return input_list


def get_digit_from_str(input_str: str) -> int:
    digit_index_map = {}

    for i in range(len(input_str)):
        if input_str[i].isdigit():
            digit_index_map[i] = int(input_str[i])
            continue

        for str_digit in STR_TO_DIGIT.keys():
            index_str_digit = input_str.find(str_digit, i)

            if index_str_digit != -1:
                digit_index_map[index_str_digit] = STR_TO_DIGIT[str_digit]

    first_digit = digit_index_map[min(digit_index_map)]
    last_digit = digit_index_map[max(digit_index_map)]

    return int(f"{first_digit}{last_digit}")


def main():
    input_list = parse_input()

    coordinator = 0

    for line in input_list:
        one_coordinator = get_digit_from_str(line)

        coordinator += one_coordinator

    print(coordinator)


if __name__ == "__main__":
    main()
