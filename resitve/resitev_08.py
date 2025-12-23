import turtle
import time
from resitev_1 import narisi_kvadrat

# Z uporabo zanke nariši 5 kvadratov, kjer se vsak naslednji začne znotraj prejšnjega in je za 20 manjši.

# Ker smo kvadrat že naredili v nalogi 1 bomo uvozili funkcijo iz resitev_1
dolzina_kvadrata = 200 # določimo velikost prvega kvadrata, mora biti dovolj velik da lahko 5 krat odštejemo 20

zelva = turtle.Turtle()
barve_tabela = ['red', 'green', 'purple', 'pink', 'blue'] # barve so zgolj plus del, lahko sami še bolj sčarate, jaz jih bom zgolj po vrsti vstavljal
for i in range(5):
    narisi_kvadrat(zelva, barve_tabela[i], dolzina_kvadrata - i * 20)
time.sleep(1)
