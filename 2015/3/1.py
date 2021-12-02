if __name__ == "__main__":

    file_input = "input.txt"

    x = 0
    y = 0
    locations = set()

    with open(file_input, "r") as f:
        input_str = f.read()

    for item in input_str:
        if item == ">":
            x += 1
        elif item == "<":
            x -= 1
        elif item == "^":
            y += 1
        elif item == "v":
            y -= 1

        locations.add(f"{x}x{y}")

    print(len(locations))
