import matplotlib.pyplot as plt 
import numpy as np



def knn(X,y,test_points,k=3):
    predictions = []
    for point in test_points:
        distances = euclidean_distance(X,point)
        nearest_i = np.argpartition(distances,k)[:k]
        nearest_labels = y[nearest_i]
        
        counts = np.bincount(nearest_labels)
        predictions.append(np.argmax(counts))

    return np.array(predictions)


def euclidean_distance(a,b):
    return np.sqrt(np.sum((a-b)**2,axis=1))

def accuracy(y_pred,y_true):
    return np.sum(y_pred == y_true) / len(y_true)


n_samples = 100
n_features = 2
n_classes = 3

centers = np.array([
    [2,2],
    [4,4],
    [3,8]
])

X = []
y = []

for idx, center in enumerate(centers):
    X_class = np.random.randn(n_samples,n_features) + center
    X.append(X_class)
    y.append(np.full(n_samples,idx))
    
X = np.vstack(X)
y = np.hstack(y)



indices = np.random.permutation(len(X))
X, y = X[indices], y[indices]

split_idx = int(0.8 * len(X))
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]


pred = knn(X_train,y_train,X_test,5)
print(pred)

colors = {
    0 : 'red',
    1 : 'blue',
    2 : 'green'
}

for label,color in colors.items():
    mask = (y_train == label)
    plt.scatter(X_train[mask,0],X_train[mask,1], color=color)
    mask2 = (pred == label)
    plt.scatter(X_test[mask2,0],X_test[mask2,1], color=color, marker='s',s=150, edgecolors="black")
    
print(f"{accuracy(pred,y_test):.2%}")
plt.show()






