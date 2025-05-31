import numpy as np
import os
# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Christmas Tree Pattern using NumPy
# Create arrays for the x and y coordinates
# and stack them to form the tree structure
x = np.arange(7, 16)
y = np.arange(1, 18, 2)
z = np.column_stack((x[:: -1], y))

print()
for i, j in z:
    print(' ' * i + '*' * j)
for r in range(3):
    print(' ' * 13, ' || ')
print(' ' * 12, end= '\\======/')
print('')
print(' '*8, end= "Merry Christmas!") # English
print() 
