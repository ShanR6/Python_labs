import numpy as np


def change_line(array, a, b):
    array[[a, b]] = array[[b, a]]
    print(f"Поменяны местами строки с индексами {a} и {b}")
    return array


arr = np.arange(16).reshape(4, 4)
print(change_line(arr, 1, 3))
