import turtle
import time
# Nariši cvet z 8 cvetnimi listi, nariši mnogokotnik in poveži središče z vsakim ogliščem, za cvet dodaj krog in se malo potrudi z barvami.
# Določimo naše spremenljivke
r = 100
n = 8
barva_cvet = 'red'
barva_listi = 'green'
def narisi_cvetico_mnogokotnik(zelva, r, n, barva_cvet, barva_listi):
    '''nariše mnogokotnik dolžine dolzina, n predstavlja število kotov'''
    koordinate_tock = list()
    
    if n <= 2:
        print('Nič, negativno število, ena in dva kotnik ne obstajajo!')
    
    kot = 360 / n
    
    # 1. KORAK: Zberi koordinate oglišč in nariši črte od središča
    for _ in range(n):
        zelva.fd(r)
        koordinate_tock.append(zelva.pos())
        zelva.bk(r)
        zelva.lt(kot)
    
    # 2. KORAK: Napolni obliko (z vidnim robom)
    zelva.pencolor('black')  # Barva roba
    zelva.pensize(2)  # Debelina roba
    zelva.fillcolor(barva_listi)
    zelva.penup()
    zelva.goto(koordinate_tock[0])
    zelva.pendown()  # POMEMBNO: spusti pero
    zelva.begin_fill()
    for kam in range(n):
        zelva.goto(koordinate_tock[kam])
    zelva.goto(koordinate_tock[0])
    zelva.end_fill()
    
    # Vrni se v središče
    zelva.penup()
    zelva.goto(0, 0)
    zelva.pendown()
    for _ in range(n): # dorišemo povezavo za liste znova
        zelva.fd(r)
        zelva.bk(r)
        zelva.lt(kot)
    # sedaj pa rabimo narisati še cvet
    zelva.fillcolor(barva_cvet)
    zelva.begin_fill()
    zelva.penup()
    zelva.goto(0, -r / 2)
    zelva.pendown()
    zelva.circle(r / 2)
    zelva.end_fill()

zelva = turtle.Turtle()
koordinate = narisi_cvetico_mnogokotnik(zelva, r, n, barva_cvet, barva_listi)# uporabimo 13 nalogo da dobimo koordinate koncev listov
# dodal bom med vsako točki še dve točki 
time.sleep(1)

# narejeno malo drugače, zahteva poznavanje vektorjev, toda ne uporabimo mnogokotnika za liste
import math
from resitev_13 import narisi_pike_krog

def točke_na_simetrali(x1, y1, x2, y2, t):
    '''funkcija nam izračuna, dve dodatni točki, ki sta enako oddaljeni od dveh točk in od razpolovišča daljice oddaljeni za t'''
    # Razpolovišče
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    
    # Vektor daljice
    dx = x2 - x1
    dy = y2 - y1
    
    # Dolžina
    dolžina = math.sqrt(dx**2 + dy**2)
    
    # Normaliziran pravokotni vektor
    nx = -dy / dolžina
    ny = dx / dolžina
    
    # Točki na simetrali
    p1 = (mx + t * nx, my + t * ny)
    p2 = (mx - t * nx, my - t * ny)
    
    return p1, p2

zelva.home()
zelva.clear()

koordinate_druga = narisi_pike_krog(zelva, r, n)
koordinate_z_dodatki = list()
zelva.fillcolor(barva_listi)
zelva.begin_fill()
zelva.pendown()
for tocka in koordinate_druga:
    t1, t2 = točke_na_simetrali(tocka[0], tocka[1], 0, 0, 10)
    zelva.goto(t1)
    zelva.goto(tocka)
    zelva.goto(t2)
    zelva.home()
zelva.end_fill()

# sedaj pa narišimo še cvet
zelva.penup()
zelva.goto(0, -r/4)
zelva.pendown()
zelva.fillcolor(barva_cvet)
zelva.begin_fill()
zelva.circle(r / 4)
zelva.end_fill()
time.sleep(2)
