#przykład 0
def przykladowa():
    return 567

print(przykladowa())

def brak():
    print("to jest funkcja która tylko wyświetla komunikat!")

brak()

def policz(a,b):
    return a+(b-2)**2

print(policz(3,6))

#przykład 1
#funkcja jako obiekt pierwszej klasy

def przyjmij_funkcje(f,x):
    return f(x)

def podwoj(x):
    return x*2


def podniesienie(y):
    return y + 22

wynik = przyjmij_funkcje(podwoj,5)
print(wynik)

nextwynik = przyjmij_funkcje(podniesienie,57)
print(nextwynik)

#przykład 2
#funkcje anonimowe (lambda)
print((lambda e:e+5)(6))
pd = lambda x:x*2
print(pd(19))
