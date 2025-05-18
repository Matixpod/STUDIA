# Mateusz Podporski, nr. alb. 152774
# Wnioski
# Najlepszy stopień: 4 lub 5 (oba dają identyczne, MSE: 0.0112).
# Overfitting zaczyna się: od stopnia 6, gdzie MSE zaczyna rosnąć.

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


class PolynominalRegression:
    def __init__(self,xi,yi,degree):
        self.xi = xi
        self.yi = yi
        self.degree = degree
        
    def ols(self):
        self.x = np.vander(self.xi,self.degree + 1, increasing=True)
        self.y = self.yi.reshape(-1, 1)
        self.w = np.linalg.inv(self.x.T @ self.x) @ self.x.T @ self.y
        self.w = self.w.flatten()
        return self.w
    
    def predict(self, x):
        X = np.vander(x, self.degree + 1, increasing=True)
        return X @ self.w

    def mse(self):
        y_pred = self.predict(self.xi)
        return np.mean((self.yi - y_pred) ** 2)


    def plot_regression(self, x_plot):
        y_plot = self.predict(x_plot)
        plt.plot(x_plot, y_plot, label=f'stopien {self.degree}, MSE={self.mse():.4f}')


def main():
    xi = np.array([1, 2, 3, 4, 5, 6, 7])
    yi = np.array([2.84, 5.1, 6.2, 8.95, 9.18, 12.79, 13.47])

    model = LinearRegression(xi,yi)
    w = model.ols()
    mse = model.mse()
    print(f"w0: {w[0]:.4f}, w1: {w[1]}:.4f")
    print(f"MSE: {mse:.4f}")
    model.plot_regression()

    xi = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    yi = np.array([-0.05, 0.94, 0.64, -0.07, -0.52, -0.86, -0.22, 0.89, 1.11, 0.18])
    x_plot = np.linspace(0,9,200)
    plt.figure(figsize=(10,6))
    plt.plot(xi,yi,'o',label='Dane')
    mse_list = []
    
    for degree in range(1,len(xi)):
        model = PolynominalRegression(xi,yi,degree)
        model.ols()
        mse = model.mse()
        mse_list.append(mse)
        model.plot_regression(x_plot)
        print(f"Stopien: {degree}, MSE: {mse:.4f}")
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresja wielomianowa')
    plt.legend()
    plt.grid()
    plt.show()
    

if __name__ == "__main__":
    main()










