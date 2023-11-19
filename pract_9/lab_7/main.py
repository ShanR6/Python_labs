import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris = np.genfromtxt(url, delimiter=",", dtype="object")

species_column = iris[:, 4]
unique_values, counts = np.unique(species_column, return_counts=True)

for value, count in zip(unique_values, counts):
    print(f"Уникальное значение: {value.decode()}, количество повторений: {count}")
