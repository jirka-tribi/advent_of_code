from typing import List

FORBIDDEN = [105, 108, 111]


def abc_to_int(abc_str) -> List[int]:
    result_list = []

    for letter in abc_str:
        result_list.append(ord(letter))

    return result_list


def abc_to_str(abc_int: List[int]) -> str:
    result = ""
    for number in abc_int:
        result += chr(number)

    return result


def increase_int(abc_int: List[int]) -> List[int]:
    abc_int_rev = abc_int
    abc_int_rev.reverse()

    complete = False
    abc_int_new = []
    for number in abc_int_rev:
        if complete:
            abc_int_new.append(number)
            continue

        if number < 122:
            abc_int_new.append(number + 1)
            complete = True
            continue

        if number == 122:
            abc_int_new.append(97)

    abc_int_new.reverse()

    return abc_int_new


def is_validated(abc_int: List[int]) -> bool:
    validated_inc = False
    validate_double = False
    forbidden_double = 0

    for number in abc_int:
        if number in FORBIDDEN:
            return False

    first = abc_int[0]
    second = abc_int[1]
    counter = 0
    for i in range(2, len(abc_int)):
        third = abc_int[i]

        if first == second and first != forbidden_double:
            counter += 1
            forbidden_double = first
        if i == len(abc_int) - 1:
            if second == third and second != forbidden_double:
                counter += 1
                forbidden_double = third

        if first + 2 == second + 1 == third:
            validated_inc = True

        first = second
        second = third

    if counter >= 2:
        validate_double = True

    return validated_inc and validate_double


if __name__ == "__main__":

    # Part 1 password = hepxcrrq
    # Part 2 password = hepxxyzz

    password = "hepxxyzz"
    pass_list_int = abc_to_int(password)

    while True:
        testing_int_list = increase_int(pass_list_int)
        if is_validated(testing_int_list):
            break

        pass_list_int = testing_int_list

    print(abc_to_str(testing_int_list))
