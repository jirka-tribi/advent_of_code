if __name__ == "__main__":

    file_input = "input.txt"

    floor = 0
    squares = 0
    ribbon = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            size_list = [int(item) for item in line.rstrip("\n").split("x")]
            size_list.sort()

            ribbon += 2 * size_list[0] + 2 * size_list[1]
            ribbon += size_list[0] * size_list[1] * size_list[2]

    print(ribbon)
