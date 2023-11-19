import numpy as np


def run_length_encoding(x):
    i = np.where(x[:-1] != x[1:])[0] + 1
    counts = np.diff(np.r_[0, i, x.size])
    numbers = x[np.r_[0, i]]
    return numbers, counts


x = np.array([2, 2, 2, 3, 3, 3, 5])
numbers, counts = run_length_encoding(x)

print("Числа:", numbers)
print("Количество повторений:", counts)
