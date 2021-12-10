from typing import List

INPUT_FILE_NAME = "input.txt"


def parse_input(file_name: str) -> List[List[int]]:
    lava_map = []

    with open(file_name, "r") as f:
        for line in f.readlines():
            lava_map_line = [10]
            for number in line.strip("\n"):
                lava_map_line.append(int(number))

            lava_map_line.append(10)
            lava_map.append(lava_map_line)

    lava_map.insert(0, [10] * len(lava_map[1]))
    lava_map.append([10] * len(lava_map[1]))

    return lava_map


def main():

    result = []
    lava_map = parse_input(INPUT_FILE_NAME)

    for i in range(1, len(lava_map) - 1):
        for j in range(1, len(lava_map[0]) - 1):
            is_deep = True
            point = lava_map[i][j]

            if point >= lava_map[i - 1][j]:
                is_deep = False

            if point >= lava_map[i + 1][j]:
                is_deep = False

            if point >= lava_map[i][j - 1]:
                is_deep = False

            if point >= lava_map[i][j + 1]:
                is_deep = False

            if is_deep:
                result.append(point)

    count = 0
    for item in result:
        count += item + 1

    print(count)


if __name__ == "__main__":
    main()
