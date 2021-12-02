from compute import compute_wires

if __name__ == "__main__":

    file_input = "input_2.txt"

    commands_list = []

    # Store all command into list of dict
    with open(file_input, "r") as f:
        for line in f.readlines():
            command_str, wire_str = line.rstrip("\n").split(" -> ")
            commands_list.append({"command": command_str, "wire": wire_str, "executed": False})

    wires = compute_wires(commands_list)

    print(wires["a"])
