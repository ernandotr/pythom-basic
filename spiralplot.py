import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 4 * np.pi, 100)
r = theta**1.5

plt.polar(theta, r, color='purple', linewidth=2)
plt.title("Spiral Plot", va='bottom')
plt.show()