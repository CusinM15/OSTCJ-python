import turtle
import time

def utripajoci_krog():
    """Krog se 5-krat povečuje in zmanjšuje"""
    ekran = turtle.Screen()
    ekran.title("Utripajoč krog")
    
    zelva = turtle.Turtle()
    zelva.speed(0)
    zelva.hideturtle()
    
    # Parametri
    min_polmer = 20
    max_polmer = 100
    korak = 5
    
    for _ in range(5):  # 5 utripov
        # Povečevanje
        for polmer in range(min_polmer, max_polmer, korak):
            zelva.clear()
            zelva.penup()
            zelva.goto(0, -polmer)
            zelva.pendown()
            zelva.circle(polmer)
            ekran.update()
            time.sleep(0.05)
        
        # Zmanjševanje
        for polmer in range(max_polmer, min_polmer, -korak):
            zelva.clear()
            zelva.penup()
            zelva.goto(0, -polmer)
            zelva.pendown()
            zelva.circle(polmer)
            ekran.update()
            time.sleep(0.05)


utripajoci_krog()