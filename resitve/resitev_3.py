import turtle
zelva = turtle.Turtle()

# Naredimo ročno

zelva.forward(90)
zelva.left(60)
zelva.color('blue')
zelva.forward(90)
zelva.left(60)
zelva.color('red')
zelva.forward(90)
zelva.left(60)
zelva.color('green')
zelva.forward(90)
zelva.left(60)
zelva.color('orange')
zelva.forward(90)
zelva.left(60)
zelva.color('yellow')
zelva.forward(90)

# Naredimo z zanko in barvo izberemo naključno, zato rabimo uporabiti tudi knjižnico random
from random import random
# počistimo zaslon
zelva.clear()
# obrnimo želvo da gre po isti poti
zelva.left(60)

for _ in range(6):
    zelva.color(random(), 
          random(), 
          random())
    zelva.forward(100)
    zelva.left(60)
    