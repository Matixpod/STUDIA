import cupy as cp

# Test: Tworzenie macierzy na GPU
try:
    a = cp.array([1, 2, 3, 4], dtype=cp.float32)
    b = cp.array([5, 6, 7, 8], dtype=cp.float32)
    print("Macierze na GPU utworzone.")
except Exception as e:
    print("Błąd podczas tworzenia macierzy:", e)

# Test: Operacja matematyczna
try:
    result = a + b
    print("Suma elementów:", result)
except Exception as e:
    print("Błąd podczas dodawania macierzy:", e)

# Test: Iloczyn skalarny
try:
    dot_product = cp.dot(a, b)
    print("Iloczyn skalarny:", dot_product)
except Exception as e:
    print("Błąd podczas obliczania iloczynu skalarnego:", e)
