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

print('\033[32m\033[1m')  # Bold
for i, j in z:
    print(' ' * i + '*' * j)
print('\033[31m', end='')
for r in range(3):
    print(' ' * 13, ' || ')
print(' ' * 12, end= '\\======/')
print('\033[0m')  # Reset color
print('\033[32m\033[1m')  # Bold and underline]]')
# print(' '*8, end= "Merry Christmas!") # English
# print() 

messages = {"pt_BR": "Feliz Natal!",  # Portuguese (Brazil)
            "fr_FR": "Joyeux Noël!",  # French (France)
            "en_US": "Merry Christmas!"  # English (United States)
            } 
for lang, message in messages.items():
    print(f"{message:^32}")  # Print the message in the specified language
    print()  # New line after each message
# print(' ' * 8, end= "Ho Ho Ho!")  # English
print()  # New line after the last message
