if __name__ == "__main__":

    file_input = "input.txt"

    previous = None
    counter = 0

    input_list = []
    checksums = []

    with open(file_input, "r") as f:
        for line in f.readlines():
            input_list.append(int(line.rstrip("\n")))

    for index in range(0, len(input_list) - 2):
        checksums.append(input_list[index] + input_list[index + 1] + input_list[index + 2])

    for item in checksums:
        if previous:
            if item > previous:
                counter += 1

        previous = item

    print(counter)
