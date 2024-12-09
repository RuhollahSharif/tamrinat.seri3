import turtle
import random

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Barnsley Fern")
screen.setup(width=1200, height=1200)

fern = turtle.Turtle()
fern.hideturtle()
fern.speed(999)
fern.color("green")
fern.penup()

num_points = 20000

x, y = 0, 0

for _ in range(num_points):
    fern.goto(100 * x, 60 * y - 400)
    fern.pendown()
    fern.dot(3)
    fern.penup()

    rand = random.random()
    if rand < 0.02:
        x_new = 0
        y_new = 0.16 * y
    elif rand < 0.17:  # 0.02 + 0.15 = 0.17
        x_new = 0.2 * x - 0.26 * y
        y_new = 0.23 * x + 0.22 * y + 1.6
    elif rand < 0.30:  # 0.17 + 0.13 = 0.30
        x_new = -0.15 * x + 0.28 * y
        y_new = 0.26 * x + 0.24 * y + 0.44
    else:  # 0.30 + 0.70 = 1.00
        x_new = 0.85 * x + 0.04 * y
        y_new = -0.04 * x + 0.85 * y + 1.6

    x, y = x_new, y_new

screen.exitonclick()