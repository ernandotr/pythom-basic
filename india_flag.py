import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def draw_india_flag():
    # Flag dimensions
    width = 1.5
    height = 1.0

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(width * 5, height * 5))

    # Draw the three stripes
    ax.add_patch(Rectangle((0, 0), width, height / 3, color='#FF9933'))  # Saffron
    ax.add_patch(Rectangle((0, height / 3), width, height / 3, color='white'))  # White
    ax.add_patch(Rectangle((0, 2 * height / 3), width, height / 3, color='#138808'))  # Green

    # Draw the Ashoka Chakra
    chakra_center = (width / 2, height / 2)
    chakra_radius = height / 6
    chakra = plt.Circle(chakra_center, chakra_radius, color='#000080', fill=False, linewidth=2)
    ax.add_patch(chakra)

    # Draw the 24 spokes
    for i in range(24):
        angle = i * (360 / 24)
        x_end = chakra_center[0] + chakra_radius * np.cos(np.radians(angle))
        y_end = chakra_center[1] + chakra_radius * np.sin(np.radians(angle))
        ax.plot([chakra_center[0], x_end], [chakra_center[1], y_end], color='#000080', linewidth=1)

    # Set limits and aspect
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide axes

    # Show the flag
    plt.show()
draw_india_flag()
