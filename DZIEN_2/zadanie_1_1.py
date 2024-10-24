from typing import Any
# Funkcja wyższego rzędu przyjmująca dwie funkcje i wartość x
def funkcja_wyzszego_rzedu(f1:Any, f2:Any, x:float)->float:
    return f1(x) + f2(x)

# Definicja dwóch funkcji do przekazania jako argumenty
def podwoj(x:float)->float:
    return x * 2

def kwadrat(x:float)->float:
    return x ** 2

# Przykład użycia funkcji wyższego rzędu
x = 5.5
wynik = funkcja_wyzszego_rzedu(podwoj, kwadrat, x)

print(f"Wynik dla x = {x} wynosi: {wynik}")




d:int = 8
print(d)
print(type(d))

print(isinstance(d,(int,float)))
d = "osiem"
print(d)
print(type(d))

if isinstance(d,(int,float)):
    print(d)
else:
    raise Exception("zły typ")
