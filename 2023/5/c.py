INPUT_FILE_NAME = "test_input.txt"


def parse_input() -> tuple[list[int], dict[str, list[dict[str, int]]]]:
    process_maps = {}
    process_type = None

    with open(INPUT_FILE_NAME, "r") as f:
        for line in f.read().split("\n"):
            if not line:
                continue

            if "seeds:" in line:
                seeds = [int(item) for item in line.removeprefix("seeds: ").split(" ")]
            elif "map" in line:
                process_type = line
                process_maps[process_type] = []
            else:
                range_dict = {}
                ranges = line.split(" ")

                range_dict["source"] = int(ranges[1])
                range_dict["source_to_target"] = int(ranges[0])
                range_dict["range"] = int(ranges[2])

                process_maps[process_type].append(range_dict)

    return seeds, process_maps


def get_lowest_location(seeds: list[int] | set[int], process_maps: dict[str, list[dict, str, int]]) -> int:
    print(process_maps)
    locations = []
    for seed in seeds:
        previous_location = seed

        for process in process_maps.values():
            for one_range in process:
                source = one_range["source"]
                source_to_target = one_range["source_to_target"]
                range_ = one_range["range"]
                if source <= previous_location <= source + range_:
                    previous_location = previous_location + (source_to_target - source)
                    break

        locations.append(previous_location)

    print(locations)

    return min(locations)
