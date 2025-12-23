import turtle
import time

def narisi_drevo(zelva, dolzina, kot=45, faktor=0.8, min_dolzina=5):
    """
    Rekurzivno nariše fraktalno drevo
    
    Args:
        zelva: turtle objekt
        dolzina: dolžina trenutne veje
        kot: kot razvejanja (privzeto 45°)
        faktor: faktor krajšanja naslednje veje (privzeto 0.8 = 20% krajša)
        min_dolzina: minimalna dolžina veje pred ustavitvijo
    """
    if dolzina < min_dolzina:
        # Nariši zeleno piko za list
        zelva.pencolor("green")
        zelva.pensize(5)
        zelva.forward(1)
        zelva.backward(1)
        return
    
    # Nastavi barvo in debelino glede na dolžino veje
    if dolzina > 30:
        zelva.pencolor("brown")
        zelva.pensize(dolzina / 10)
    else:
        zelva.pencolor("darkgreen")
        zelva.pensize(2)
    
    # Nariši trenutno vejo
    zelva.forward(dolzina)
    
    # Desna veja
    zelva.right(kot)
    narisi_drevo(zelva, dolzina * faktor, kot, faktor, min_dolzina)
    
    # Vrnitev na razvejišče
    zelva.left(kot)
    
    # Leva veja
    zelva.left(kot)
    narisi_drevo(zelva, dolzina * faktor, kot, faktor, min_dolzina)
    
    # Vrnitev nazaj
    zelva.right(kot)
    zelva.penup()
    zelva.backward(dolzina)
    zelva.pendown()


def puhasto_drevo():
    """Glavni program za risanje puhasega drevesa"""
    ekran = turtle.Screen()
    ekran.title("Puhasto drevo - Rekurzija")
    ekran.setup(width=800, height=800)
    ekran.bgcolor("lightblue")
    
    zelva = turtle.Turtle()
    zelva.speed(0)
    zelva.left(90)  # Obrni navzgor
    zelva.penup()
    zelva.goto(0, -300)  # Začni na dnu
    zelva.pendown()
    
    # Nariši drevo
    narisi_drevo(zelva, dolzina=100, kot=30, faktor=0.75, min_dolzina=15)
    
    zelva.hideturtle()
    ekran.mainloop()

puhasto_drevo()