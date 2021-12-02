if __name__ == "__main__":

    file_input = "input.txt"

    floor = 0
    squares = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            size_list = [int(item) for item in line.rstrip("\n").split("x")]
            length, width, height = size_list

            sides = [length * width, width * height, height * length]

            for side in sides:
                squares += 2 * side

            squares += min(sides)

    print(squares)
