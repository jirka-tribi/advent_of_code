if __name__ == "__main__":

    file_input = "input.txt"

    commands = []
    wires = {}

    # Store all command into list of dict
    with open(file_input, "r") as f:
        for line in f.readlines():
            command, wire = line.rstrip("\n").split(" -> ")
            commands.append({"command": command, "wire": wire, "executed": False})

    # Set all wires if possible
    for item in commands:
        try:
            signal = int(item["command"])
        except ValueError:
            pass
        else:
            wires[item["wire"]] = signal
            item["executed"] = True

    # Execute all commands if possible
    while True:
        all_executed = True

        for item in commands:
            parsed_command = item["command"].split(" ")

            if item["executed"]:
                continue
            else:
                all_executed = False

            if len(parsed_command) == 1:
                wire = parsed_command[0]
                if wire in wires:
                    wires[item["wire"]] = wires[wire] & 0xFFFF
                    item["executed"] = True
                continue

            # NOT command
            if len(parsed_command) == 2:
                wire = parsed_command[1]
                if wire in wires:
                    wires[item["wire"]] = ~wires[wire] & 0xFFFF
                    item["executed"] = True
                continue

            in_1, command, in_2 = parsed_command
            try:
                in_1 = int(in_1)
            except ValueError:
                if in_1 not in wires:
                    continue
                in_1 = wires[in_1]

            try:
                in_2 = int(in_2)
            except ValueError:
                if in_2 not in wires:
                    continue
                in_2 = wires[in_2]

            if command == "AND":
                output = in_1 & in_2
                wires[item["wire"]] = output & 0xFFFF
            elif command == "OR":
                output = in_1 | in_2
                wires[item["wire"]] = output & 0xFFFF
            elif command == "LSHIFT":
                output = in_1 << in_2
                wires[item["wire"]] = output & 0xFFFF
            elif command == "RSHIFT":
                output = in_1 >> in_2
                wires[item["wire"]] = output & 0xFFFF
            else:
                raise RuntimeError("Unknown command")

            item["executed"] = True

        if all_executed:
            break

    print(wires["a"])
