import re

INPUT_FILE_NAME = "input.txt"

RED_TOTAL = 12
BLUE_TOTAL = 14
GREEN_TOTAL = 13


def parse_input() -> tuple[int, str]:
    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.readlines():
            find_line = re.search(r"Game (\d*): (.*)", line)
            game_id = find_line.group(1)
            game_sets = find_line.group(2)

            yield int(game_id), game_sets


def find_color_in_game_set(color: str, game_set: str) -> int:
    find_color = re.search(r"(\d*) %s" % color, game_set)

    return int(find_color.group(1)) if find_color else 0


def main():
    game_ids_count = 0

    for game_id, game_sets in parse_input():
        useless_game = False

        for game_set in game_sets.split(";"):
            red_count = find_color_in_game_set("red", game_set)
            blue_count = find_color_in_game_set("blue", game_set)
            green_count = find_color_in_game_set("green", game_set)

            if red_count > RED_TOTAL or blue_count > BLUE_TOTAL or green_count > GREEN_TOTAL:
                useless_game = True
                break

        if not useless_game:
            game_ids_count += game_id

    print(game_ids_count)


if __name__ == "__main__":
    main()
