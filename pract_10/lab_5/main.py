import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z1 = X ** 2 + Y ** 2
Z2 = np.log(Z1)

fig = plt.figure(figsize=(10, 5))

ax1 = fig.add_subplot(121, projection="3d")
ax1.plot_surface(X, Y, Z1, cmap="viridis")
ax1.set_title("MSE")
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_zlabel("Z")

ax2 = fig.add_subplot(122, projection="3d")
ax2.plot_surface(X, Y, Z2, cmap="viridis")
ax2.set_title("MSE with log(Z)")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("log(Z)")

plt.show()
