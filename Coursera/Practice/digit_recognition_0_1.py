from tensorflow.keras.datasets import mnist
import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dropout, Dense, Input
from tensorflow.keras.models import Model,Sequential, Model
from tensorflow.keras.utils import to_categorical

import platform
import numpy as np
import numpy
import tensorflow
print(platform.architecture())
print(np.__version__)
print(numpy.__version__)
print(tensorflow.__version__)

# Załaduj dane (obrazy i etykiety)
(X_train, y_train), (X_test, y_test) = mnist.load_data()

pixels = X_train.shape[1] * X_train.shape[2]
X_train = X_train.reshape(X_train.shape[0],pixels).astype('float32')
X_test = X_test.reshape(X_test.shape[0],pixels).astype('float32')
X_train = X_train / 255
X_test = X_test / 255

print(X_train[0])


y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
outputs = y_train.shape[1]

print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

input_layer = Input(shape=(pixels,))
hidden_layer_1 = Dense(64,activation='relu')(input_layer)
dropout_1 = Dropout(rate=0.3)(hidden_layer_1)
hidden_layer_2 = Dense(32,activation='relu')(dropout_1)
output_layer = Dense(outputs,activation='softmax')(hidden_layer_2)

model = Model(inputs=input_layer, outputs=output_layer)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train,y_train,epochs=10)

loss,accuracy = model.evaluate(X_test,y_test)
print(f"loss: {loss}")
print(f"accuracy: {accuracy}")



idx = 0  # dowolny indeks testowy

sample_image = X_test[idx]
sample_label = y_test[idx]

sample_image_reshaped = sample_image.reshape(1, -1)
pred = model.predict(sample_image_reshaped)
predicted_digit = np.argmax(pred)

print("Model predicts:", predicted_digit)
print("Correct answer:", np.argmax(sample_label))

plt.imshow(sample_image.reshape(28, 28), cmap='gray')
plt.title(f"Model predicts: {predicted_digit}")
plt.show()









