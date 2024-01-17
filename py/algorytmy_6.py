# %%
from collections import deque
from collections import defaultdict

# %%
def zadanie1(filename):
    graf = defaultdict(list)
    with open(filename,"r") as file:
        for line in file:
            line=line.replace('"','').replace('\n','').split(',')
            graf[line[0]].append(line[1])
            graf[line[1]].append(line[0])
    return graf

graf = zadanie1(r'..\pliki_do_zadan\small.csv')
print(graf)

# %%

def zadanie2(G,vs,vk):
    Q=deque([vs])
    visited = {vs}
    P={vs:-1}
    while Q:
        v=Q.popleft()
        if v == vk:
            break
        for u in G[v]:
            if u not in visited:
                visited.add(u)
                Q.append(u)
                P[u]=v
    if v!=vk:
        return []
    path=[]
    while P[v]!=-1:
        path.append(v)
        v=P[v]
    path.append(vs)
    return path[::1]

G1=zadanie1(r'..\pliki_do_zadan\small.csv')
print(zadanie2(G1,'A','D'))
G2=zadanie1(r'..\pliki_do_zadan\city.csv')
print(zadanie2(G2,'Pomorzany','Ludowa'))

# %%

def zadanie3(filename):
    graph = defaultdict(dict)
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace(' ', '').replace('\n', '').replace('"', '').split(',')
            graph[line[0]][line[1]] = int(line[2])
            graph[line[1]][line[0]] = int(line[2])
    return graph
print(zadanie3(r'..\pliki_do_zadan\small_weighted.csv'))

# %%

def zadanie4a(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited_vertices = list(graph.keys())
    previous_vertices = {vertex: None for vertex in graph}

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])

        unvisited_vertices.remove(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex

    return previous_vertices

def zadanie4b(previous_vertices, start, end):
    path = []
    current_vertex = end
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    return path




graph_small = zadanie3(r'..\pliki_do_zadan\small_weighted.csv')
start_vertex_small = 1
end_vertex_small = 2
previous_vertices_small = zadanie4a(graph_small, 'A')
path_small = zadanie4b(previous_vertices_small, start_vertex_small, 'C')
print(f"Najkrótsza ścieżka dla grafu small_weighted.csv, startując z wierzchołka {start_vertex_small} do {end_vertex_small}:")
print(path_small)

graph_city = zadanie3(r'..\pliki_do_zadan\city_weighted.csv')
start_vertex_city = 1
end_vertex_city = 2
previous_vertices_city = zadanie4a(graph_city, 'Wawrzyniaka')
path_city = zadanie4b(previous_vertices_city, start_vertex_city, 'Pomorzany')
print(f"\nNajkrótsza ścieżka dla grafu city_weighted.csv, startując z wierzchołka {start_vertex_city} do {end_vertex_city}:")
print(path_city)
