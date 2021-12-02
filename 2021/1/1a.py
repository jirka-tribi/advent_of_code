if __name__ == "__main__":

    file_input = "input.txt"

    previous = None
    counter = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            new = int(line.rstrip("\n"))

            if previous:
                if new > previous:
                    counter += 1

            previous = new

    print(counter)
