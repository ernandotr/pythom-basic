import matplotlib.pyplot as plt
import numpy as np

stars_x = np.random.rand(30) * 100
stars_y = np.random.rand(30) * 100

plt.scatter(stars_x, stars_y, color='white',  marker='*')
for i in range(10):
    a, b = np.random.randint(0, 30, 2)
    plt.plot( [ stars_x[a], stars_x[b]], [stars_y[a], stars_y[b] ] , "yellow")


plt.gca().set_facecolor('black')
plt.title("Constellation of Stars", color='white')
# plt.xlabel("X Coordinate", color='white')
# plt.ylabel("Y Coordinate", color='white')
# plt.tick_params(colors='white')
plt.show()