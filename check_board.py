import numpy as np
import matplotlib.pyplot as plt

def check_board(size=8):
    board = np.indices((size, size)).sum(axis=0) % 2

    plt.figure(figsize=(6, 6))
    plt.imshow(board, cmap='gray', interpolation='nearest')

    plt.xticks([])
    plt.yticks([])
    plt.title(f"{size}x{size} Checkerboard Pattern", fontsize=14, fontweight='bold')

    plt.show()

check_board(8)