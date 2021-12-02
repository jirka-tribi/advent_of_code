if __name__ == "__main__":

    file_input = "input.txt"

    floor = 0

    with open(file_input, "r") as f:
        input_str = f.read()

    for item in input_str:
        if item == "(":
            floor += 1
        elif item == ")":
            floor -= 1

    print(floor)
