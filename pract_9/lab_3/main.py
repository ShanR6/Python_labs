import numpy as np

arr = np.random.randn(10, 4)

min_value = np.min(arr)

max_value = np.max(arr)

mean_value = np.mean(arr)

std_value = np.std(arr)

save_arr = arr[:5, :]

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_value)
print("Первые 5 строк:\n", save_arr)
