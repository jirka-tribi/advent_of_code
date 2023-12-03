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


def get_gears_multiple(i_pos: int, j_pos: int, symbols_map: list[list[str]]) -> int:
    gears_multiple = 0

    first_gear = None
    second_gear = None

    for m in range(i_pos - 1, i_pos + 2):
        if m < 0:
            continue

        first_char_in_line = True

        for n in range(j_pos - 1, j_pos + 2):
            if n < 0:
                first_char_in_line = False
                continue

            try:
                char_to_check = symbols_map[m][n]
            except IndexError:
                continue

            if char_to_check.isdigit():
                try:
                    prev_char = symbols_map[m][n - 1]
                except IndexError:
                    prev_char = ""

                if not first_char_in_line and prev_char.isdigit():
                    continue

                char_digit = char_to_check
                if first_char_in_line:
                    if n != 0:
                        for k in range(1, 10):
                            if (n - k) < 0:
                                break

                            try:
                                previous_char = symbols_map[m][n - k]
                            except IndexError:
                                break

                            if previous_char.isdigit():
                                char_digit = previous_char + char_digit
                            else:
                                break

                        for k in range(1, 10):
                            try:
                                next_char = symbols_map[m][n + k]
                            except IndexError:
                                break

                            if next_char.isdigit():
                                char_digit = char_digit + next_char
                            else:
                                break
                else:
                    for k in range(1, 10):
                        try:
                            next_char = symbols_map[m][n + k]
                        except IndexError:
                            break

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

    return gears_multiple


def main():
    sum_gears = 0

    symbols_list = parse_input()

    for i in range(len(symbols_list)):
        for j in range(len(symbols_list[i])):
            char = symbols_list[i][j]

            if char == "*":
                sum_gears += get_gears_multiple(i, j, symbols_list)

    print(sum_gears)


if __name__ == "__main__":
    main()
