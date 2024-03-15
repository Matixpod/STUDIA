import matplotlib.pyplot as plt
import numpy as np
import random as rng


def non_directional_graph(V,E):
    num_points = len(V)
    V = list(V)
    x = [rng.randint(-100,100) for _ in range(num_points)]
    y = [np.sin(i) for i in x]
    points = {}
    plt.scatter(x,y,s=50)
    for i in range(num_points):
        plt.annotate(V[i],[x[i],y[i]])
        points[V[i]] = [x[i],y[i]]


    for a,b in E:        
        plt.plot([points[a][0],points[b][0]],[points[a][1],points[b][1]])


    plt.title('Graf nieskierowany')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_axisbelow(True)
    plt.grid(True)
    plt.show()



def directional_graph(V,E):
    num_points = len(V)
    V = list(V)
    x = [rng.randint(-100,100) for _ in range(num_points)]
    y = [np.sin(i) * 10 for i in x]
    points = {

    }
    plt.scatter(x,y,s=50)
    for i in range(num_points):
        plt.annotate(V[i],[x[i]+2,y[i]])
        points[V[i]] = [x[i],y[i]]

    
    colors = [plt.cm.viridis(i/float(len(E))) for i in range(len(E))]  # Lista kolorów dla każdej strzałki
    for (a,b),color in zip(E,colors):        
        dx = points[b][0] - points[a][0]
        dy = points[b][1] - points[a][1]
        length = np.sqrt(dx ** 2 + dy ** 2)
        arrow_length = 0.94 * length
        dx /= length
        dy /= length
        plt.arrow(points[a][0], points[a][1], arrow_length * dx, arrow_length * dy, head_length=2, head_width=1, color=color)

        
    plt.title('Graf skierowany')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_axisbelow(True)
    plt.grid(True)
    plt.show()




print(non_directional_graph( {'v4', 'v3', 'v1', 'v2', 'v0', 'v5'},{('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0','v5'), ('v3', 'v4')}))
print(directional_graph( {'v4', 'v3', 'v1', 'v2', 'v0', 'v5'},{('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0','v5'), ('v3', 'v4')}))












# with open('zadania2.txt',encoding="utf8") as file:

#     for line in file:
#         # exe = line[line.index("[")+1: line.index("]")]
#         # for point in exe:

#         if line[0] == "V":                                   
#             V = line[line.index('{')+1:line.index('}')].replace("'","").replace(" ","").split(',')
#             print(set(V))
#         elif line[0] == "E":
#             print(line[line.index('{')+1:line.index('G')])

            


#         ex=[]


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graphs = []
        current_graph = {'V': set(), 'E': set()}
        for line in lines:
            if line.startswith('Graph'):
                if current_graph:
                    graphs.append(current_graph)
                current_graph = {'V': set(), 'E': set()}
            elif line.startswith('V'):
                vertices = line.split('=')[1].strip()[1:-1].split(', ')
                # Usunięcie pojedynczych cudzysłowów
                vertices = [v.strip("'") for v in vertices]
                current_graph['V'] = set(vertices)
            elif line.startswith('E'):
                edges = line.split('=')[1].strip()[1:-1].split('), ')
                edges = [tuple(e.split(', ', 1)) for e in edges if ',' in e]
                # Usunięcie pojedynczych cudzysłowów
                edges = [(a.strip("'"), b.strip("'")) for (a, b) in edges]
                current_graph['E'] = set(edges)
        if current_graph:
            graphs.append(current_graph)
    return graphs

# Przykład użycia
graphs = read_graph_from_file('zadania2.txt')
for idx, graph in enumerate(graphs, start=1):
    print(f"Graph {idx}:")
    print("V =", graph['V'])
    print("E =", graph['E'])
    print("Keys:", graph.keys())  # Dodane w celu sprawdzenia kluczy
    directional_graph(graph['V'], graph['E'])






