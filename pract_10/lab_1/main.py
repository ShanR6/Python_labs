import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre

x = np.linspace(-1, 1, 100)

plt.figure()
plt.title("Полиномы Лежандра")

for n in range(1, 8):
    y = eval_legendre(n, x)
    plt.plot(x, y, label=f"n = {n}")

plt.legend(loc="upper right")
plt.show()
