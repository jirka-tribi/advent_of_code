import copy
from typing import List, Dict, Tuple
from collections import OrderedDict

BINGO_TYPING = List[Dict[int, bool]]
BINGOS_TYPING = List[BINGO_TYPING]


def parse_bingos(
    input_not_sorted: List[str],
) -> Tuple[List[int], BINGOS_TYPING]:
    bingos = []
    numbers_list = []

    bingo_array = []
    for i in range(0, len(input_not_sorted)):
        if i == 0:
            numbers_list = [int(item) for item in input_not_sorted[i].split(",")]
            continue

        temp_dict = OrderedDict()
        for item in input_not_sorted[i].split(" "):
            strip_item = item.strip(" ")
            if strip_item != "":
                temp_dict[int(strip_item)] = False

        bingo_array.append(temp_dict)

        if (i % 5) == 0:
            bingos.append(bingo_array)
            bingo_array = []

    return numbers_list, bingos


def check_bingos(number: int, bingos: BINGOS_TYPING) -> BINGOS_TYPING:
    for bingo in bingos:
        for item in bingo:
            for k in item.keys():
                if k == number:
                    item[number] = True

    return bingos


def remove_winers(bingos: BINGOS_TYPING) -> BINGOS_TYPING:
    # Check all rows if there is all True
    winner = True

    temp_bingos = copy.deepcopy(bingos)

    for bingo in bingos:
        for item in bingo:
            for v in item.values():
                if not v:
                    winner = False
                    break

            if winner:
                try:
                    temp_bingos.remove(bingo)
                except ValueError:
                    pass
            else:
                winner = True

        # Check all columns if there is all True
        for i in range(0, 5):
            for item in bingo:
                temp_list = list(item.values())
                if not temp_list[i]:
                    winner = False
                    break

            if winner:
                try:
                    temp_bingos.remove(bingo)
                except ValueError:
                    pass
            else:
                winner = True

    return temp_bingos


def is_winner(bingo: BINGO_TYPING) -> bool:
    # Check all rows if there is all True
    winner = True

    for item in bingo:
        for v in item.values():
            if not v:
                winner = False
                break

        if winner:
            return True
        else:
            winner = True

    # Check all columns if there is all True
    for i in range(0, 5):
        for item in bingo:
            temp_list = list(item.values())
            if not temp_list[i]:
                winner = False
                break

        if winner:
            return True
        else:
            winner = True

    return False


def count_unchecked(bingo: BINGO_TYPING) -> int:
    count = 0
    for item in bingo:
        for k, v in item.items():
            if not v:
                count += k

    return count


def main():
    file_input = "input.txt"
    input_not_sorted = []

    with open(file_input, "r") as f:
        for line in f.readlines():
            if line == "\n":
                continue

            line_strip = line.strip("\n")
            input_not_sorted.append(line_strip)

    numbers_list, bingos = parse_bingos(input_not_sorted)

    new_bingos = copy.deepcopy(bingos)
    for number in numbers_list:
        new_bingos = check_bingos(number, new_bingos)
        if len(new_bingos) == 1:
            winner = is_winner(new_bingos[0])
            if winner:
                print(number)
                count = count_unchecked(new_bingos[0])
                for item in new_bingos[0]:
                    print(item)
                print(count)
                print(number * count)
                break
        else:
            new_bingos = remove_winers(new_bingos)


if __name__ == "__main__":
    main()
