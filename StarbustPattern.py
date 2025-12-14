import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
t = np.linspace(0, 2 * np.pi, 1500)
x = np.cos(t) * (1 + 0.6 * np.cos(20 * t))
y = np.sin(t) * (1 + 0.6 * np.cos(20 * t))
plt.scatter(x, y, c=t, cmap='spring', s=2)
plt.axis('equal')
plt.show()