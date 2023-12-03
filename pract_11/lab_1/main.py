import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

t = np.linspace(0, 1, 1000)
x = square(2 * np.pi * 10 * t)

plt.plot(t, x)
plt.xlabel("Время")
plt.ylabel("Амплитуда")
plt.title("Прямоугольный сигнал")
plt.show()
