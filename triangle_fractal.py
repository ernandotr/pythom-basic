import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("cyan")

def draw_triangle_fractal(length, depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        draw_triangle_fractal(length / 2, depth - 1)
        t.forward(length / 2)
        draw_triangle_fractal(length / 2, depth - 1)
        t.backward(length / 2)
        t.left(60)
        t.forward(length / 2)
        t.right(60)
        draw_triangle_fractal(length / 2, depth - 1)
        t.left(60)
        t.backward(length / 2)
        t.right(60)
draw_triangle_fractal(300, 4)
turtle.done()