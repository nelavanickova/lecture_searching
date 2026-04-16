import json
import os
import time
import matplotlib.pyplot as plt
from random import choices
from generators import unordered_sequence
from generators import  ordered_sequence
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

def binary_search(sekvence, cislo):
    leva = 0
    prava = len(sekvence) - 1
    pozice = []
    while leva <= prava:
        stred = (leva + prava) // 2
        if sekvence[stred] == cislo:
            return stred
        elif sekvence[stred] > cislo:
            prava = stred -1
        else:
            leva = stred + 1
    return None



def main():
    nacteni = (read_data("sequential.json", "unordered_numbers"))
    nacteno_serazeno =(read_data("sequential.json", "ordered_numbers"))
    linearni = (linear_search( nacteni, 0))
    binarni = binary_search(nacteno_serazeno, -3)

    # print(nacteni)
    # print(linearni)
    # print(binarni)
    seq_casy = [100, 500, 1000, 5000, 10000]
    linearni_seq = []
    # linearni
    for i in seq_casy:
        seq = unordered_sequence(i)
        start = time.perf_counter()
        linear_search(seq, 0)
        end = time.perf_counter()
        duration_lin = end - start
        linearni_seq.append(duration_lin)
    print(f"Měření linearni trvalo {linearni_seq} s")
    plt.plot(seq_casy, linearni_seq)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření linerarni")
    plt.show()

    # print(seq_500)
    # seq_500 = unordered_sequence(500)
    # start = time.perf_counter()
    # linear_search(seq_500, 0)
    # end = time.perf_counter()
    # duration_lin = end - start
    # print(f"Měření linearni trvalo {duration_lin:.8f} s")

    # binarni
    binar_seq = []
    for i in seq_casy:
        seq = ordered_sequence(i)
        start = time.perf_counter()
        binary_search(seq, 0)
        end = time.perf_counter()
        duration_bin = end - start
        binar_seq.append(duration_bin)


    print(f"Měření linearni trvalo {binar_seq} s")
    plt.plot(seq_casy, binar_seq)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Ukázkový graf měření binarni")
    plt.show()

    # serazeno_seq_500 = ordered_sequence(500)
    # start = time.perf_counter()
    # binary_search(serazeno_seq_500, 0)
    # end = time.perf_counter()
    # duration_bin = end - start
    # print(f"Měření binarni trvalo {duration_bin:.8f} s")


if __name__ == '__main__':
    main()