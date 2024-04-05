# %%
import math
import matplotlib.pyplot as plt
import numpy as np
import random

def f(x):
    return x ** 3
# %% Zadanie 1 i 2

def rectangle_method(f,a,b, n):
    k = (b-a)/n
    suma = 0

    for i in range(n+1):
        suma += f(a+i*k)
        x = a+i*k
        xp = a+(i-1)*k
        plt.plot([xp,x,x,xp,xp],[0,0,f(x),f(x),0])
        

    draw_method(a,b,n)
    return suma*k


def draw_method(a,b,n):
    x = np.linspace(a, b, n)
    plt.plot(x, f(x))
    plt.show()




print(rectangle_method(f, 0, 2, 20))

# %% Zadanie 3 i 4



def trapezoidal_method(f,a,b,n):
    k = (b-a)/n
    suma = 0
    for i in range(1,n):
        suma += f(a+i*k)
        x = a+i*k
        xp = a+(i-1)*k
        plt.plot([xp,x,x,xp,xp],[0,0,f(x),f(a+(i-1)*k),0])
    draw_method(a,b,n)


    return k*(suma+(f(a)+f(b))/2)

print(trapezoidal_method(f, 0, 2, 20))




# %% Zadanie 5 i 6


def monte_carlo(f,a,b,y_max,N):
    N_traf = 0
    for i in range(N):
        x = random.uniform(a,b)
        y = random.uniform(0,y_max)
        if y < f(x):
            plt.scatter(x,y,color="green")
            N_traf += 1
        else:
            plt.scatter(x,y,color="red")

    draw_method(a,b,N)
    return (b-a) * y_max * (N_traf/N)


print(monte_carlo(f, 0, 2, 8, 1000))










