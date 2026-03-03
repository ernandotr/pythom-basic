import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2*np.pi, 400)
a,b = 1, 0.6
x = a * np.cos(t)
y = b * np.sin(t)
plt.plot(x, y)
plt.scatter([0], [0], color='yellow', label='Sun')
plt.title('Planetary Orbit Simulator')
plt.axis('equal')
plt.show()