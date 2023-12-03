import re

INPUT_FILE_NAME = "input.txt"


def parse_input() -> tuple[int, str]:
    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            find_line = re.search(r"Game \d*: (.*)", line)
            game_sets = find_line.group(1)

            yield game_sets


def find_color_in_game_set(color: str, game_set: str) -> int:
    find_color = re.search(r"(\d*) %s" % color, game_set)

    return int(find_color.group(1)) if find_color else 0


def main():
    cube_power = 0

    for game_sets in parse_input():
        red_count_total = 0
        blue_count_total = 0
        green_count_total = 0

        for game_set in game_sets.split(";"):
            red_count = find_color_in_game_set("red", game_set)
            blue_count = find_color_in_game_set("blue", game_set)
            green_count = find_color_in_game_set("green", game_set)

            if red_count > red_count_total:
                red_count_total = red_count

            if blue_count > blue_count_total:
                blue_count_total = blue_count

            if green_count > green_count_total:
                green_count_total = green_count

        cube_power += red_count_total * blue_count_total * green_count_total

    print(cube_power)


if __name__ == "__main__":
    main()
