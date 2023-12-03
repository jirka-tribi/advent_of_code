from c import parse_input


def get_gears_multiple(i_pos: int, j_pos: int, symbols_map: list[list[str]]) -> int:
    first_gear = None
    second_gear = None

    for m in range(i_pos - 1, i_pos + 2):
        first_char_in_line = True

        for n in range(j_pos - 1, j_pos + 2):
            char_to_check = symbols_map[m][n]

            if char_to_check.isdigit():
                prev_char = symbols_map[m][n - 1] if (n - 1) >= 0 else ""

                if not first_char_in_line and prev_char.isdigit():
                    continue

                char_digit = char_to_check

                if first_char_in_line:
                    for k in range(1, 10):
                        previous_char = symbols_map[m][n - k]
                        if previous_char.isdigit():
                            char_digit = previous_char + char_digit
                        else:
                            break

                for k in range(1, 10):
                    next_char = symbols_map[m][n + k]
                    if next_char.isdigit():
                        char_digit = char_digit + next_char
                    else:
                        break

                if not first_gear:
                    first_gear = int(char_digit)
                else:
                    second_gear = int(char_digit)

            first_char_in_line = False

    if first_gear and second_gear:
        return first_gear * second_gear

    return 0


def main():
    sum_gears = 0

    symbols_list = parse_input()

    for i in range(1, len(symbols_list) - 1):
        for j in range(1, len(symbols_list[i]) - 1):
            char = symbols_list[i][j]

            if char == "*":
                sum_gears += get_gears_multiple(i, j, symbols_list)

    print(sum_gears)


if __name__ == "__main__":
    main()
