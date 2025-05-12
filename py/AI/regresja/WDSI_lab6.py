import numpy as np
import matplotlib.pyplot as plt

class LinearRegression():
    def __init__(self,xi,yi):
        self.xi = xi
        self.yi = yi
        
    def ols(self):
        self.x = self.xi.reshape(-1, 1)
        self.y = self.yi.reshape(-1, 1)
        ones = np.ones((self.x.shape[0], 1))
        self.x = np.hstack([ones, self.x])
        self.w = np.linalg.inv(self.x.T @ self.x) @ self.x.T @ self.y
        self.w = self.w.flatten()
        return self.w
    
    def mse(self):
        return np.mean((self.yi - (self.w[0] + self.w[1] * self.xi))**2)
    
    def plot_regression(self):
        plt.plot(self.xi, self.yi, 'o', label='Dane')
        plt.plot(self.xi, self.w[0] + self.w[1] * self.xi, label='Regresja liniowa', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Regresja liniowa')
        plt.legend()
        plt.grid()
        plt.show()


class NonLinearRegression:
    def __init__(self,xi,yi):
        self.xi = xi
        self.yi = yi
        
    def ols(self):
        self.x = self.xi.reshape(-1, 1)
        self.y = self.yi.reshape(-1, 1)
        ones = np.ones((self.x.shape[0], 1))
        self.x = np.hstack([ones, self.x, self.x**2])
        self.w = np.linalg.inv(self.x.T @ self.x) @ self.x.T @ self.y
        self.w = self.w.flatten()
        return self.w
    
    def mse(self):
        return np.mean((self.yi - (self.w[0] + self.w[1] * self.xi + self.w[2] * self.xi**2))**2)

    def plot_regression(self):
        plt.plot(self.xi, self.yi, 'o', label='Dane')
        plt.plot(self.xi, self.w[0] + self.w[1] * self.xi + self.w[2] * self.xi**2, label='Regresja kwadratowa', color='red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Regresja liniowa')
        plt.legend()
        plt.grid()
        plt.show()


def main():
    xi = np.array([1, 2, 3, 4, 5, 6, 7])
    yi = np.array([2.84, 5.1, 6.2, 8.95, 9.18, 12.79, 13.47])

    model = LinearRegression(xi,yi)
    w = model.ols()
    mse = model.mse()
    print(f"w0: {w[0]}, w1: {w[1]}")
    print(f"MSE: {mse}")
    model.plot_regression()

    xi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    yi = np.array([-0.05, 0.94, 0.64, -0.07, -0.52, -0.86, -0.22, 0.89, 1.11, 0.18])

    model2 = NonLinearRegression(xi,yi)
    w = model2.ols()
    mse = model2.mse()
    print(f"w0: {w[0]}, w1: {w[1]}, w2: {w[2]}")
    print(f"MSE: {mse}")
    model2.plot_regression()

if __name__ == "__main__":
    main()











