if __name__ == "__main__":

    testing_str = "1113222113"

    # Part 1 - repeated = 40
    # Part 2 - repeated = 50

    repeated = 50

    for i in range(0, repeated):
        testing_str = f"A{testing_str}Z"
        previous = None
        counter = 0
        result = ""

        for item in testing_str:
            if item == "A":
                previous = item
                continue

            if item == previous:
                counter += 1
            else:
                if previous != "A":
                    result += f"{counter}{previous}"
                counter = 1

            previous = item

        testing_str = result

    print(len(result))
