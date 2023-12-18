# %%
from collections import deque
from collections import defaultdict


# %%

def zadanie1(filename):
    with open(filename,encoding="utf8") as file:
        data = [line.strip().split(',') for line in file]
        dict = {}
        for element1,element2 in data:
            if element1 not in dict:
                dict[element1] = [element2]
            else:
                dict[element1].append(element2)

            if element2 not in dict:
                dict[element2] = [element1]
            else:
                dict[element2].append(element1)

    return dict
    
zadanie1('..\pliki_do_zadan\small.csv')


# %%





def shortest_path_bfs(graph, start, end):
    queue = deque()
    queue.append(start)
    visited = set()
    parent = {}
    found = False

    while queue:
        node = queue.popleft()
        if node == end:
            found = True
            break
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = node

    if not found:
        return None

    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()

    return path

shortest_path_bfs(zadanie1(),'A','C')


def zadanie2(G,vs,vk):
    Q = deque([vs])
    visited = set([vs])
    P = {vs:-1}
    while Q:
        v = Q.popleft()
        if v == vk:
            break
        for u in G[v]:
            if u not in visited:
                visited.add(u)
                Q.append(u)
                P[u] = v
    if v!=vk:
        return []
    path = []
    while P[v] != -1:
        path.append(v)
        v = P[v]
    path.append(vs)
    return path[::-1]

zadanie2(zadanie1('..\pliki_do_zadan\small.csv'),'A','C')




# %%

def zadanie3(filename):
    graph = defaultdict(dict)
    with open(filename,encoding="utf8") as file:
        for line in file:
            line = line.replace(" ", "").replace("\n","").split(',')
            graph[line[0]][line[1]] = int(line[2])
            graph[line[1]][line[0]] = int(line[2])
    return graph



zadanie3('..\pliki_do_zadan\small_weighted.csv')

def zadanie4(G,vs,vk):
    Q = deque([vs])
    visited = {vs}
    P = {vs:-1}
    D = {}