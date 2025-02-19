import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3
plt.contourf(X, Y, Z, levels=[-1000, 0], colors='red')
plt.contour(X, Y, Z, levels=[0], colors='red', linewidths=1.5)
plt.show()
