import numpy as np
import matplotlib.pyplot as plt


def generate(n=100, seed=None):
    np.random.seed(seed)
    x1 = 2 * np.random.rand(n) - 1
    x2 = 2 * np.random.rand(n) - 1

    a = 4 * np.random.rand() - 2
    b = 0.1 * np.random.rand() - 0.05

    y = (a * x1 + b) >= x2
    y = 2 * y - 1
    return np.array([x1, x2]).T, y


# def perceptron_learning_rule(D, n, epochs=20):
#     w = np.zeros(D[0][0].shape)
#     b = 0
#     E = []

#     for _ in range(epochs):
#         errors = 0
#         for x, y in D:
#             activation = np.dot(w, x) + b
#             if y * activation <= 0:
#                 w += n * y * x
#                 b += n * y
#                 errors += 1
#         E.append(errors)
#     return w, b, E


def perceptron_learning_rule(D, n, max_iterations):
    w = np.zeros(D[0][0].shape)
    b = 0
    E = [1]
    i = 0

    while E and i < max_iterations:
        E = []
        for x, y in D:
            activation = np.dot(w, x) + b
            if y * activation <= 0:
                w += n * y * x
                b += n * y
                E.append((x,y))
        i += 1
    print(i)
    return w,b







X, y = generate(100, seed=42)
D = list(zip(X, y))
w, b = perceptron_learning_rule(D, 0.1, 1000)
print(w,b)

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], c='blue', label='Klasa 1')
plt.scatter(X[y == -1][:, 0], X[y == -1][:, 1], c='red', label='Klasa -1')
x_range = np.linspace(-1.5, 1.5, 100)
y_range = -(w[0]*x_range + b)/w[1] # Przekształcenie równania w1*x + w2*y + b = 0 aby liczyć y
plt.plot(x_range, y_range, 'g-', label='Linia decyzyjna')
plt.show()