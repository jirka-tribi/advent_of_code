import typing as t


INPUT_FILE_NAME = "input.txt"


def parse_input() -> t.List[str]:
    input_list = []

    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            input_list.append(line)

    return input_list


def get_firs_digit_from_str(input_str: str) -> int:
    for char in input_str:
        if char.isdigit():
            return int(char)


def main():
    input_list = parse_input()

    coordinator = 0

    for line in input_list:
        first_digit = get_firs_digit_from_str(line)
        last_digit = get_firs_digit_from_str(line[::-1])

        coordinator += int(f"{first_digit}{last_digit}")

    print(coordinator)


if __name__ == "__main__":
    main()
