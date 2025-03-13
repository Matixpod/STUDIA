import numpy as np

# Ustawienie ziarna dla powtarzalności wyników
np.random.seed(123)

# Utworzenie macierzy 10x5 z losowymi liczbami całkowitymi
matrix = np.random.randint(1, 101, size=(10, 5))

# Wyświetlenie macierzy
print("Macierz:")
print(matrix)

# Obliczenie sumy głównej przekątnej macierzy za pomocą funkcji trace
sum_diagonal = np.trace(matrix)

# Wyświetlenie sumy głównej przekątnej
print(f"Suma głównej przekątnej: {sum_diagonal}")

# Wyświetlenie wartości z przekątnej za pomocą funkcji diag
diagonal_values = np.diag(matrix)

# Wyświetlenie wartości z przekątnej
print(f"Wartości z przekątnej: {diagonal_values}")