from c import get_lowest_location, parse_input


def main():
    seeds_ranges, process_maps = parse_input()

    seeds = set()

    i = 0
    for _ in range(int(len(seeds_ranges) / 2)):
        for j in range(seeds_ranges[i + 1]):
            seeds.add(seeds_ranges[i] + j)

        i += 2

    print(seeds)

    min_location = get_lowest_location(seeds, process_maps)

    print(min_location)


if __name__ == "__main__":
    main()
