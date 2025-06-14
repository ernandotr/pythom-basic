import matplotlib.pyplot as plt
import numpy as np

x=np.random.rand(10000)
y=np.random.rand(10000)

plt.hexbin(x, y, gridsize=30, cmap='Oranges', edgecolor='gray')
plt.colorbar(label='Count in bin')

plt.title('Honeycomb Pattern Hexbin Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
