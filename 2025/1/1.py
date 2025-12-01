import typing as t

INPUT_FILE_NAME = "test_input.txt"

def parse_input() -> t.Iterator[tuple[str, int]]:
    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.read().split("\n"):
            if not line:
                continue

            yield line[0], int(line[1:])

def correct_position(position: int) -> int:
    new_position = position

    if 0 <= position <= 99:
        return new_position

    if position < 0:
        new_position = 100 + position

    if position > 99:
        new_position = position - 100

    return correct_position(new_position)



def main() -> None:
    counter = 0
    position = 50

    for direction, count in parse_input():
        if direction == "L":
            position = position - count

        elif direction == "R":
            position = position + count

        position = correct_position(position)

        if position == 0:
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()