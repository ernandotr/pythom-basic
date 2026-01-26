import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

now = dt.datetime.now()
h, m, s = now.hour % 12, now.minute, now.second
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, polar=True)
ax.barh(3, 2 * np.pi * h / 12, color='purple')
ax.barh(2, 2 * np.pi * m / 60, color='orange')
ax.barh(1, 2 * np.pi * s / 60, color='cyan')
ax.set_yticks([])
ax.set_xticks([])
ax.set_title(f"Current Time: {h:02d}:{m:02d}:{s:02d}", fontdict={'fontsize': 16, 'fontweight': 'bold'})
plt.show()