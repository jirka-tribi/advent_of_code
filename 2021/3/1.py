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

    gamma_bin_str = ""
    epsilon_bin_str = ""
    for i in range(0, 12):
        zero_count = 0
        one_count = 0
        for item in binary_list:
            if item[i] == 0:
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            gamma_bin_str += "0"
            epsilon_bin_str += "1"
        else:
            gamma_bin_str += "1"
            epsilon_bin_str += "0"

    gamma_dec = int(gamma_bin_str, 2)
    epsilon_bin_str = int(epsilon_bin_str, 2)
    print(gamma_dec)
    print(epsilon_bin_str)
    print(gamma_dec * epsilon_bin_str)
