import turtle
import time

# Nariši 12 enakih črt, ki se izvirajo iz iste točke in so enakomerno razporejene (kot žarki sonca).

# Celoten krog ima 360° radi bi naredili tako, da so razporejeni enakomerno za 12 žarkov, toda, ker je praktično enako treba narediti, za katerokoli številko bomo naredili funkcijo, ki število črt dobi kot parameter v funkcijo



def narisi_krozni_vzorec(zelva, st, dolzina):
    '''
        Funkcija nariše st žarkov iz iste točke dolžina žarkov je enaka spremenljivki dolzina, 
        enakomerno porazdeljene čez cel krog.
    '''
    if st <= 0:
        print('nič oz negativno število žarkov ne moremo izpisati')
    else:
        kot = 360 / st # določimo kot za katerega se moramo premikati
        for _ in range (st):
            zelva.fd(dolzina) # narisali smo prvi krak sedaj se vrnimo nazaj na izhodišče, tu je več možnosti
            zelva.bk(dolzina)
            zelva.lt(kot)

if __name__ == '__main__':
    zelva1 = turtle.Turtle()
    narisi_krozni_vzorec(zelva1, 12, 100)
    time.sleep(1)