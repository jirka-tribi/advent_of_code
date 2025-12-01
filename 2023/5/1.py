from c import get_lowest_location, parse_input


def main():
    seeds, process_maps = parse_input()

    min_location = get_lowest_location(seeds, process_maps)

    print(min_location)


if __name__ == "__main__":
    main()
