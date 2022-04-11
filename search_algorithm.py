import json


def read_data(file_name, key):
    all_keys = ["unordered_numbers", "ordered_numbers", "dna_sequence"]
    if key in all_keys:
        with open(file_name) as data_file:
            data = json.load(data_file)
        sequential_data = data[key]
    else:
        return None
    return sequential_data


def main():
    file_name = "sequential.json"
    key = "unordered_numbers"
    sequential_data = read_data(file_name, key)
    print(sequential_data)


if __name__ == '__main__':
    main()
