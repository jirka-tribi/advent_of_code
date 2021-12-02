if __name__ == "__main__":

    file_input = "input.txt"

    horizontal = 0
    depth = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            command, count = line.rstrip("\n").split(" ")

            if command == "forward":
                horizontal += int(count)
            elif command == "down":
                depth += int(count)
            elif command == "up":
                depth -= int(count)

    print(horizontal)
    print(depth)

    print(horizontal * depth)
