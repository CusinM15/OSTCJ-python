import turtle
import time

# Nariši kvadratno spiralo z uporabo zanke, kjer se dolžina stranice vsakič poveča za 5.

def narisi_spiralo(zelva, dolzina, povecava, stevilo_obratov):
    for _ in range(stevilo_obratov):
        zelva.fd(dolzina)
        zelva.lt(90)
        dolzina += povecava


if __name__ == '__main__':
    zacetna_dolzina = 1
    povecava = 5
    stevilo_obratov = 20
    zelva1 = turtle.Turtle()
    narisi_spiralo(zelva1, zacetna_dolzina, povecava, stevilo_obratov)