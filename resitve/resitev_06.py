import turtle
import time

zelva = turtle.Turtle()
# tu je malo morje možnossti za prestaviti, na tej povezavi je turtle dokumentacija https://docs.python.org/3/library/turtle.html
zelva.penup()
zelva.fd(50)
zelva.lt(90)
zelva.fd(100)
time.sleep(0.5)
zelva.pendown()
zelva.circle(40)