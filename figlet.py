import pyfiglet
from colorama import Fore

def print_figlet(text):
    f = pyfiglet.figlet_format(text, font="slant")
    print(Fore.GREEN+f)

print_figlet("PyFiglet")
print_figlet("Hello, World!")
print_figlet("This is a test of PyFiglet.")
