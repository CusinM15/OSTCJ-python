import turtle
import time

# Nariši 10 vodoravnih črt, kjer se debelina in barva črte postopoma spreminjata.

velikost_polja = 100
premik = 15

zelva = turtle.Turtle()
y_pozicija = 0

for pisava in range(1, 11):
    zelva.pensize(pisava)
    zelva.fd(velikost_polja)
    zelva.bk(velikost_polja)
    y_pozicija += premik
    zelva.penup()
    zelva.goto(0, y_pozicija)
    zelva.pendown()