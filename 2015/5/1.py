if __name__ == "__main__":

    file_input = "input.txt"

    nice_string = 0

    with open(file_input, "r") as f:
        for line in f.readlines():
            testing_string = line.rstrip("\n")

            count_vowel = 0
            vowel_nice = False
            not_forbidden_string = True
            double_string = False
            previous = None

            for letter in testing_string:
                if letter in ("a", "e", "i", "o", "u"):
                    count_vowel += 1

                if previous:
                    if letter == previous:
                        double_string = True

                    if f"{previous}{letter}" in ("ab", "cd", "pq", "xy"):
                        not_forbidden_string = False

                previous = letter

            if count_vowel >= 3:
                vowel_nice = True

            if vowel_nice and not_forbidden_string and double_string:
                nice_string += 1

    print(nice_string)
