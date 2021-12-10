from typing import List


def parse_input(file_name: str) -> List[int]:
    with open(file_name, "r") as f:
        striped_line = f.read().strip("\n").split(",")

    lantern_fishes = [int(item) for item in striped_line]

    return lantern_fishes


def main():
    file_name = "input.txt"
    max_days = 256
    lantern_fishes = parse_input(file_name)

    days = [0] * 9

    for fish in lantern_fishes:
        days[fish] += 1

    for _ in range(0, max_days):
        new_fishes = days[0]

        days[0] = days[1]
        days[1] = days[2]
        days[2] = days[3]
        days[3] = days[4]
        days[4] = days[5]
        days[5] = days[6]
        days[6] = days[7] + new_fishes

        days[7] = days[8]
        days[8] = new_fishes

    print(sum(days))


if __name__ == "__main__":
    main()
