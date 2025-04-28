import numpy as np
import matplotlib.pyplot as plt

def generate(n=100, seed= None):
    np.random.seed(seed)
    x1 = 2 * np.random.rand(n) - 1
    x2 = 2 * np.random.rand(n) - 1

    a = 4 * np.random.rand() - 2
    b = 0.1 * np.random.rand() - 0.05

    y = (a*x1 + b) >= x2
    y = 2 * y -1
    return np.array([x1,x2]).T,y

X,y = generate(100,42)

plt.scatter(X[:,0],X[:,1],c=y)
# plt.show()
# print(X)
# print(y)

def perceptron_learning_rule(D,n,epochs=20):
    w = np.zeros(D[0][0].shape)
    b = 0
    E = []

    for epoch in range(epochs):
        errors = 0
        for x,y in D:
            activation = np.dot(w,x) + b
            print(activation)

            if y * activation <= 0:
                w += n * y * x
                b += n * y
                errors += 1
        E.append(errors)
    return w,b,E

D = list(zip(X,y))
perceptron_learning_rule(D,0.1)