from typing import List, Dict, Union


def compute_wires(commands: List[Dict[str, Union[str, bool]]]) -> Dict[str, int]:
    # Set all wires if possible
    wires_dict = {}

    for item in commands:
        try:
            signal = int(item["command"])
        except ValueError:
            pass
        else:
            wires_dict[item["wire"]] = signal
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
                if wire in wires_dict:
                    wires_dict[item["wire"]] = wires_dict[wire] & 0xFFFF
                    item["executed"] = True
                continue

            # NOT command
            if len(parsed_command) == 2:
                wire = parsed_command[1]
                if wire in wires_dict:
                    wires_dict[item["wire"]] = ~wires_dict[wire] & 0xFFFF
                    item["executed"] = True
                continue

            in_1, command, in_2 = parsed_command
            try:
                in_1 = int(in_1)
            except ValueError:
                if in_1 not in wires_dict:
                    continue
                in_1 = wires_dict[in_1]

            try:
                in_2 = int(in_2)
            except ValueError:
                if in_2 not in wires_dict:
                    continue
                in_2 = wires_dict[in_2]

            if command == "AND":
                output = in_1 & in_2
                wires_dict[item["wire"]] = output & 0xFFFF
            elif command == "OR":
                output = in_1 | in_2
                wires_dict[item["wire"]] = output & 0xFFFF
            elif command == "LSHIFT":
                output = in_1 << in_2
                wires_dict[item["wire"]] = output & 0xFFFF
            elif command == "RSHIFT":
                output = in_1 >> in_2
                wires_dict[item["wire"]] = output & 0xFFFF
            else:
                raise RuntimeError("Unknown command")

            item["executed"] = True

        if all_executed:
            break

    return wires_dict
