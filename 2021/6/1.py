from typing import List


def parse_input(file_name: str) -> List[int]:
    with open(file_name, "r") as f:
        striped_line = f.read().strip("\n").split(",")

    lantern_fishes = [int(item) for item in striped_line]

    return lantern_fishes


def main():
    file_name = "input.txt"
    max_days = 200
    lantern_fishes = parse_input(file_name)

    print("Initial state: " + ",".join(map(str, lantern_fishes)))

    i = 0
    devaty_den_new = len(lantern_fishes)
    for i in range(1, max_days + 1):
        append_counter = 0
        for j in range(0, len(lantern_fishes)):
            fish = lantern_fishes[j]
            if fish == 0:
                append_counter += 1
                lantern_fishes[j] = 6
            else:
                lantern_fishes[j] = fish - 1

        for k in range(0, append_counter):
            lantern_fishes.append(8)

        if (i % 9) == 0:
            devaty_den_old = devaty_den_new
            devaty_den_new = len(lantern_fishes)

            print(f"After {i} day: {devaty_den_new - devaty_den_old}")


if __name__ == "__main__":
    main()
