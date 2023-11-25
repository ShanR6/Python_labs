import numpy as np
import matplotlib.pyplot as plt

frequency = [(3, 2), (3, 4), (5, 4), (5, 6)]

t = np.linspace(0, 2 * np.pi, 1000)
print(t)

plt.figure()
plt.suptitle('Фигуры Лисажу с разными соотношениями частот')

for i, (f1, f2) in enumerate(frequency):
    x = np.sin(f1 * t)
    y = np.sin(f2 * t)
    plt.subplot(2, 2, i + 1)
    plt.plot(x, y)
    plt.title(f'Соотношение частот: {f1}:{f2}')

plt.tight_layout()
plt.show()
