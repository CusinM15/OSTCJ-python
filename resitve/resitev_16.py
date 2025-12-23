import turtle
import time

velikost_polja = 240
premik = velikost_polja // 8 # celoštevilsko deljenje je dvojni / -> ta premik rabimo da vemo za koliko se rabimo premikati navzgor/navzdol/levo/desno
# središče bomo pustili na sredini, šli bomo torej v vse štiri smeri in na vsaki narisali 4

zelva = turtle.Turtle()
y_pozicija = 0
for _ in range(8):
    zelva.fd(velikost_polja)
    zelva.bk(velikost_polja)
    y_pozicija += premik
    zelva.goto(0, y_pozicija)
zelva.rt(90)
x_pozicija = 0
for _ in range(8): 
    x_pozicija += premik
    zelva.goto(x_pozicija, velikost_polja)

    zelva.fd(velikost_polja)
    zelva.bk(velikost_polja)
time.sleep(1)