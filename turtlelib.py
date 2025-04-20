import turtle
import math

t = turtle.Turtle()
t.speed(0)

raio = 100

for angulo in range(360):
    x = math.cos(math.radians(angulo)) * raio
    y = math.sin(math.radians(angulo)) * raio
    t.goto(x, y)

turtle.done()
