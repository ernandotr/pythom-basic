import pyfiglet

def print_figlet(text):
    f = pyfiglet.Figlet(font='slant')
    print(f.renderText(text))

print_figlet("PyFiglet")
