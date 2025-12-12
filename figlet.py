# pip install pyfiglet colorama

# This script uses the PyFiglet library to print text in a stylized ASCII art format
# and the Colorama library to color the output in the terminal.
# The text is printed in green color using the Fore module from Colorama.
# The script demonstrates how to create a simple text-based interface with stylized output.
# The PyFiglet library allows for various font styles, and the Colorama library enables colored output in the terminal.

import pyfiglet
from termcolor import colored
import random

def getradom_font():
    fonts = pyfiglet.FigletFont.getFonts()
    font = random.choice(fonts);
    print(f"Selected font: {font}")
    return font;

def getrandom_color():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    return random.choice(colors)

def wish_mothers_day():
    text = "Happy Mother's Day!"
    font = getradom_font()
    color = getrandom_color()
    ascii_art = pyfiglet.figlet_format(text, font=font)
    colored_art = colored(ascii_art, color)
    print(colored_art)

wish_mothers_day()
