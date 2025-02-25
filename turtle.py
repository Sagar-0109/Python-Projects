import turtle
import colorsys

# Setup turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
turtle.colormode(255)

# Color setup
h = 0
n = 36  # Number of colors
colors = [colorsys.hsv_to_rgb(h + i/n, 1, 1) for i in range(n)]
colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]

# Drawing pattern
for i in range(180):
    t.pencolor(colors[i % n])
    t.circle(i * 0.5, 90)
    t.left(90)
    t.circle(i * 0.5, 90)
    t.left(18)

turtle.done()
