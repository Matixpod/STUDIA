# Mateusz Podporski, nr. alb. 152774

import numpy as np
import pandas as pd
from math import log
from collections import defaultdict
from sklearn.metrics import confusion_matrix

# Zadanie 1: Wczytanie danych
df = pd.read_csv("spam_prepared.csv")
labels = df["v1"].values.astype(int)
texts = df["v2"].values.astype(str)

# Zadanie 2: Podział danych
X_train_texts = texts[:5000]
y_train = labels[:5000]
X_test_texts = texts[5000:]
y_test = labels[5000:]

# Zadanie 3: Ekstrakcja cech
def extract_features(data):
    vocab = sorted(set(word for doc in data for word in doc.split()))
    word_to_feature = {word: idx for idx, word in enumerate(vocab)}
    X = np.zeros((len(data), len(word_to_feature)), dtype='int8')
    for i, doc in enumerate(data):
        for word in doc.split():
            if word in word_to_feature:
                j = word_to_feature[word]
                X[i, j] = 1
    return X, word_to_feature

X_train, word_to_feature = extract_features(X_train_texts)
X_test = np.zeros((len(X_test_texts), len(word_to_feature)), dtype='int8')
for i, doc in enumerate(X_test_texts):
    for word in doc.split():
        if word in word_to_feature:
            j = word_to_feature[word]
            X_test[i, j] = 1

# Zadanie 4: Trenowanie modelu NBC
def trainNB(X, y):
    logprior = {}
    loglikelyhood = {}
    Xcount = X.sum() + X.shape[1]

    for c in np.unique(y):
        X_c = X[y == c]
        logprior[c] = log(len(X_c) / len(y))
        loglikelyhood[c] = np.log((X_c.sum(axis=0) + 1) / Xcount)
    
    return logprior, loglikelyhood

logprior, loglikelyhood = trainNB(X_train, y_train)

# Zadanie 5: Predykcja
def predictNB(text, logprior, loglikelyhood, word_to_feature):
    prob_sum = {}
    for c in logprior:
        prob_sum[c] = logprior[c]
        for word in text.split():
            if word in word_to_feature:
                j = word_to_feature[word]
                prob_sum[c] += loglikelyhood[c][j]
    return max(prob_sum, key=prob_sum.get)

# Zadanie 6: Ocena dokładności
predictions = [predictNB(text, logprior, loglikelyhood, word_to_feature) for text in X_test_texts]
predictions = np.array(predictions)
accuracy = (predictions == y_test).sum() / len(y_test)
print(f"Dokładność: {accuracy * 100:.2f}%")

# Zadanie 7: Macierz konfuzji
cm = confusion_matrix(y_test, predictions)
print("Macierz konfuzji:")
print(cm)

# Komentarz do pliku:
# Macierz konfuzji:
# [[TP  FP]
#  [FN  TN]]
