import re

INPUT_FILE_NAME = "input.txt"

CARD_INSTANCES = {}


def parse_input() -> list[tuple[int, list[str], list[str]]]:
    with open(INPUT_FILE_NAME, "r") as f:
        game_list = []
        for line in f.readlines():
            find_line = re.search(r"Card\s*(\d*): (.*)", line)

            game_id = int(find_line.group(1))
            CARD_INSTANCES[game_id] = 1
            winning_numbers, all_numbers = find_line.group(2).split("|")

            game_list.append(
                (
                    game_id,
                    [item for item in winning_numbers.strip().split(" ") if item],
                    [item for item in all_numbers.strip().split(" ") if item],
                )
            )

    return game_list


def main():
    for game_id, winning_numbers, all_numbers in parse_input():
        matches = 0

        for number in winning_numbers:
            if number in all_numbers:
                matches += 1

        number_of_cards = CARD_INSTANCES[game_id]
        for i in range(matches):
            CARD_INSTANCES[game_id + i + 1] += number_of_cards

    card_count = 0
    for item in CARD_INSTANCES.values():
        card_count += item

    print(card_count)


if __name__ == "__main__":
    main()
