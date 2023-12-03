from c import parse_input


def test_digit_in_map(char_digit: str, i_pos: int, j_pos: int, symbols_map: list[list[str]]):
    correct_digit = False

    for m in range(i_pos - 1, i_pos + 2):
        for n in range(j_pos - 1, j_pos + len(char_digit) + 1):
            char_to_check = symbols_map[m][n]

            if char_to_check.isdigit():
                continue

            if char_to_check != ".":
                correct_digit = True

    return correct_digit


def main():
    sum_digits = 0

    symbols_list = parse_input()

    for i in range(1, len(symbols_list) - 1):
        for j in range(1, len(symbols_list[i]) - 1):
            char = symbols_list[i][j]
            if char.isdigit():
                previous_char = symbols_list[i][j - 1]
                if previous_char.isdigit():
                    continue

                k = 1
                while symbols_list[i][j + k].isdigit():
                    char = char + symbols_list[i][j + k]
                    k += 1

                if test_digit_in_map(char, i, j, symbols_list):
                    sum_digits += int(char)

    print(sum_digits)


if __name__ == "__main__":
    main()
