import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
import pprint as pp


class NeuralNetworkModel:
    def __init__(self, input_size, hidden_sizes, output_size, node_activation='relu', output_activation='softmax'):
        self.layers = []
        prev_size = input_size
        for size in hidden_sizes:
            self.layers.append({
                'W': np.random.randn(prev_size, size) * 0.01,
                'b': np.zeros((1, size)),
                'activation': node_activation
            })
            prev_size = size
        self.layers.append({
            'W': np.random.randn(prev_size, output_size) * 0.01,
            'b': np.zeros((1, output_size)),
            'activation': output_activation
        })
        
    def fit(self, X, y, epochs=1000, lr=0.1):     
        for epoch in range(epochs):
        # --- Forward ---
            A = X
            caches = []  # lista (A_prev, Z)
            for l, layer in enumerate(self.layers):
                Z = A @ layer['W'] + layer['b']
                caches.append((A, Z))  # do backwarda
                if layer['activation'] == 'relu':
                    A = self.relu(Z)
                elif layer['activation'] == 'softmax':
                    A = self.softmax(Z)
            Y_hat = A
            

        # Obliczamy gradient ("delta") funkcji kosztu względem predykcji sieci.
        # Dla softmax + crossentropy: to Y_hat - y
        dA = (Y_hat - y)

        # Przechodzimy przez wszystkie warstwy WSTECZ (od końca do początku)
        for l in reversed(range(len(self.layers))):
            # Pobieramy aktywacje i "z" z wcześniejszego forwarda 
            A_prev, Z = caches[l]
            
            # Jeśli to warstwa ukryta (ReLU, NIE ostatnia)
            if self.layers[l]['activation'] == 'relu' and l != len(self.layers) - 1:
                # Gradient przechodzi tylko tam, gdzie z>0 (Relu')
                # Reguła łańcuchowa: gradient * pochodna aktywacji
                dZ = dA * self.relu_derivative(Z)
            else:
                # Ostatnia warstwa (softmax), pochodna softmax+crossentropy = 1, więc tylko dA
                dZ = dA

            # Obliczamy gradient wag:
            # (A_prev.T @ dZ) / liczba próbek — to jest ∂Cost/∂W, uśredniony po batchu
            dW = A_prev.T @ dZ / X.shape[0]
            # Gradient biasów: suma gradientów po wszystkich próbkach, uśredniony po batchu
            db = np.sum(dZ, axis=0, keepdims=True) / X.shape[0]
            
            # Przygotowujemy dA dla kolejnej, wcześniejszej warstwy (potrzebne, jeśli będziemy iść dalej wstecz)
            if l > 0:  # Jeśli nie jesteśmy już na samym początku (brak „warstwy -1”)
                # dA = dZ @ (W.T): propagujemy gradient przez wagi do poprzednich neuronów (reguła łańcuchowa)
                dA = dZ @ self.layers[l]['W'].T
            
            # Aktualizujemy wagi i biasy w tej warstwie — krok optymalizacji gradientowej (uczymy się!)
            self.layers[l]['W'] -= lr * dW
            self.layers[l]['b'] -= lr * db

        # Dla monitoringu: co 10 epok lub na końcu wypisz aktualny błąd (loss)
        if epoch % 10 == 0 or epoch == epochs - 1:
            print(f"Epoch {epoch}, Loss: {self.cross_entropy_loss(y, Y_hat):.4f}")
                
    def predict(self, X):
        A = X
        for layer in self.layers:
            Z = A @ layer['W'] + layer['b']
            if layer['activation'] == 'relu':
                A = self.relu(Z)
            elif layer['activation'] == 'softmax':
                A = self.softmax(Z)
        return A
    
    def evaluate(self, X, y):
        predictions = self.predict(X)
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(y, axis=1)
        accuracy = np.mean(predicted_classes == true_classes)
        return accuracy


    def relu(self, x):
        return np.maximum(0, x)
    
    def relu_derivative(self, x):
        return np.where(x > 0, 1, 0)

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))  # normalizacja po próbce
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    
    def cross_entropy_loss(self, y_true, y_pred):
        return -np.sum(y_true * np.log(y_pred + 1e-15)) / y_true.shape[0]
    



(X_train, y_train), (X_test, y_test) = mnist.load_data()
pixels = X_train.shape[1] * X_train.shape[2]

X_train = X_train.reshape(X_train.shape[0], -1)
y_train = np.eye(10)[y_train]  # One-hot encoding of labels
model = NeuralNetworkModel(input_size=pixels, hidden_sizes=[128,128], output_size=10, node_activation='relu', output_activation='softmax')
model.fit(X_train, y_train, epochs=100, lr=0.01)
# model_predictions = model.predict(X_train)
accuracy = model.evaluate(X_train, y_train)
print(f"Training accuracy: {accuracy:.4f}")

# plt.imshow(X_train[0], cmap='gray')
# plt.show()































