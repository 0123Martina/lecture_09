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


def linear_search(searched_sequence, number):
    positions = []
    index = 0
    count = 0
    for element in searched_sequence:
        if element == number:
            positions.append(index)
            count = count + 1
        index = index + 1
    slovník = {"positions": positions, "count": count}
    return slovník

def main():
    file_name = "sequential.json"
    key = "unordered_numbers"
    searched_number = 5
    sequential_data = read_data(file_name, key)
    slovník = linear_search(sequential_data, searched_number)
    print(sequential_data)
    print(slovník)


if __name__ == '__main__':
    main()
