from typing import List


def parse_input(file_name: str) -> List[int]:
    with open(file_name, "r") as f:
        striped_line = f.read().strip("\n").split(",")

    crabs = [int(item) for item in striped_line]

    return crabs


def main():
    file_name = "input.txt"

    crabs = parse_input(file_name)
    fuels = []

    for start_crab in range(0, max(crabs)):
        fuel_crab = 0
        for j in range(len(crabs)):
            numbers = abs(crabs[j] - start_crab)

            for number in range(1, numbers + 1):
                fuel_crab += number

        fuels.append(fuel_crab)

    print(min(fuels))


if __name__ == "__main__":
    main()
