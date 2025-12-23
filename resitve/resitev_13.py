import turtle
import time

# Nariši 10 majhnih krogov (pik) enakomerno razporejenih po obodu velikega kroga.

# Ta naloga kar piše po uporabi funkcije, da je ta 10, lahko spremenljiv

def narisi_pike_krog(zelva, r, n):
    '''nariše n enakomerno razporejenih pik po krožnem obodu, r je polmer krožnice na kateri bodo ležale točke'''
    # vzemimo da je naše izhodišče naše koordinato izhodišče, ima koordinati (0, 0)
    # ker vemo da so točke na krožnici enako oddaljene oz središča bomo vsako točko risali
    # iz središča in se tja tudi vračali
    koordinate_tock = list() # vrnili bomo seznam koordinat n-kotnika
    if n <= 0:
        print('Nič oziroma negativno število točk ne moremo izpidati!')
    else:
        kot = 360 / n
        for _ in range(n):
            zelva.penup() # dvignemo pero
            zelva.fd(r) # premaknemo na željeni prostor
            zelva.dot()
            koordinate_tock.append(zelva.pos())
            zelva.bk(r)
            zelva.lt(kot)
        return koordinate_tock

if __name__ == '__main__':
    zelva1 = turtle.Turtle()
    narisi_pike_krog(zelva1, 100, 10)