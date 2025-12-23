import turtle
import time

from resitev_13 import narisi_pike_krog

zelva = turtle.Turtle()
koordinate = narisi_pike_krog(zelva, 100, 5)
# sedaj smo spremenili funkcijo iz 13 tako, da nam vrne koordinate oglišč, da narišemo zvezdo s pomočjo pravilnega petkotnika, postavimo vrstni red po katerem se mora izvajati

vrsti_red = [2, 4, 1, 3, 0] # začnemo iz 1 do 3
# prestavimo v koordinato z indeksom 0 brez črte (torej penup)
zelva.penup()
zelva.goto(koordinate[0])
zelva.pendown()
for kam in vrsti_red: 
    zelva.goto(koordinate[kam])
time.sleep(1)