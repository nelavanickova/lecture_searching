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
        file_path = os.path.join(cwd_path, file_name)
    """
    with open(file_name, "r") as file:
        data = json.load(file)
        sequential_data = data[field]
    return sequential_data

def linear_search(sekvence, cislo):
    scitac = 0
    pozice = []
    slovnik = {}
    for index, prvek in enumerate(sekvence):
        if prvek == cislo:
            scitac += 1
            pozice.append(index+1)
            slovnik["positions"] = pozice
            slovnik["count"] = scitac
    return slovnik



def main():
    nacteni = (read_data("sequential.json", "unordered_numbers"))
    linearni =(linear_search( nacteni, -10))
    print(nacteni)
    print(linearni)

if __name__ == '__main__':
    main()