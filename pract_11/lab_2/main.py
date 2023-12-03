import numpy as np
import matplotlib.pyplot as plt

av_val = 0
stand = 1
size = 1000
data = np.random.normal(av_val, stand, size)

plt.hist(data, bins=30, density=True)
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.title("Нормальное распределение(гистограмма)")
plt.show()
