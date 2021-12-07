def compute_rating(input_list, oxygen: bool):
    input_list_temp = input_list

    for i in range(0, 12):
        if len(input_list_temp) == 1:
            break

        zero_count = 0
        one_count = 0

        zero_list = []
        one_list = []

        for item in input_list_temp:
            if item[i] == 0:
                zero_count += 1
                zero_list.append(item)
            else:
                one_count += 1
                one_list.append(item)

        if oxygen:
            if one_count >= zero_count:
                input_list_temp = one_list
            else:
                input_list_temp = zero_list
        else:
            if zero_count <= one_count:
                input_list_temp = zero_list
            else:
                input_list_temp = one_list

    rating_bin_str = ""
    for number in input_list_temp[0]:
        rating_bin_str += str(number)

    return int(rating_bin_str, 2)


if __name__ == "__main__":

    file_input = "input.txt"

    binary_list = []

    with open(file_input, "r") as f:
        for line in f.readlines():
            line_strip = line.strip("\n")

            input_list = []

            for number in line_strip:
                input_list.append(int(number))

            binary_list.append(input_list)

    binary_list_oxygen = binary_list
    binary_list_co = binary_list

    oxygen_rating = compute_rating(binary_list_oxygen, True)
    co_rating = compute_rating(binary_list_co, False)

    print(oxygen_rating)
    print(co_rating)

    print(oxygen_rating * co_rating)
