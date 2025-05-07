import numpy as np
import matplotlib.pyplot as plt

xi = np.array([1, 2, 3, 4, 5, 6, 7])
yi = np.array([2.84, 5.1, 6.2, 8.95, 9.18, 12.79, 13.47])

x = xi.reshape(-1, 1)
y = yi.reshape(-1, 1)
ones = np.ones((x.shape[0], 1))
x = np.hstack([ones, x]) 

w = np.linalg.inv(x.T @ x) @ x.T @ y
w = w.flatten()

mse = np.mean((yi - (w[0] + w[1] * xi))**2)


print(f"w0: {w[0]}, w1: {w[1]}")
print(f"MSE: {mse}")
plt.plot(xi, yi, 'o', label='Dane')
plt.plot(xi, w[0] + w[1] * xi, label='Regresja liniowa', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresja liniowa')
plt.legend()
plt.grid()
plt.show()


xi = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yi = np.array([-0.05, 0.94, 0.64, -0.07, -0.52, -0.86, -0.22, 0.89, 1.11, 0.18])

x = xi.reshape(-1, 1)
y = yi.reshape(-1, 1)
ones = np.ones((x.shape[0], 1))
x = np.hstack([ones, x, x**2])

w = np.linalg.inv(x.T @ x) @ x.T @ y
w = w.flatten()

mse = np.mean((yi - (w[0] + w[1] * xi + w[2] * xi**2))**2)

print(f"w0: {w[0]}, w1: {w[1]}, w2: {w[2]}")
print(f"MSE: {mse}")
plt.plot(xi, yi, 'o', label='Dane')
plt.plot(xi, w[0] + w[1] * xi + w[2] * xi**2, label='Regresja kwadratowa', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresja kwadratowa')
plt.legend()
plt.grid()
plt.show()















