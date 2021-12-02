if __name__ == "__main__":

    file_input = "input.txt"

    horizontal = 0
    aim = 0
    depth = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            command, count = line.rstrip("\n").split(" ")
            count = int(count)

            if command == "forward":
                horizontal += count
                if aim != 0:
                    depth += count * aim
            elif command == "down":
                aim += count
            elif command == "up":
                aim -= count

    print(horizontal)
    print(depth)

    print(horizontal * depth)
