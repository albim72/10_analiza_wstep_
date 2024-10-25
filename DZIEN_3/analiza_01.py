# Importowanie niezbędnych bibliotek
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Ustawienia wykresów Seaborn
sns.set(style="whitegrid")

# 1. Wczytanie danych z przykładowego pliku CSV (wzrost, waga)

df = pd.read_csv("height_weight_sample.csv")

# 2. Przetwarzanie danych
# Wstępne statystyki opisowe
print("Podstawowe statystyki opisowe:")
print(df.describe())

# 3. Analiza statystyczna z wykorzystaniem SciPy
# Wyliczamy korelację między wzrostem a wagą
correlation, p_value = stats.pearsonr(df['height'], df['weight'])
print(f"Korelacja między wzrostem a wagą: {correlation:.2f}, wartość p: {p_value:.2e}")

# 4. Tworzenie modelu regresji liniowej
# Dopasowanie modelu liniowego
slope, intercept, r_value, p_value, std_err = stats.linregress(df['height'], df['weight'])

# Funkcja liniowa do predykcji
def predict(weight):
    return slope * weight + intercept

# Predykcja wag na podstawie wzrostu
df['predicted_weight'] = predict(df['height'])

# 5. Wizualizacja wyników
plt.figure(figsize=(10, 6))

# Wykres punktowy wzrost-waga
sns.scatterplot(data=df, x='height', y='weight', label="Dane rzeczywiste")

# Dodanie linii regresji
plt.plot(df['height'], df['predicted_weight'], color="red", label="Linia regresji")

# Tytuł i etykiety osi
plt.title(f"Analiza wzrostu a wagi (korelacja = {correlation:.2f})")
plt.xlabel("Wzrost (cm)")
plt.ylabel("Waga (kg)")
plt.legend()

plt.show()
