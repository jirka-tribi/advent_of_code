if __name__ == "__main__":

    file_input = "input.txt"

    total_char = 0
    total_memory = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            line_strip = line.strip("\n")
            line_count = len(line_strip)

            decrease_count = 2

            previous = None

            for letter in line_strip:
                if previous:
                    if f"{previous}{letter}" == "\\x":
                        decrease_count += 3
                    elif previous == "\\" and letter == "\\":
                        letter = "a"
                        decrease_count += 1
                    elif previous == "\\":
                        decrease_count += 1

                previous = letter

            total_char += line_count
            total_memory += line_count - decrease_count

    print(total_char)
    print(total_memory)
    print(total_char - total_memory)
