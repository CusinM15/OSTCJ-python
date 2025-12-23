import turtle
from resitev_1 import narisi_kvadrat # uvozimo funkcijo ki smo jo spisali pri prvi nalogi
from resitev_2 import narisi_trikotnik # uvozimo funkcijo, ki smo jo naredili pri nalogi 2

zelva = turtle.Turtle()
d = 100
# Tu rabimo narisati kvadrat in trikotnik kar smo danes ze spisali zato bomo malo spremenili 1 in 2 nalogo in le te uporabili pri tej nalogi

narisi_kvadrat(zelva, 'red', d) # ta funkcija nariše kvadrat
# prestaviti moramo želvico, za dolžino gor
zelva.sety(d)
narisi_trikotnik(zelva, 'green', d) # ta funkcija nariše trikotnik