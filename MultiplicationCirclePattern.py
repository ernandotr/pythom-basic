import turtle, math
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("cyan")

n = 50; m = 2

for i in range(n):
    t.penup()
    t.goto(200 * math.cos(2 * math.pi * i / n), 200 * math.sin(2 * math.pi * i / n))
    t.pendown()
    j = (i * m) % n
    t.goto(200 * math.cos(2 * math.pi * j / n), 200 * math.sin(2 * math.pi * j / n))
turtle.done()