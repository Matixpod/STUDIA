import numpy as np
import pprint as pp


class XOR:
    def __init__(self,layer_input,hidden_layers,num_nodes):
        self.network = {}
        num_node_previous =  layer_input
        
        for layer in range(hidden_layers+1):
            if layer == hidden_layers:
                layer_name = 'output'
                num_node = 1
            else:
                layer_name = f"{layer+1}_layer"
                num_node = num_nodes[layer]
                
            self.network[layer_name] = {}
            for node in range(num_node):
                node_name = f"node_{node+1}"
                self.network[layer_name][node_name] = {
                    'weights' : np.random.uniform(size=num_node_previous),
                    'bias' : np.random.uniform(size=1)
                }
                
            num_node_previous = num_node
        # pp.pprint(self.network)
        
    def fit(self,X,y,epochs=1000,lr=0.1):
        n = X.shape[0]
        
        for epoch in range(epochs):
            # forward
            layer_input = X
            for layer in self.network:
                layer_outputs= []
                self.network[layer]['layer_input'] = layer_input
                for node in self.network[layer]:
                    if node == 'layer_input': continue
                    w = self.network[layer][node]['weights']
                    b = self.network[layer][node]['bias']
                    z = layer_input @ w + b
                    a = self.sigmoid(z)
                    layer_outputs.append(a)
                    self.network[layer][node]['node_output'] = a
                layer_input = np.stack(layer_outputs, axis=1)
            
            # backward
            output = layer_input
            error = (y - output).reshape(n,)
            layers = list(self.network.keys())
            reversed_layers = layers[::-1]
            
            previous_delta = error * self.sigmoid_derivative(output.reshape(n,))  # Derivative for output layer
            # print(self.network)
            deltas = {
                'output': {'node_1' : previous_delta}
            }
            # print(deltas)
            for i in range(1,len(reversed_layers)):
                current_layer = reversed_layers[i]
                previous_layer = reversed_layers[i-1]
                deltas[current_layer] = {}
                
                for node in self.network[current_layer]:
                    if node == 'layer_input': continue
                    delta_sum = 0
                    for prev_node in self.network[previous_layer]:
                        if prev_node == 'layer_input': continue
                        weight = self.network[previous_layer][prev_node]['weights'][int(node.split('_')[1]) - 1]
                        delta_sum += deltas[previous_layer][prev_node] * weight
                    node_output = self.network[current_layer][node]['node_output']
                    delta = delta_sum * self.sigmoid_derivative(node_output)
                    deltas[current_layer][node] = delta
                    
            for layer in self.network:
                X_in = self.network[layer]['layer_input']     # (n, prev_nodes)
                for node in self.network[layer]:
                    if node == 'layer_input': continue
                    delta = deltas[layer][node]               # (n,)
                    delta = delta.reshape(-1, 1)               # <<<< zmiana: (n,1) by wymnożyć kolumnowo
                    grad_w = np.mean(X_in * delta, axis=0)    # (prev_nodes,)
                    grad_b = np.mean(deltas[layer][node])     # skalar
                    self.network[layer][node]['weights'] -= lr * grad_w
                    self.network[layer][node]['bias']    -= lr * grad_b 

    def predict(self, X):
        a = X.copy()                          # wejście (n_próbek, n_cech)
        for layer in self.network:           # iterujemy przez kolejne warstwy
            outputs = []
            for node_key in self.network[layer]:
                if not node_key.startswith('node_'):
                    continue                 # pomiń np. 'layer_input'
                w = self.network[layer][node_key]['weights']   # (poprzednie_neurony,)
                b = self.network[layer][node_key]['bias']      # (1,)
                z = a @ w + b                                   # (n_próbek,)
                outputs.append(self.sigmoid(z))
            a = np.stack(outputs, axis=1)    # (n_próbek, liczba_neuronów_w_warstwie)
        return a   


    def sigmoid(self,z):
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_derivative(self,a):
        return a * (1 - a)
    
    def compute_loss(self, y_true, y_pred):
        return np.mean((y_true - y_pred)**2)
    


X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])
model = XOR(layer_input=2, hidden_layers=1, num_nodes=[2])
model.fit(X, y, epochs=10000, lr=0.05)
print(model.predict(X))  # tu powinno być blisko [[0],[1],[1],[0]]















