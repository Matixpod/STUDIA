import numpy as np

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
            error = (y - output)
            layers = list(self.network.keys())
            reversed_layers = layers[::-1]
            
            # --- OUTPUT LAYER DELTA ---
            output_layer = reversed_layers[0]
            deltas = {}
            deltas[output_layer] = {}
            node_list = [k for k in self.network[output_layer] if k.startswith('node_')]  # <-- ZMIANA
            for i, node in enumerate(node_list):  # <-- ZMIANA
                out = self.network[output_layer][node]['node_output'].reshape(-1)
                deltas[output_layer][node] = error[:, i] * self.sigmoid_derivative(out)

            # --- HIDDEN LAYERS DELTA ---
            for l in range(1, len(reversed_layers)):
                curr_layer = reversed_layers[l]
                next_layer = reversed_layers[l-1]
                deltas[curr_layer] = {}
                curr_node_list = [k for k in self.network[curr_layer] if k.startswith('node_')]   # <-- ZMIANA
                next_node_list = [k for k in self.network[next_layer] if k.startswith('node_')]   # <-- ZMIANA
                for i, node in enumerate(curr_node_list):                                         # <-- ZMIANA
                    node_output = self.network[curr_layer][node]['node_output'].reshape(-1)
                    delta_sum = 0
                    for j, next_node in enumerate(next_node_list):                                # <-- ZMIANA
                        w = self.network[next_layer][next_node]['weights'][i]
                        d = deltas[next_layer][next_node]
                        delta_sum += w * d
                    deltas[curr_layer][node] = delta_sum * self.sigmoid_derivative(node_output)
            
            # --- UPDATE ---
            for layer in self.network:
                X_in = self.network[layer]['layer_input']
                node_list = [k for k in self.network[layer] if k.startswith('node_')]             # <-- ZMIANA
                for node in node_list:                                                           # <-- ZMIANA
                    delta = deltas[layer][node]
                    delta = delta.reshape(-1, 1)
                    grad_w = np.mean(X_in * delta, axis=0)
                    grad_b = np.mean(delta)
                    self.network[layer][node]['weights'] += lr * grad_w
                    self.network[layer][node]['bias']    += lr * grad_b

    def predict(self, X):
        a = X.copy()
        for layer in self.network:
            outputs = []
            for node_key in self.network[layer]:
                if not node_key.startswith('node_'):
                    continue
                w = self.network[layer][node_key]['weights']
                b = self.network[layer][node_key]['bias']
                z = a @ w + b
                outputs.append(self.sigmoid(z))
            a = np.stack(outputs, axis=1)
        return a   

    def sigmoid(self,z):
        return 1 / (1 + np.exp(-z))
    
    def sigmoid_derivative(self,a):
        return a * (1 - a)
    
    def compute_loss(self, y_true, y_pred):
        return np.mean((y_true - y_pred)**2)

# --- TEST ---
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])
model = XOR(layer_input=2, hidden_layers=1, num_nodes=[2])
model.fit(X, y, epochs=60000, lr=0.05)
print(model.predict(X))
