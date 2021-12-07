def get_reindeer_distance(speed: int, speed_time: int, resting_time: int, total) -> int:
    distance = 0

    resting = False
    running = True

    start_running = 0
    start_resting = 0

    for _ in range(total):
        if running:
            distance += speed
            start_running += 1

        if start_running == speed_time:
            running = False
            resting = True
            start_running = 0
            continue

        if resting:
            start_resting += 1

        if start_resting == resting_time:
            resting = False
            running = True
            start_resting = 0

    return distance


if __name__ == "__main__":

    file_input = "input.txt"

    TOTAL_SECONDS = 2503
    distance_list = []

    with open(file_input, "r") as f:
        for line in f.readlines():
            _, _, _, max_speed, _, _, time_speed, _, _, _, _, _, _, resting_time, _ = line.strip(
                "\n"
            ).split(" ")
            dist = get_reindeer_distance(
                int(max_speed), int(time_speed), int(resting_time), TOTAL_SECONDS
            )
            distance_list.append(dist)

    print(max(distance_list))
