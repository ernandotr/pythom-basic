import turtle

def draw_olympic_rings(color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(50)# Draw a circle with radius 50

turtle.speed(5)
turtle.width(5)
draw_olympic_rings("blue", -120, 0)
draw_olympic_rings("black", 0, 0)
draw_olympic_rings("red", 120, 0)
draw_olympic_rings("yellow", -60, -50)
draw_olympic_rings("green", 60, -50)
turtle.hideturtle()
turtle.done()
