import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5
plt.fill_between(x, y1, color='skyblue', alpha=0.4)
plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='orange')
plt.title('Filled Area Plot')
plt.show()