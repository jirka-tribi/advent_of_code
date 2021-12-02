if __name__ == "__main__":

    file_input = "input.txt"

    floor = 0
    counter = 0

    with open(file_input, "r") as f:
        input_str = f.read()

    for item in input_str:
        counter += 1

        if item == "(":
            floor += 1
        elif item == ")":
            floor -= 1

        if floor == -1:
            break

    print(counter)
