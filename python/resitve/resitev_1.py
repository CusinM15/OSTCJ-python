import turtle
# if __name__ == '__main__': samo pomeni, da se izvede zgolj, ko zaganjamo to datoteko v tem primeru resitev_1.py, če kličemo funkcijo nariši kvadrat v drugi datoteki se to znotraj te zanke ne izvede
def narisi_kvadrat(zelva, barva, d):
    zelva.color(barva) 
    for _ in range(4):
        zelva.forward(d)
        zelva.left(90)

if __name__ == '__main__':
    zelva = turtle.Turtle()

    # Naredimo "ročno"
    zelva.forward(100)
    zelva.left(90)
    zelva.forward(100)
    zelva.left(90)
    zelva.forward(100)
    zelva.left(90)
    zelva.forward(100)
    # Naredimo s pomočjo zanke
    # da se bo videlo in če bi radi, da gre čez prejšen kvadrat moramo želvo še obrniti za 90
    zelva.left(90)
    narisi_kvadrat(zelva, 'red', 100)