import matplotlib.pyplot as plt
import numpy as np

rows, cols = 5, 5

x = np.arange(cols)
y = np.arange(rows)
X, Y = np.meshgrid(x, y)

x = X.flatten()
y = Y.flatten()
fig, ax = plt.subplots(figsize=(6, 6))

ax.scatter(x, y, s=300, color='gold', marker='*', edgecolor='black')

ax.set_xlim(-1, cols)
ax.set_ylim(-1, rows)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()