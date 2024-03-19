import matplotlib.pyplot as plt
import numpy as np
import random as rng
from tabulate import tabulate


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
    # plt.figure(figsize=(8,6),dpi=300)
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
        arrow_length = 0.97 * length
        dx /= length
        dy /= length
        plt.arrow(points[a][0], points[a][1], arrow_length * dx, arrow_length * dy, head_length=2, head_width=1, color=color)

        
    plt.title('Graf skierowany')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.gca().set_axisbelow(True)
    plt.grid(True)
    # plt.figure(figsize=(8,6),dpi=300)
    plt.show()




def neighborhood_list(V,E):
    dic = {}
    for point in V:
        dic[point] = []

    for connection in E:
        dic[connection[0]].append(connection[1])
        dic[connection[1]].append(connection[0])

    return dic



def adjacency_matrix(V, E):
    V = list(V)
    E = list(E)
    matrix = [[0] * (len(V) + 1) for _ in range(len(V) + 1)]

    for i, vertex in enumerate(V, start=1):
        matrix[0][i] = vertex
        matrix[i][0] = vertex

    for edge in E:
        v1, v2 = edge

        index1 = V.index(v1) + 1
        index2 = V.index(v2) + 1

        matrix[index1][index2] = 1
        matrix[index2][index1] = 1 

    return tabulate(matrix, tablefmt='fancy_grid')


def incidence_matrix(V, E):
    V = list(V)
    E = list(E)
    matrix = [[0] * (len(E) + 1) for _ in range(len(V) + 1)]

    for i, vertex in enumerate(V):
        matrix[i + 1][0] = vertex

    for j, edge in enumerate(E):
        matrix[0][j + 1] = f"E{j} = ({edge[0]}, {edge[1]})"

    for i, edge in enumerate(E):
        v1, v2 = edge
        v1_index = V.index(v1) + 1
        v2_index = V.index(v2) + 1
        matrix[v1_index][i + 1] = 1
        matrix[v2_index][i + 1] = -1

    return tabulate(matrix, tablefmt='fancy_grid')










with open('zadania2.txt', 'r') as file:
    lines = file.readlines()

graph_number = 1
current_section = ""
V = ""
E = ""

for line in lines:
    if line.startswith('Graph'):
        print(f"\nGraph {graph_number}:")
        graph_number += 1
    else:
        current_section += line
        if line.strip().endswith('}'):
            if current_section.startswith("V"):
                V = current_section[current_section.index('{')+1:current_section.index('}')].replace("'","").replace(" ","").split(',')
                V = set(V)
            elif current_section.startswith("E"):
                E = current_section[current_section.index('{')+1:current_section.index('}')].replace("(","").replace(")","").replace("'","").replace(" ","").split(',')
                edges = set()
                for i in range(0, len(E), 2):
                    edge = (E[i].strip(), E[i+1].strip())
                    edges.add(edge)
                
            if V and E:
                print(f"V = {V}")
                print(f"E = {edges}")
                if graph_number < 12:
                    non_directional_graph(V, edges)
                elif graph_number < 22:
                    directional_graph(V, edges)
                elif  graph_number < 32:
                    print(f"Lista sąsiedztw:")
                    for key, value in neighborhood_list(V, edges).items():
                        print(f"{key}: {value}")
                elif graph_number < 42:
                    print(f"macierz sąsiedztwa")
                    print(adjacency_matrix(V, edges))
                elif graph_number < 52:
                    print(f"macierz incydencji")
                    print(incidence_matrix(V, edges))
                V = ""
                E = ""
            current_section = ""




# non_directional_graph({'v4', 'v3', 'v1', 'v2', 'v0', 'v5'}
# , {('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0',
# 'v5'), ('v3', 'v4')}
# )
# directional_graph({'v4', 'v3', 'v1', 'v2', 'v0', 'v5'}, {('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0',
# 'v5'), ('v3', 'v4')})



# for key, value in neighborhood_list({'v4', 'v3', 'v1', 'v2', 'v0', 'v5'}, {('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0',
# 'v5'), ('v3', 'v4')}).items():
#     print(key, ":", value)
            




















