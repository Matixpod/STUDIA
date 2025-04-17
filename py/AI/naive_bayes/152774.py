import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from typing import Tuple, Dict


# Wczytanie pliku CSV
df = pd.read_csv('spam_prepared.csv')

# Konwersja kolumn na numpy arrays
spam_labels = df['v1'].values  # automatycznie konwertuje na {0,1}
text_data = df['v2'].values

x_train, x_test, y_train, y_test = train_test_split(text_data,spam_labels,train_size=5000,random_state=42)


def extract_features(data: np.ndarray) -> Tuple[np.ndarray, Dict[str, int]]:
    """
    Funkcja ekstrahująca cechy z tekstów.
    
    Args:
        data: np.array zawierający teksty wiadomości
    
    Returns:
        Tuple zawierający:
        - macierz cech (dokumenty x słowa)
        - słownik mapujący słowa na ich indeksy
    """
    
    # (a) Utworzenie posortowanego zbioru wszystkich słów
    all_words = set()
    for text in data:
        # Rozdzielamy tekst na słowa i dodajemy do zbioru
        words = text.lower().split()
        all_words.update(words)
    
    # Sortujemy słowa
    sorted_words = sorted(list(all_words))
    
    # (b) Tworzenie słownika mapującego słowa na indeksy
    word_to_feature = {word: idx for idx, word in enumerate(sorted_words)}
    
    # (c) Tworzenie macierzy cech
    feature_matrix = np.zeros((len(data), len(word_to_feature)), dtype='int8')
    
    # (d) Wypełnianie macierzy cech
    for i, text in enumerate(data):
        words = text.lower().split()
        for word in words:
            if word in word_to_feature:  # sprawdzamy, czy słowo jest w słowniku
                j = word_to_feature[word]
                feature_matrix[i, j] = 1
    
    # (e) Zwracanie macierzy cech i słownika
    return feature_matrix, word_to_feature

# Przykład użycia:
def test_feature_extraction():
    # Przykładowe dane
    sample_data = np.array([
        "Hello world",
        "Hello Python",
        "Python world programming"
    ])
    
    # Ekstrakcja cech
    features, word_dict = extract_features(sample_data)
    
    # Wyświetlenie wyników
    print("Słownik word_to_feature:")
    print(word_dict)
    print("\nMacierz cech:")
    print(features)
    print("\nWymiary macierzy cech:", features.shape)

# test_feature_extraction()