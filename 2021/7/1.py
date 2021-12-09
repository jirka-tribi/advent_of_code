from typing import List


def parse_input(file_name: str) -> List[int]:
    with open(file_name, "r") as f:
        striped_line = f.read().strip("\n").split(",")

    crabs = [int(item) for item in striped_line]

    return crabs


def main():
    file_name = "test_input.txt"

    crabs = parse_input(file_name)
    fuels = []

    for start_crab in range(max(crabs)):
        fuel_crab = 0
        for j in range(len(crabs)):
            fuel_crab += abs(crabs[j] - start_crab)

        fuels.append(fuel_crab)

    print(fuels)


if __name__ == "__main__":
    main()
