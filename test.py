import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

class CommonPoint(object):
    def __init__(self, f, g):
        print(f'Podane funkcje: \nf(x) = {f} \ng(x) = {g}')
        self.f = lambda x: eval(f,{'x': x, 'sin': np.sin, 'cos': np.cos})
        self.g = lambda x: eval(g,{'x': x, 'sin': np.sin, 'cos': np.cos})
        self.guess = np.array([0, 0])
        self.xpoints = np.linspace(-10, 10, 1000)


    def difference(self, x):
        return self.f(x) - self.g(x)

    def intersection(self):
        return fsolve(self.difference, self.guess)

    def plot(self):
        intersection = self.intersection()
        ypoints_f = self.f(self.xpoints)
        ypoints_g = self.g(self.xpoints)
        plt.plot(self.xpoints, ypoints_f, label='f(x)')
        plt.plot(self.xpoints, ypoints_g, label='g(x)')

        if np.allclose(intersection, [0, 0], atol=1e-08):
            print("Brak punktu wspólnego dla podanych funkcji.")
        else:
            print(f'Punkt wspólny tych funkcji to: \n{intersection}')
            plt.scatter(intersection[0], self.f(intersection[0]), color='red', marker='x', label='Punkt wspólny')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid()
        plt.show()


f = input("Podaj funkcje f(x)")
g = input("Podaj funkcje g(x)")
CommonPoint(f,g).plot()