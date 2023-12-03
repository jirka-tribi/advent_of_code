INPUT_FILE_NAME = "input.txt"


def parse_input() -> list[list[str]]:
    symbols_list = []

    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            symbols_line_list = []

            for char in line.strip():
                symbols_line_list.append(char)

            symbols_list.append(symbols_line_list)

    return symbols_list


def test_digit_in_map(char_digit: str, i_pos: int, j_pos: int, symbols_map: list[list[str]]):
    correct_digit = False

    for m in range(i_pos - 1, i_pos + 2):
        if m < 0:
            continue

        for n in range(j_pos - 1, j_pos + len(char_digit) + 1):
            if n < 0:
                continue

            try:
                char_to_check = symbols_map[m][n]
            except IndexError:
                continue

            if char_to_check.isdigit():
                continue

            if char_to_check != ".":
                correct_digit = True

    return correct_digit


def main():
    sum_digits = 0

    symbols_list = parse_input()

    for i in range(len(symbols_list)):
        for j in range(len(symbols_list[i])):
            char = symbols_list[i][j]
            if char.isdigit():
                if j != 0:
                    previous_char = symbols_list[i][j - 1]
                    if previous_char.isdigit():
                        continue

                for k in range(1, 10):
                    try:
                        next_char = symbols_list[i][j + k]
                    except IndexError:
                        break

                    if next_char.isdigit():
                        char += next_char
                    else:
                        break

                print("Checking %s" % char)
                if test_digit_in_map(char, i, j, symbols_list):
                    print("OK")
                    sum_digits += int(char)

    print(sum_digits)


if __name__ == "__main__":
    main()
