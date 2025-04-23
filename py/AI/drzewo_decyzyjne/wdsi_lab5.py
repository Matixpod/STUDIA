from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt



X, y = load_iris(return_X_y=True)

# print(accuracy_score(y_pred,y_test))
# plot_tree(dtc, filled=True, feature_names=load_iris().feature_names, class_names=load_iris().target_names)
# plt.show()


depths = [1, 2, 3, 4, None]

for depth in depths:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=22)
    dtc = DecisionTreeClassifier(max_depth=depth)
    dtc.fit(X_train, y_train)
    y_pred = dtc.predict(X_test)
    print(f"Accuracy for depth {depth}: {accuracy_score(y_pred,y_test)}")
    

