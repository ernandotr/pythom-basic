# pip install schemdraw
# https://schemdraw.readthedocs.io/en/stable/index.html

import schemdraw
import schemdraw.elements as elm
# This script uses the Schemdraw library to create a simple electrical circuit diagram.

def create_circuit_diagram():

    # with schemdraw.Drawing() as d:
    #     elm.Resistor().label('100KΩ')
    #     elm.Capacitor().down().label('0.1μF', loc='bottom')
    #     elm.Line().left()
    #     elm.Ground()
    #     elm.SourceV().up().label('10V')
    #     d.draw()


    # Create a simple circuit with a battery, resistor, and LED
    d = schemdraw.Drawing()    
    d += elm.Battery().label('Battery').up()
    d += elm.Resistor().label('Resistor').right()
    d += elm.LED().label('LED').down()
    
    # Connect the elements
    d += elm.Line().tox(0)  # Connect the last element back to the first

    # Save the drawing to a file
    d.save('circuit_diagram.svg')
    print("Circuit diagram created successfully.")
    d.draw()

if __name__ == "__main__":
    create_circuit_diagram()
