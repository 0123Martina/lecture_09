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


def pattern_search(sequence, template):
    nalezene_pozice = set()
    zacatek = 0
    index = len(template)
    while index < len(sequence):
        if template == sequence[zacatek:index]:
            nalezene_pozice.add(zacatek)
        zacatek = zacatek + 1
        index = index + 1
    return nalezene_pozice



def main():
    file_name = "sequential.json"
    key = "dna_sequence"
    searched_number = 5
    template = "TGAC"
    sequential_data = read_data(file_name, key)
    # slovník = linear_search(sequential_data, searched_number)
    nalezene_pozice_zacatku_vzoru = pattern_search(sequential_data, template)
    print(nalezene_pozice_zacatku_vzoru)


if __name__ == '__main__':
    main()
