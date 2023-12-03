INPUT_FILE_NAME = "input.txt"


def parse_input() -> list[list[str]]:
    symbols_list = []

    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            symbols_line_list = ["."]

            for char in line.strip():
                symbols_line_list.append(char)

            symbols_line_list.append(".")
            symbols_list.append(symbols_line_list)

    dot_list = []
    for _ in range(len(symbols_list[0])):
        dot_list.append(".")

    symbols_list.insert(0, dot_list)
    symbols_list.append(dot_list)

    return symbols_list
