# pip install pyfiglet colorama

# This script uses the PyFiglet library to print text in a stylized ASCII art format
# and the Colorama library to color the output in the terminal.
# The text is printed in green color using the Fore module from Colorama.
# The script demonstrates how to create a simple text-based interface with stylized output.
# The PyFiglet library allows for various font styles, and the Colorama library enables colored output in the terminal.

import pyfiglet
from colorama import Fore

def print_figlet(text):
    f = pyfiglet.figlet_format(text, font="slant")
    print(Fore.GREEN+f)

print_figlet("PyFiglet")
print_figlet("Hello, World!")
print_figlet("This is a test of PyFiglet.")
