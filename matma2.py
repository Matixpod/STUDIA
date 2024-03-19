import matplotlib.pyplot as plt
import numpy as np
import random as rng


def non_directional_graph(V,E):
    num_points = len(V)
    V = list(V)
    x = [rng.randint(-100,100) for _ in range(num_points)]
    y = [np.sin(i) for i in x]
    points = {}
    plt.scatter(x,y)
    for i in range(num_points):
        plt.annotate(V[i],[x[i],y[i]])
        points[V[i]] = [x[i],y[i]]


    for a,b in E:        
        plt.plot([points[a][0],points[b][0]],[points[a][1],points[b][1]])

    plt.figure(figsize=(4,3),dpi=3000)
    plt.show()



def directional_graph(V,E):
    num_points = len(V)
    V = list(V)
    x = [rng.randint(-100,100) for _ in range(num_points)]
    y = [np.sin(i) * 10 for i in x]
    points = {

    }
    plt.scatter(x,y)
    for i in range(num_points):
        plt.annotate(V[i],[x[i],y[i]])
        points[V[i]] = [x[i],y[i]]


    for a,b in E:        
        plt.arrow(points[a][0], points[a][1], points[b][0] - points[a][0], points[b][1] - points[a][1],
              head_width=1, length_includes_head=True)
    plt.figure(figsize=(10,10),dpi=100)
    plt.show()












print(directional_graph( {'v4', 'v3', 'v1', 'v2', 'v0', 'v5'},{('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0','v5'), ('v3', 'v4')}))
print(non_directional_graph( {'v4', 'v3', 'v1', 'v2', 'v0', 'v5'},{('v4', 'v5'), ('v1', 'v4'), ('v1', 'v2'), ('v2', 'v4'), ('v0','v5'), ('v3', 'v4')}))




























# with open('zadania2.txt',encoding="utf8") as file:
#     ex = []
#     for line in file:
#         exe = line[line.index("[")+1: line.index("]")]
#         for num in exe:
#             ex.append(int(num))


#         ex=[]

