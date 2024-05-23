# %%
import scipy
import math
import matplotlib.pyplot as plt
import numpy as np


# %% Zadanie 1
def f1(x):
    return (x-2)**3 - x**2 + 2*x

def f2(x):
    return x**2 - 2

def f3(x):
    return math.sin(x)

def f4(x):
    return x**3 - 2*x + 2

print(scipy.optimize.fsolve(f1,x0 = 1.5))
print(scipy.optimize.fsolve(f2,x0 = 2))
print(scipy.optimize.fsolve(f3,x0 = 3))
print(scipy.optimize.fsolve(f4,x0 = -1))

# %% Zadanie 2


def f5(x):
    return x**3

def f6(x):
    return (x**3 - 6*x**2 + 9*x + 2)

def f7(x):
    return (math.sin(2*x)+1)

def f8(x):
    return ((math.sin(8*x))/x+1)

print(scipy.integrate.quad(f5,0,2))
print(scipy.integrate.quad(f6,0,4))
print(scipy.integrate.quad(f7,0,math.pi))
print(scipy.integrate.quad(f8,1,4))


# %% Zadanie 3 i 4
def interpolate(x,y):
    plt.figure(figsize=(6, 4), dpi=300)

    print(x,y)

    plt.plot(x, y, 'o', markersize=10, label='Dane oryginalne')

    xx = np.arange(0, np.max(x), 0.01)
    for kind in ['linear', 'nearest', 'cubic']:
        f_interpt = scipy.interpolate.interp1d(x, y,kind=kind)
        plt.plot(xx, f_interpt(xx), label=kind)

    plt.grid(alpha=0.5, linestyle='--')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()


x = np.arange(0, 5)
y = np.arange(-1,12,3)
interpolate(x,y)

x = np.arange(0,3.1,0.5)
y = np.array([0.0,0.84,0.91,0.14,-0.76,-0.96,-0.28])
interpolate(x,y)





# %% Zadanie 5 i 6

def make_wielomian(n): # Funkcja która tworzy funkcje wielomianu stopnia n
    def f(x, *coefs):
        return sum(x**i * coefs[i] for i in range(n + 1))
    return f

fig = plt.figure(figsize=(9, 5.5), dpi=300)

def aproximetely(x,y):
    xx = np.arange(0, np.max(x), 0.01) # Warto´sci x do rysowania krzywej
    for n in range(1, len(x)):
        plt.subplot(2, 3, n)
        plt.plot(x, y, 'o', markersize=10, label='Dane oryginalne')

        wielomian = make_wielomian(n) # Tworzymy wielomian stopnia n
        p0 = np.ones(n + 1) # Pierwotnie wszystkie współczynniki to 1
        popt, _ = scipy.optimize.curve_fit(wielomian, x, y, p0) # Dobieramy optymalne współczynniki
        plt.plot(xx, wielomian(xx, *popt), label=f'Wielomian stopnia {n}') # Rysujemy krzyw ˛a

        plt.grid(alpha=0.5, linestyle='--')
        plt.legend(fontsize=8)

    plt.tight_layout()
    plt.show()


x = np.arange(0, 5)
y = np.array([1.55,4.71,5.99,9.47,13.18])
aproximetely(x,y)

x = np.arange(0,3.1,0.5)
y = np.array([1.0,0.92,0.63,-0.41,-0.94,0.27,0.89])
aproximetely(x,y)
# %% Zadanie 4