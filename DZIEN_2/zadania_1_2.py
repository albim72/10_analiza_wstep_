# Definicja klasy Prostokat
class Prostokat:
    # Inicjalizacja zmiennych instancyjnych
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    # Metoda do obliczania obwodu
    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

    # Metoda do obliczania pola
    def pole(self):
        return self.dlugosc * self.szerokosc

    # Metoda do wyświetlania opisu prostokąta
    def opis(self):
        return f"Prostokąt o długości {self.dlugosc} i szerokości {self.szerokosc}."


# Tworzenie obiektu klasy Prostokat
moj_prostokat = Prostokat(5, 3)

# Obliczanie obwodu
print(f"Obwód prostokąta: {moj_prostokat.obwod()}")

# Obliczanie pola
print(f"Pole prostokąta: {moj_prostokat.pole()}")

# Wyświetlanie opisu prostokąta
print(moj_prostokat.opis())
