import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

edge = 1
ax.set_xlim([-edge, edge])
ax.set_ylim([-edge, edge])

lisazhu, = plt.plot([], [])

ratio = np.linspace(0, 1, 100)


def animate(frame):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = edge * np.sin(t)
    y = edge * np.sin(ratio[frame] * t)
    lisazhu.set_data(x, y)
    return lisazhu,


animation = FuncAnimation(fig, animate, frames=100, interval=30)

plt.show()
