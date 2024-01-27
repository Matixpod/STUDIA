import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def common_point(f,g):
    def difference(x):
        # print(x)
        return eval(f) - eval(g)

    guess = np.array([0,0])
    intersection = fsolve(difference,guess)



    def evaluate(function):
        return lambda x: eval(function)
    
    f = evaluate(f)
    g = evaluate(g)


    
    xpoints = np.linspace(-10, 10, 100)
    ypoints_f = f(xpoints)
    ypoints_g = g(xpoints)
    plt.plot(xpoints, ypoints_f,label='f(x)')
    plt.plot(xpoints, ypoints_g,label='g(x)')
    plt.scatter(intersection, f(intersection), color='red', marker='x', label='Intersection')
    

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

    print(intersection)


common_point('x**2', '2*x-1')









