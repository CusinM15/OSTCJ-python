import turtle

def narisi_trikotnik(zelva, barva,  d):
    zelva.speed(1)
    zelva.color(barva)
    zelva.fd(d)
    zelva.lt(120)
    zelva.fd(d)
    zelva.lt(120)
    zelva.fd(d)
    
if __name__ == '__main__':
    zelva = turtle.Turtle()
    
    # Naredimo ročno

    zelva.forward(90)
    # v enakostraničnem trikotniku so vsi trije koti enaki, ker je vsota notranjih kotov trikotnika 180, je torej en enak 60
    # zasukati pa se moramo za zunanji kot, notranji + zunanji kot je tudi 180, zato sučemo za 120
    zelva.left(120)
    zelva.forward(90)
    zelva.left(120)
    zelva.forward(90)

    # Še z zanko
    # spremenimo barvo in zasučemo, da prerišemo prejšni trikotnik
    zelva.left(120)
    zelva.color('blue')
    for _ in range(3):
        zelva.forward(90)
        zelva.left(120)