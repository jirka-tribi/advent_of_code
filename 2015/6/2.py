if __name__ == "__main__":

    file_input = "input.txt"

    lighters_array = []

    i = 0
    j = 0

    light_counter = 0

    # Fill all lighters as off o
    for _ in range(0, 1000):
        lighter_line = []
        for _ in range(0, 1000):
            lighter_line.append(0)
        lighters_array.append(lighter_line)

    with open(file_input, "r") as f:
        for line in f.readlines():
            input_list = line.rstrip("\n").split(" ")

            lighter = None

            if len(input_list) == 4:
                command = input_list[0]
                start_x, start_y = [int(item) for item in input_list[1].split(",")]
                end_x, end_y = [int(item) for item in input_list[3].split(",")]
            else:
                command = f"{input_list[0]} {input_list[1]}"
                start_x, start_y = [int(item) for item in input_list[2].split(",")]
                end_x, end_y = [int(item) for item in input_list[4].split(",")]

            for i in range(start_x, end_x + 1):
                for j in range(start_y, end_y + 1):
                    if command == "turn on":
                        lighters_array[i][j] += 1
                    elif command == "turn off":
                        if lighters_array[i][j] > 0:
                            lighters_array[i][j] -= 1
                    elif command == "toggle":
                        lighters_array[i][j] += 2

    for i in range(0, 1000):
        for j in range(0, 1000):
            light_counter += lighters_array[i][j]

    print(light_counter)
