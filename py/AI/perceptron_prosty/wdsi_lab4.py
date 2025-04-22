# Mateusz Podporski, nr. alb. 152774

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

def perceptron_learning_rule(D, n, max_iterations):
    w = np.zeros(D[0][0].shape)
    b = 0
    E = True
    i = 0
    k = 0

    while E and i < max_iterations:
        E = False
        for x, y in D:
            activation = np.dot(w, x) + b
            if y * activation <= 0:
                w += n * y * x
                b += n * y
                E = True
                k += 1
        i += 1
    return w,b,i,k

def main():
    data_size = [50, 100, 200]
    learning_rates = [0.001, 0.1, 1]
    fig, axs = plt.subplots(3, 3, figsize=(15, 10))

    for size in data_size:
        for rate in learning_rates:
            X, y = generate(size, seed=42)
            D = list(zip(X, y))
            w, b, epochs, errors = perceptron_learning_rule(D, rate, 1000)
            print(f"Size: {size}, Learning Rate: {rate}, Weights: {w}, Bias: {b}, epochs: {epochs}, Errors: {errors}")

            axs[data_size.index(size), learning_rates.index(rate)].scatter(X[y == 1][:, 0], X[y == 1][:, 1], c='blue', label='Klasa 1')
            axs[data_size.index(size), learning_rates.index(rate)].scatter(X[y == -1][:, 0], X[y == -1][:, 1], c='red', label='Klasa -1')
            x_range = np.linspace(-1.5, 1.5, 100)
            y_range = -(w[0]*x_range + b)/w[1] # Przekształcenie równania w1*x + w2*y + b = 0 aby liczyć y
            axs[data_size.index(size), learning_rates.index(rate)].plot(x_range, y_range, 'g-', label='Linia decyzyjna')
            axs[data_size.index(size), learning_rates.index(rate)].set_title(f'Size: {size}, Rate: {rate}, epochs: {epochs}, Errors: {errors}')
            axs[data_size.index(size), learning_rates.index(rate)].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


#* Wpływ rozmiaru zbioru uczącego:
# Wraz ze wzrostem liczby przykładów uczących (50 → 100 → 200) znacząco rośnie liczba iteracji (5 → 197 → 415)
# Większy zbiór danych wymaga więcej iteracji do osiągnięcia zbieżności
# Liczba błędów również rośnie proporcjonalnie do rozmiaru zbioru (18 → 609 → 1997)

#* Wpływ współczynnika uczenia (learning rate):
# Różne wartości learning rate (0.001, 0.1, 1) nie wpływają na liczbę iteracji ani liczbę błędów
# Learning rate wpływa głównie na wielkość wag i biasu (są proporcjonalne do learning rate)
# Dla learning rate = 0.001: wagi ~0.003
# Dla learning rate = 0.1: wagi ~0.3
# Dla learning rate = 1: wagi ~3.0