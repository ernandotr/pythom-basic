import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1),
          (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
for x, y, z in points:
    ax.scatter(x, y, z, s=60)

edges = [(0, 1), (0, 2), (0, 3), (7, 4), (7, 5), (7, 6), (1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6)]
for i, j in edges:
    ax.plot(*zip(points[i], points[j]))

ax.set_title('Simple Cube unit cell')
ax.axis('off')
plt.show()
