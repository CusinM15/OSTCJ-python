import turtle
import time

# Napiši funkcijo mnogokotnik(n, dolzina), ki nariše pravilni n-kotnik.

def mnogokotnik(n, dolzina):
    '''nariše mnogokotnik dolžine dolzina, n predstavlja število kotov'''
    # seveda bomo narisali pravilen n-kotnik, tako, da najprej izračunajmo kolikšen kot se bo potrebno sukati
    if n < 3:
        print('Ne moremo imeti negativni oz enakotnik/dvakotnik')
    else:
        kot = 360 / n
        zelva = turtle.Turtle() # ker tu v navodilu piše, da funkcija mnogokotnik sprejme zgolj n in dolžino bomo želva ustvarili znotraj funkcije, drugače vam to odsvetujem
        for _ in range(n):
            zelva.fd(dolzina)
            zelva.lt(kot)

if __name__ == '__main__':
    mnogokotnik(3, 100)
    time.sleep(1)