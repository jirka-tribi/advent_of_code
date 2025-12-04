import typing as t
import copy

INPUT_FILE_NAME = "input.txt"

def parse_input() -> t.Iterator[str]:
    with open(INPUT_FILE_NAME, "r") as f:
        for line in f:
            yield line.strip()


def prepare_rolls_array() -> list[list[str]]:
    rolls_array = []

    for line in parse_input():
        line_list = ["."]
        for char in line:
            line_list.append(char)

        line_list.append(".")
        rolls_array.append(line_list)

    empty_line = []
    for _ in range(len(rolls_array[0])):
        empty_line.append(".")

    rolls_array.insert(0, empty_line)
    rolls_array.append(empty_line)

    return rolls_array


def find_neighbor_rolls(rolls_array: list[list[str]], i: int, j: int) -> int:
    count = 0
    for m in range(i - 1, i + 2):
        for n in range(j - 1, j + 2):
            if m == i and n == j:
                continue

            if rolls_array[m][n] == "@":
                count += 1

    return count

def check_rolls_array(rolls_array: list[list[str]]) -> tuple[list[list[str]], int]:
    new_array = copy.deepcopy(rolls_array)

    counter = 0
    for i in range(1, len(rolls_array) - 1):
        for j in range(1, len(rolls_array[0]) - 1):
            if rolls_array[i][j] == ".":
                continue

            count = find_neighbor_rolls(rolls_array, i, j)

            if count < 4:
                new_array[i][j] = "."
                counter += 1

    return new_array, counter


def main() -> None:
    counter_1 = 0
    is_done_1 = False
    counter_2 = 0

    rolls_array = prepare_rolls_array()

    while True:
        rolls_array, count = check_rolls_array(rolls_array)

        if not is_done_1:
            counter_1 = count
            is_done_1 = True

        if count == 0:
            break

        counter_2 += count

    print(counter_1)
    print(counter_2)


if __name__ == "__main__":
    main()