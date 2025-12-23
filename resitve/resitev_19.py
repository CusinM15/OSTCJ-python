import turtle
import time

# Naredi program, kjer želva risanje sledi gibanju miškinega klika

def spremljaj_misko():
    """Želva sledi gibanju miškinega kazalca"""
    ekran = turtle.Screen()
    ekran.title("Spremljaj miško")
    ekran.setup(width=800, height=600)
    
    zelva = turtle.Turtle()
    zelva.shape("turtle")
    zelva.color("blue")
    zelva.speed(0)
    zelva.pensize(2)
    
    def pojdi_na_misko(x, y):
        """Premakne želvo na pozicijo miške"""
        zelva.goto(x, y)
    
    # Poveži klik miške z gibanjem želve
    ekran.onclick(pojdi_na_misko)
    
    # Če želiš, da želva sledi brez klika (bolj gladko):
    def sledi_misko(x, y):
        zelva.setheading(zelva.towards(x, y))
        zelva.goto(x, y)
    
    ekran.onscreenclick(sledi_misko)
    
    ekran.mainloop()

spremljaj_misko()
