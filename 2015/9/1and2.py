import itertools

if __name__ == "__main__":

    file_input = "input.txt"

    cities_dest_dict = {}
    cities_dest_dict_complete = {}
    cities_set = set()
    dest_list = []

    with open(file_input, "r") as f:
        for line in f.readlines():
            cities, dest = line.strip("\n").split(" = ")
            cities_dest_dict[cities] = dest

    for k, v in cities_dest_dict.items():
        city_1, city_2 = k.split(" to ")
        cities_set.add(city_1)
        cities_set.add(city_2)

        cities_dest_dict_complete[f"{city_1}{city_2}"] = v
        cities_dest_dict_complete[f"{city_2}{city_1}"] = v

    perms = itertools.permutations(cities_set)

    for perm in perms:
        dest = 0
        for i in range(0, len(cities_set) - 1):
            cities_1_2 = f"{perm[i]}{perm[i + 1]}"
            if cities_1_2 in cities_dest_dict_complete:
                dest += int(cities_dest_dict_complete[cities_1_2])
            else:
                break
        dest_list.append(dest)

    print(len(dest_list))
    # Part 1 - shortest way
    print(min(dest_list))

    # Part 2 - longest way
    print(max(dest_list))
