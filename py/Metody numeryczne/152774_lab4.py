import math



# %%

def f2(x):
    return (x - 2)**2 - 1

def złoty_podział(f, a, b, eps, max_iter):
    i=0
    k=(math.sqrt(5)-1)/2

    while (b-a) > eps or i < max_iter:
        xl = b-(b-a)*k
        xr = a+(b-a)*k
        if f(xl) < f(xr):
            b = xr

        else:
            plt.plot
            a = xl
        i+=1

    return (a+b)/2

złoty_podział(f2,0,5,0.000001,100)
