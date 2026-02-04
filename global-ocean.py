import numpy as np
import matplotlib.pyplot as plt

x,y = np.meshgrid(np.linspace(-180,180,30), np.linspace(-90,90,15))
u = np.cos(np.radians(y))
v = np.sin(np.radians(x))

plt.quiver(x, y, u, v, color='teal')
plt.title('Global Ocean Currents Visualization', fontsize=16, fontweight='bold')
plt.show()
