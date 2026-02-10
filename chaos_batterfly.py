import numpy as np
import matplotlib.pyplot as plt

x=y=z=0.1
dt=0.01; xs=[]; ys=[];
for _ in range(10000):
    dx=10*(x-y)
    dy=x*(28-z)-y
    dz=x*y-8/3*z
    x+=dx*dt; y+=dy*dt; z+=dz*dt
    xs.append(x); ys.append(y)
plt.plot(xs, ys, linewidth=0.5)
plt.axis("off")
plt.show()