import numpy as np
import matplotlib.pyplot as plt

a = 2.0
b = 1.0

np.random.seed(0)
X = np.random.rand(100,1)
noise = np.random.randn(100,1) * 0.1
y = a * X + b + noise


class Perceptron:
    def __init__(self,epochs=100,lr=0.1):
        self.w = None
        self.b = 0
        self.epochs = epochs
        self.lr = lr
        
    def fit(self,X,y):
        self.w = np.zeros(X.shape[1])
        for epoch in range(self.epochs):
            y_pred = X @ self.w + self.b
            error = y.reshape(-1) - y_pred.reshape(-1)
            dw = (-1/X.shape[0]) * (X.T @ error)
            db = (-1/X.shape[0]) * np.sum(error)
            self.w = self.w - self.lr * dw
            self.b = self.b - self.lr * db
        return self.w, self.b


model = Perceptron(epochs=1000)
w,b = model.fit(X,y)
print(w)
plt.scatter(X,y)
plt.plot(X,w*X+b)
plt.show()





