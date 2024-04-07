# %%
import math
import matplotlib.pyplot as plt
import numpy as np
# %% Zadanie 1 i 2
def f(x):
    return (x - 2)**3 - x**2 + 2*x

def metoda_połowienia(f, a, b, eps=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Wartości funkcji na krańcach przedziału muszą mieć przeciwne znaki.")
    
    liczba_iteracji = 0
    punkty_iteracyjne = []
    while liczba_iteracji < max_iter:
        liczba_iteracji += 1
        c = (a + b) / 2
        punkty_iteracyjne.append(c)
        
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


wynik, punkty_iteracyjne = metoda_połowienia(f, 1.5, 3, eps=10**-6, max_iter=100)
print("Otrzymany wynik:", wynik)
wizualizacja_punktow_iteracyjnych(f, 1.5, 3, punkty_iteracyjne)

wynik, punkty_iteracyjne = metoda_połowienia(f, 1, 2, eps=10**-6, max_iter=100)
print("Otrzymany wynik:", wynik)
wizualizacja_punktow_iteracyjnych(f, 1, 2, punkty_iteracyjne)

wynik, punkty_iteracyjne = metoda_połowienia(np.sin, 3, 5, eps=10**-6, max_iter=100)
print("Otrzymany wynik:", wynik)
wizualizacja_punktow_iteracyjnych(np.sin, 3, 5, punkty_iteracyjne)

#  %% Zadanie 3 i 4

def newton(f, x0, eps=10**-6, max_iter=100):
    h = 10**-7
    iter_count = 0
    
    while True:
        iter_count += 1
        if iter_count > max_iter:
            return None
        
        pochodna = (f(x0 + h) - f(x0)) / h
        x1 = x0 - f(x0) / pochodna
        
        if abs(x1 - x0) < eps:
            return x1
        
        x0 = x1

def newton_visualization(f, x0, eps=10**-6, max_iter=100):
    h = 10**-7
    iter_count = 0

    x_vals = np.linspace(x0 - 2, x0 + 2, 100)
    y_vals = f(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, 'b-', label='f(x)')
    ax.grid(True, linestyle='--', alpha=0.7)

    ax.plot(x0, f(x0), 'ro', label='x0')

    while True:
        iter_count += 1
        if iter_count > max_iter:
            print("Osiągnięto maksymalną liczbę iteracji.")
            return None

        x = newton(f, x0, eps, max_iter)
        if x is None:
            print("Osiągnięto maksymalną liczbę iteracji.")
            return None

        pochodna = (f(x + h) - f(x)) / h
        x1 = x - f(x) / pochodna

        tangent_x = np.array([x1 - 2, x1 + 2])
        tangent_y = f(x1) + pochodna * (tangent_x - x1)
        ax.plot(tangent_x, tangent_y, 'r--', label=f'Tangenta {iter_count}')

        if abs(x1 - x) < eps:
            ax.plot(x1, f(x1), 'ro', label='Pierwiastek')

            ax.set_xlabel('x')
            ax.set_ylabel('f(x)')
            plt.show()
            return x1

def f2(x):
    return (x - 2)**2 - 1

def f3(x):
    return (x - 2)**3 - x**2 + 2*x

def f4(x):
    return x**2 - 2

def f5(x):
    return x**3 - 2*x + 2 

print(newton_visualization(f2, 4)) 
print(newton_visualization(f3, 1.5)) 
print(newton_visualization(f4, 2)) 
print(newton_visualization(np.sin, 3)) 
print(newton_visualization(f5, 0)) 



























