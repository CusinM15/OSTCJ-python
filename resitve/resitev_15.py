import turtle
import time
from resitev_13 import narisi_pike_krog
# Nariši cvet z 8 cvetnimi listi, kjer je vsak list sestavljen iz dveh lokov.

def create_arc(turtle, x1, y1, x2, y2, start=0, extent=90):

    radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
    cx, cy = x1 + (x2 - x1) / 2, y1 + (y2 - y1) / 2

    turtle.penup()
    turtle.setposition(max(x1, x2), cy)
    turtle.setheading(90)
    turtle.circle(radius, extent=start)
    position = turtle.position()

    turtle.pendown()
    turtle.circle(radius, extent=extent)
    turtle.setposition(cx, cy)
    turtle.setposition(position)

zelva = turtle.Turtle()
koordinate = narisi_pike_krog(zelva, 100, 8) # uporabimo 13 nalogo da dobimo koordinate koncev listov
# zelva.penup()
# zelva.fd(50)
# zelva.pendown()
zelva.pendown()
# zelva.circle(50)
create_arc(zelva, koordinate[0][0], koordinate[0][1], koordinate[1][0], koordinate[1][1])
time.sleep(1)