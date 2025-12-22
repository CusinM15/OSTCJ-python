import turtle
import time

# Z uporabo zanke in seznama barv nariši 8-kotnik, kjer ima vsaka stran drugačno barvo.


# Tu bi drugače lahko dodelali, funkcijo iz naloge 11 (vam priporočam, da le tisto spremenite, da sprejme tudi tabelo barv oz generira zadostno število barv)
kot = 360 / 8
zelva = turtle.Turtle() 
tabela_barv = ['red', 'green', 'purple', 'pink', 'blue', 'black', 'orange', 'yellow'] 
for barva in tabela_barv: # tokrat iteriramo po tabeli v spremenljivki pred in v tem primeru barva imamo barve iz tabele 
    zelva.color(barva)
    zelva.fd(100)
    zelva.lt(kot)

time.sleep(1)