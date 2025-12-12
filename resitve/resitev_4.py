import turtle
import time
zelva = turtle.Turtle()
# Začni barvanje
zelva.fillcolor("green")  # nastavi barvo zapolnitve
zelva.begin_fill()         # začni beleženje oblike za barvanje


# Naredimo "ročno"
zelva.forward(120)
zelva.left(90)
zelva.forward(120)
zelva.left(90)
zelva.forward(120)
zelva.left(90)
zelva.forward(120)
zelva.fillcolor('green')

zelva.end_fill()
# Pavza pred zapiranjem
time.sleep(1)  # 1 sekunda pavze

# počistimo ekran
zelva.clear()
# Začni barvanje
zelva.fillcolor("purple")  # nastavi barvo zapolnitve
zelva.begin_fill()         # začni beleženje oblike za barvanje
# Naredimo s pomočjo zanke
# da se bo videlo in če bi radi, da gre čez prejšen kvadrat moramo želvo še obrniti za 90
zelva.left(90)

zelva.color('red') 
for _ in range(4):
    zelva.forward(120)
    zelva.left(90)

# tega pa napolnili z vijolično
zelva.end_fill()
# Pavza pred zapiranjem
time.sleep(1)  # 1 sekunda pavze
