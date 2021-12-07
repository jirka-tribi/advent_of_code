import itertools


def get_happy(n_1, n_2) -> int:
    happy = 0

    happy += happiness[f"{n_1}{n_2}"]
    happy += happiness[f"{n_2}{n_1}"]

    return happy


if __name__ == "__main__":

    file_input = "input.txt"

    persons = set()
    happiness = {}
    happy_list = []
    me = "Jirka"

    with open(file_input, "r") as f:
        for line in f.readlines():
            name_1, _, command, unit, _, _, _, _, _, _, name_2 = line.strip("\n").split(" ")
            persons.add(name_1)
            unit = int(unit)
            if command == "lose":
                unit = 0 - unit

            happiness[f"{name_1}{name_2.rstrip('.')}"] = unit

    for person in persons:
        happiness[f"{me}{person}"] = 0
        happiness[f"{person}{me}"] = 0

    persons.add(me)

    perms = itertools.permutations(persons)

    for perm in perms:
        happy_count = 0

        for i in range(0, len(persons) - 1):
            if i == 0:
                happy_count += get_happy(perm[0], perm[-1])

            happy_count += get_happy(perm[i], perm[i + 1])

        happy_list.append(happy_count)

    print(max(happy_list))
