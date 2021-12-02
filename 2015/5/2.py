if __name__ == "__main__":

    file_input = "input.txt"

    nice_string = 0
    count_bad = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            testing_string = line.rstrip("\n")

            first = None
            second = None
            third = None

            count_double = 0
            pair_string = False
            repeating = False

            pair_list = []

            for letter in testing_string:
                first = second
                second = third
                third = letter

                if second:
                    pair_list.append(f"{second}{third}")

                if first:
                    if first == third:
                        repeating = True

            pair_set = set(pair_list)

            if len(pair_set) != len(pair_list):
                pair_string = True

            if pair_string and repeating:
                nice_string += 1

                previous = None
                for pair in pair_list:
                    if previous:
                        if previous == pair:
                            count_bad += 1

                    previous = pair

    print(nice_string)
    print(count_bad)
    print(nice_string - count_bad)
