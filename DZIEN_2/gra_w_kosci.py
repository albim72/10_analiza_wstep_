import numpy as np
import matplotlib.pyplot as plt

# Liczba symulowanych rzutów
num_throws = 1000

# Symulacja rzutów dwiema kośćmi
np.random.seed(42)  # Ustawienie ziarna losowości
dice1 = np.random.randint(1, 7, size=num_throws)  # Wyniki dla pierwszej kości (1-6)
dice2 = np.random.randint(1, 7, size=num_throws)  # Wyniki dla drugiej kości (1-6)

# Suma wyników z dwóch kości
suma_oczek = dice1 + dice2


# Obliczenie rozkładu sumy oczek
unique, counts = np.unique(suma_oczek, return_counts=True)
rozkład_sum = dict(zip(unique, counts))

# Wyświetlenie rozkładu wyników
print(f"Rozkład sum oczek: {rozkład_sum}")

# Tworzenie wykresu rozkładu sum oczek
plt.bar(unique, counts, color='blue', alpha=0.7, edgecolor='black')
plt.title('Rozkład sum oczek w 1000 rzutach dwiema kośćmi')
plt.xlabel('Suma oczek')
plt.ylabel('Liczba wystąpień')
plt.grid(True)
plt.show()
