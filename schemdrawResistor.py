import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
d.add(elm.Resistor().label('R1'))
d.add(elm.Line())

d.save('schemdraw_resistor.svg')
print("Drawing saved as schemdraw_resistor.svg.")

d.draw()
print("Resistor drawing created successfully.")