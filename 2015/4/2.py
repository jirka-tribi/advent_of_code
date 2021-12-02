import hashlib

if __name__ == "__main__":

    file_input = "input.txt"

    with open(file_input, "r") as f:
        input_str = f.read()

    counter = 0
    while True:
        string_to_count = f"{input_str}{counter}"
        md5_checksum = hashlib.md5(string_to_count.encode())

        if md5_checksum.hexdigest().startswith("000000"):
            print(counter)
            break

        counter += 1
