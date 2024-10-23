#import modułów wbudodwanych w interpreter pythona
import math as mh
#importy bibliotek zewnętrznych
import numpy as np
#importy bibliotek własnych
import specjalny as sp
from ekstraklasa.kolory import Kolory

#wynik działania math
wynik = mh.sqrt(15)

print(f"wynik: {wynik:.3f}")

wynik2 = mh.pi
print(f"wartośc pi: {wynik2}")

#wynik działania numpy
tablica = np.array([4,7,24,7,24])
print(tablica)

#wynik działania sp
print(sp.kolor)
print(sp.LICZBA_SZTUK)
print(sp.filia)

print(sp.powitanie("Karol"))
print(sp.policz(4,8))

#wynik celowego importu Kolory
kl = Kolory("zielony",111)
print(kl.jakikod())
