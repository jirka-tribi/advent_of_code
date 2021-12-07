import json

NUMBERS_COUNT = 0


def parse_object_recursively(input_object):
    global NUMBERS_COUNT
    if isinstance(input_object, str):
        pass
    elif isinstance(input_object, int):
        NUMBERS_COUNT += input_object
    elif isinstance(input_object, dict):
        for item in input_object.values():
            parse_object_recursively(item)
    elif isinstance(input_object, list):
        for item in input_object:
            parse_object_recursively(item)


if __name__ == "__main__":

    file_input = "input.json"

    with open(file_input, "r") as f:
        input_data = f.read()

    input_json = json.loads(input_data)

    parse_object_recursively(input_json)

    print(NUMBERS_COUNT)
