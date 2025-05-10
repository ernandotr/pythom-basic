from pyfiglet import Figlet

def print_figlet(text):
    f = Figlet(font='slant')
    print(f.renderText(text))

print_figlet("Hello, World!")
print_figlet("Python")
print_figlet("Ernando")