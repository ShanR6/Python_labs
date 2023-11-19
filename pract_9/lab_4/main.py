import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_index = np.where(x == 0)[0]
if zero_index[-1] == x.size - 1:
    zero_index = zero_index[:-1]

num_index = zero_index + 1

max_value = np.max(x[num_index])

print("Максимальный элемент перед нулевым элементом:", max_value)
