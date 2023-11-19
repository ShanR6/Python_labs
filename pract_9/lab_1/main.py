import numpy as np

file_path = "text.txt"

matrix = np.loadtxt(file_path, delimiter=",")

print("Матрица:\n", matrix)

sum_elements = np.sum(matrix)

max_element = np.max(matrix)

min_element = np.min(matrix)

print("Сумма всех элементов:", sum_elements)
print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)
