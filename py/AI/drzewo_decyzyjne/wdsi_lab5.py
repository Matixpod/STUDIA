# Mateusz Podporski nr. albumu 152774

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


def analyze_decision_tree(X, y, feature_names=None, class_names=None, test_size=0.1, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)
    
    dt = DecisionTreeClassifier(random_state=random_state)
    dt.fit(X_train, y_train)
    
    y_train_pred = dt.predict(X_train)
    y_test_pred = dt.predict(X_test)
    acc_train = accuracy_score(y_train, y_train_pred)
    acc_test = accuracy_score(y_test, y_test_pred)
    print(f"Dokładność na zbiorze uczącym: {acc_train:.3f}")
    print(f"Dokładność na zbiorze testowym: {acc_test:.3f}")
    
    plt.figure(figsize=(12,8))
    plot_tree(dt, filled=True, feature_names=feature_names, class_names=class_names)
    plt.title("Wizualizacja drzewa decyzyjnego")
    plt.show()
    
    max_depth_obtained = dt.get_depth()
    print("Głębokość wyuczonego drzewa:", max_depth_obtained)
    
    depths = range(1, max_depth_obtained + 2)
    acc_trains, acc_tests = [], []
    for d in depths:
        clf = DecisionTreeClassifier(max_depth=d, random_state=random_state)
        clf.fit(X_train, y_train)
        acc_trains.append(accuracy_score(y_train, clf.predict(X_train)))
        acc_tests.append(accuracy_score(y_test, clf.predict(X_test)))
    
    plt.figure()
    plt.plot(depths, acc_trains, label='Train accuracy')
    plt.plot(depths, acc_tests, label='Test accuracy')
    plt.xlabel("Maksymalna głębokość drzewa")
    plt.ylabel("Dokładność")
    plt.legend()
    plt.title("Dokładność w zależności od głębokości")
    plt.show()
    
    return None
    
    
    
data = load_iris()

analyze_decision_tree(
    X = data.data,
    y = data.target,
    feature_names = data.feature_names,
    class_names = data.target_names
)
    
    
df = pd.read_csv('zoo.csv')
X_zoo = df.drop(['animal_name', 'class_type'], axis=1).values
classes = ['Mammal', 'Bird', 'Reptile', 'Fish', 'Amphibian', 'Bug', 'Invertebrate']
y_zoo = np.array([classes[i - 1] for i in df['class_type']])

analyze_decision_tree(
    X = X_zoo,
    y = y_zoo,
    feature_names = df.columns[1:-1],
    class_names = classes
)

    
    
    
    
    
    
    
    
    