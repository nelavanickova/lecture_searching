import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    with open(file_name, "r") as file:
        data = json.load(file)
        s_data = data[field]
    return s_data
    file_path = os.path.join(cwd_path, file_name)
print(read_data("sequential.json", "dna_sequence"))

def main():
    pass


if __name__ == '__main__':
    main()