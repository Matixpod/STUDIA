# %%
import math
import matplotlib.pyplot as plt
import numpy as np
# %% Zadanie 1

def metoda_połowienia(f, a, b, eps=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Wartości funkcji na krańcach przedziału muszą mieć przeciwne znaki.")
    
    liczba_iteracji = 0
    punkty_iteracyjne = []  # Lista do przechowywania punktów w kolejnych iteracjach
    while liczba_iteracji < max_iter:
        liczba_iteracji += 1
        c = (a + b) / 2
        punkty_iteracyjne.append(c)  # Dodaj aktualną wartość środka przedziału do listy
        
        if abs(f(c)) < eps:
            return c, punkty_iteracyjne
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    print("Osiągnięto maksymalną liczbę iteracji bez uzyskania zbieżności.")
    return None, punkty_iteracyjne

def wizualizacja_punktow_iteracyjnych(f, a, b, punkty_iteracyjne):
    x = np.linspace(a, b, 100)
    y = f(x)
    
    plt.plot(x, y, label="f(x)")
    # Zamiast plt.scatter używamy plt.vlines
    plt.vlines(punkty_iteracyjne, np.min(y), np.max(y), color='red', linestyle='--', label="Punkty iteracyjne")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Wizualizacja metody połowienia')
    plt.legend()
    plt.grid(True)
    plt.xlim(np.min(x), np.max(x))
    plt.ylim(np.min(y), np.max(y))
    plt.show()

# Testy
wynik, punkty_iteracyjne = metoda_połowienia(f1, 1.5, 3, eps=10**-6, max_iter=100)
print("Otrzymany wynik:", wynik)
wizualizacja_punktow_iteracyjnych(f1, 1.5, 3, punkty_iteracyjne)

wynik, punkty_iteracyjne = metoda_połowienia(f2, 1, 2, eps=10**-6, max_iter=100)
print("Otrzymany wynik:", wynik)
wizualizacja_punktow_iteracyjnych(f2, 1, 2, punkty_iteracyjne)

wynik, punkty_iteracyjne = metoda_połowienia(np.sin, 3, 5, eps=10**-6, max_iter=100)
print("Otrzymany wynik:", wynik)
wizualizacja_punktow_iteracyjnych(np.sin, 3, 5, punkty_iteracyjne)

