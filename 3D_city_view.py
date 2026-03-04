import pyvista as pv
import numpy as np

plotter = pv.Plotter()
for i in range(5):
    for j in range(5):
        h = np.random.randint(5, 20)
        box = pv.Box(bounds=(i, i+1, j, j+1, 0, h))
        plotter.add_mesh(box, color="lightblue", show_edges=True)
plotter.show(title="3D City View", window_size=(800, 600))
