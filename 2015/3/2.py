if __name__ == "__main__":

    file_input = "input.txt"

    santa_x = 0
    santa_y = 0
    robo_santa_x = 0
    robo_santa_y = 0

    locations = set()
    locations.add("0x0")

    with open(file_input, "r") as f:
        input_str = f.read()

    counter = 0

    for item in input_str:
        counter += 1

        # Odd index - move for santa
        if not (counter % 2) == 0:
            if item == ">":
                santa_x += 1
            elif item == "<":
                santa_x -= 1
            elif item == "^":
                santa_y += 1
            elif item == "v":
                santa_y -= 1

            locations.add(f"{santa_x}x{santa_y}")
        else:
            if item == ">":
                robo_santa_x += 1
            elif item == "<":
                robo_santa_x -= 1
            elif item == "^":
                robo_santa_y += 1
            elif item == "v":
                robo_santa_y -= 1

            locations.add(f"{robo_santa_x}x{robo_santa_y}")

    print(locations)
    print(len(locations))
