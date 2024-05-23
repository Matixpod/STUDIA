import math
import matplotlib.pyplot as plt
import numpy as np

# %% Zadanie 1 i 2

def f2(x):
    return (x - 2)**2 - 1

def złoty_podział(f, a, b, eps, max_iter):
    i=0
    k=(math.sqrt(5)-1)/2
    x = np.linspace(a, b)  
    y = f2(x)
    plt.plot(x, y, label="f(x)")
    plt.grid(True)
    plt.axvline(a,color='red', linestyle='--')
    plt.axvline(b,color='red', linestyle='--')
    while (b-a) > eps and i < max_iter:
        xl = b-(b-a)*k
        xr = a+(b-a)*k
        if f(xl) < f(xr):
            b = xr
        else:
            a = xl

        plt.axvline((xl+xr)/2,color='red', linestyle='--')
        i+=1
    plt.show()

    return (a+b)/2




złoty_podział(f2,0,5,0.000001,100)


# %% Zadanie 3
def f_prim(f,x):
    h = 10**-6
    return (f(x+h) - f(x))/h

def f_prim_2(f,x):
    h = 10**-6
    return (f_prim(f, x + h) - f_prim(f, x)) / h

def newton(f, x0, eps=10**-6, max_iter=100):
    i=0
    xk = x0
    while f_prim(f,xk) > eps or i < max_iter:
        xk_next = xk - (f_prim(f,xk))/(f_prim_2(f,xk))
        i+=1
        xk = xk_next

    return xk

newton(f2,5)


# %% Zadanie 4 i 5

def fxy(x,y):
    return 2*x**2 + y**2 + x*y - 6*x - 5*y - 8




def visualize_optimization_path(f, x0, y0, alpha, max_iter):
    path = [(x0, y0)]
    xk, yk = x0, y0
    i = 0

    while i < max_iter:
        A = [(xk, yk), (xk + alpha, yk), (xk - alpha, yk), (xk, yk + alpha), (xk, yk - alpha)]
        F = [f(xk, yk), f(xk + alpha, yk), f(xk - alpha, yk), f(xk, yk + alpha), f(xk, yk - alpha)]
        
        if (xk, yk) == A[np.argmin(F)]:
            break
        
        xk, yk = A[np.argmin(F)]
        path.append((xk, yk))
        i += 1

    path = np.array(path)
    
    x = np.linspace(path[:, 0].min() - 1, path[:, 0].max() + 1, 100)
    y = np.linspace(path[:, 1].min() - 1, path[:, 1].max() + 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    plt.figure()
    plt.contourf(X, Y, Z, levels=20, cmap='viridis')
    plt.plot(path[:, 0], path[:, 1], marker='o', color='r')
    plt.title('Optimization Path with Gradient Contour')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()



visualize_optimization_path(fxy,-3,-3,0.5,100)



