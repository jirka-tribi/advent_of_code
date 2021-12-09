from typing import Dict, List, Tuple


def parse_input(file_name: str) -> Tuple[List[Dict[str, int]], List[Dict[str, int]]]:
    coordinates = []
    coordinates_diagonal = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            coro_1, coro_2 = line.strip("\n").split(" -> ")
            x1, y1 = [int(item) for item in coro_1.split(",")]
            x2, y2 = [int(item) for item in coro_2.split(",")]

            if not (x1 == x2 or y1 == y2):
                if x1 > x2:
                    temp_x = x1
                    x1 = x2
                    x2 = temp_x
                    temp_y = y1
                    y1 = y2
                    y2 = temp_y
                coordinates_diagonal.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
                continue

            if x1 > x2:
                temp_x = x1
                x1 = x2
                x2 = temp_x

            if y1 > y2:
                temp_y = y1
                y1 = y2
                y2 = temp_y

            coordinates.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})

    return coordinates, coordinates_diagonal


def get_max_x_y(coordinates: List[Dict[str, int]]) -> Tuple[int, int]:
    x_max = 0
    y_max = 0

    for coro in coordinates:
        if coro["x1"] > x_max:
            x_max = coro["x1"]

        if coro["x2"] > x_max:
            x_max = coro["x2"]

        if coro["y1"] > y_max:
            y_max = coro["y1"]

        if coro["y2"] > y_max:
            y_max = coro["y2"]

    return x_max, y_max


def create_empty_map(x_max: int, y_max: int) -> List[List[int]]:
    empty_map = []
    for i in range(0, x_max + 1):
        temp_list = []
        for j in range(0, y_max + 1):
            temp_list.append(0)
        empty_map.append(temp_list)

    return empty_map


def main():
    file_input = "input.txt"

    coordinates, coordinates_diagonal = parse_input(file_input)
    x_max, y_max = get_max_x_y(coordinates)
    vent_map = create_empty_map(x_max, y_max)

    for coro in coordinates:
        x1 = coro["x1"]
        x2 = coro["x2"]
        y1 = coro["y1"]
        y2 = coro["y2"]

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                vent_map[i][j] += 1

    for coro_diagonal in coordinates_diagonal:
        x1 = coro_diagonal["x1"]
        x2 = coro_diagonal["x2"]
        y1 = coro_diagonal["y1"]
        y2 = coro_diagonal["y2"]

        j = y1
        for i in range(x1, x2 + 1):
            vent_map[j][i] += 1
            if y1 < y2:
                j += 1
            else:
                j -= 1

    counter = 0
    for coro_x in vent_map:
        for coro_y in coro_x:
            if coro_y > 1:
                counter += 1

    print(counter)


if __name__ == "__main__":
    main()
