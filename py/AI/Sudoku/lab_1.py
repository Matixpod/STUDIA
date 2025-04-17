# Mateusz Podporski, nr. alb. 152774
# Odpowiedzi na pytania
# 1. Jak się różni liczba stanów w zbiorach Closed i Open dla badanych algorytmów?
#       DFS ma znacznie więcej stanów w obu zbiorach (Closed: 740356, Open: 741009) niż BestFS (Closed: 8047–9363, Open: 8124–10252), co wynika z przeszukiwania w głąb bez heurystyk.

# 2. Co wpływa na rozmiar każdego ze zbiorów Closed i Open?
#       Rozmiar zależy od strategii przeszukiwania: DFS generuje wiele stanów przez eksplorację w głąb, BestFS ogranicza je dzięki heurystykom (np. liczba pustych komórek, możliwości, ograniczenia).

# 3. Który algorytm daje najlepsze wyniki? Dlaczego?
#       BestFS (least numbers of empty cells) jest najlepszy (5.6817s, 8405 Closed, 8503 Open), bo heurystyka minimalizująca puste komórki skutecznie redukuje przestrzeń poszukiwań i czas.

# Wnioski:

# Algorytmy BestFS przewyższają DFS pod względem efektywności dzięki zastosowaniu heurystyk,
# które kierują przeszukiwanie w stronę rozwiązania, minimalizując liczbę analizowanych stanów i czas wykonania. DFS, choć prosty,
# jest mniej efektywny w problemach takich jak Sudoku ze względu na brak optymalizacji.
# Najlepsza heurystyka (least numbers of empty cells) łączy szybkość z niskim zużyciem zasobów, co czyni ją optymalnym wyborem.

from itertools import count
import numpy as np
import heapq
from collections import deque
from tabulate import tabulate
import time
import matplotlib.pyplot as plt
from tqdm import tqdm


grid = np.array([
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]], dtype='int8')

# print(grid[0:9,0:1])



class Sudoku:
    def __init__(self, state):
        self.state = state
        self.possibilities_cache = {}

    
    def find_next_empty(self):
        for i in range(9):
            for j in range(9):
                if self.state[i,j] == 0:
                    return (i, j)
        return None

    def find_best_empty(self):
        min_possibilities = 10
        best_position = None
        for i in range(9):
            for j in range(9):
                if self.state[i,j] != 0:
                    continue
                possibilities = self.check_possible_nums_at(i,j)
                if len(possibilities) < min_possibilities:
                    min_possibilities = len(possibilities)
                    best_position = (i,j)
        return best_position
    
    def is_solved(self):
        return self.find_next_empty() is None



    def __str__(self):
        return tabulate(self.state,tablefmt="fancy_grid")
    

    def check_col(self, j):
        return set(self.state[:, j])

    def check_row(self, i):
        return set(self.state[i, :])

    def check_square(self, i, j):
        start_row, start_col = (i // 3) * 3, (j // 3) * 3
        return set(self.state[start_row:start_row+3, start_col:start_col+3].flatten())
    
    def check_possible_nums_at(self,i,j):
        state_hash = self.state.tobytes()
        cache_key = (i, j, state_hash)

        if cache_key in self.possibilities_cache:
            return self.possibilities_cache[cache_key]
    
        used_nums = self.check_row(i) | self.check_col(j) | self.check_square(i,j)
        possibilities =  [i for i in range(1,10) if i not in used_nums]
        self.possibilities_cache[cache_key] = possibilities
        return possibilities
    


    def heuristic_1(self):
        return np.count_nonzero(self.state == 0)

    def heuristic_2(self):
        total_possibilities = 0
        for i in range(9):
            for j in range(9):
                if self.state[i, j] == 0:
                    total_possibilities += len(self.check_possible_nums_at(i,j))
        return total_possibilities
    
    def heuristic_3(self):
        pos = self.find_best_empty()
        if not pos:
            return 0
        i,j = pos
        possible_nums = self.check_possible_nums_at(i,j)
        if not possible_nums:
            return float('inf')
        
        min_constraint = float('inf')

        for v in possible_nums:
            constraint_count = 0
            for x in range(9):
                if self.state[i,x] == 0 and v in self.check_possible_nums_at(i,x) and x != j:
                    constraint_count += 1
                if self.state[x,j] == 0 and v in self.check_possible_nums_at(x,j) and x != i:
                    constraint_count += 1

            start_row, start_col = (i // 3) * 3, (j // 3) * 3
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col +3):
                    if self.state[r,c] == 0 and (r,c) != (i,j) and v in self.check_possible_nums_at(r,c):
                        constraint_count += 1
            if constraint_count < min_constraint:
                min_constraint = constraint_count
        return min_constraint
                

    

def generate_childs(sudoku, pos, possibilities):
    childs = []
    i, j = pos
    for num in possibilities:
        new_state = sudoku.state.copy()
        new_state[i, j] = num
        childs.append(Sudoku(new_state))
    return childs


def dfs(sudoku):
    start_time = time.time()
    open_count = 1
    closed_count = 0
    open_stack = deque([sudoku])
    closed_set = set()

    while open_stack:
        curr_sudoku = open_stack.pop()
        state_id = curr_sudoku.state.tobytes()

        if state_id in closed_set:
            continue

        closed_set.add(state_id)
        closed_count += 1

        if curr_sudoku.is_solved():
            # print("Rozwiązanie znalezione!")
            # print(curr_sudoku)
            return curr_sudoku.state, closed_count, open_count, time.time() - start_time
        
        pos = curr_sudoku.find_next_empty()
        possibilities = curr_sudoku.check_possible_nums_at(pos[0],pos[1])

        childs = generate_childs(curr_sudoku, pos, possibilities)
        for child in childs:
            open_stack.append(child)
            open_count += 1

    return None, closed_count, open_count, time.time() - start_time
    

def bestFS(sudoku, heuristic_func):
    start_time = time.time()
    open_count = 1
    closed_count = 0
    open_pq = []
    closed_set = set()
    counter = count()
    heapq.heappush(open_pq, (heuristic_func(sudoku), next(counter), sudoku))
    
    while open_pq:
        _, _, curr_sudoku = heapq.heappop(open_pq)
        state_id = curr_sudoku.state.tobytes()
        if state_id in closed_set:
            continue
        closed_set.add(state_id)
        closed_count += 1

        if curr_sudoku.is_solved():
            # print("Rozwiązanie znalezione!")
            # print(curr_sudoku)
            return curr_sudoku.state, closed_count, open_count, time.time() - start_time

        pos = curr_sudoku.find_best_empty()
        possibilities = curr_sudoku.check_possible_nums_at(pos[0], pos[1])

        childs = generate_childs(curr_sudoku, pos, possibilities)
        for child in childs:
            if child.is_solved():
                # print("Rozwiązanie znalezione!")
                # print(child)
                return child.state, closed_count, open_count, time.time() - start_time
            else:
                priority = heuristic_func(child)
                heapq.heappush(open_pq, (priority, next(counter), child))
                open_count += 1

    return None, closed_count, open_count, time.time() - start_time

def load_data(filename):
    sudoku_dict = {}
    with open(filename, 'r',encoding="utf-8") as f:
        current_grid = None
        buffer = []
        for line in f:
            if line.startswith("Grid"):
                current_grid = line.strip()
                buffer = []
            else:
                buffer.append(line)
            
            if len(buffer) == 9:
                sudoku_dict[current_grid] = np.array([[int(ch) for ch in row.strip()] for row in buffer], dtype='int8')
    return sudoku_dict


def main():
    data = load_data("G:/Users/mateu/Pulpit/Github/STUDIA/STUDIA/py/AI/Sudoku/p096_sudoku.txt")
    dfs_stats = {'closed': [], 'open': [], 'time': []}
    bestfs_stats_1 = {'closed': [], 'open': [], 'time': []}
    bestfs_stats_2 = {'closed': [], 'open': [], 'time': []}
    bestfs_stats_3 = {'closed': [], 'open': [], 'time': []}


    for id, grid in tqdm(data.items(), total=len(data), desc="Przetwarzanie tablic Sudoku"):
        sudoku = Sudoku(grid.copy())
        _, closed, open, time = dfs(sudoku)
        dfs_stats['closed'].append(closed)
        dfs_stats['open'].append(open)
        dfs_stats['time'].append(time)


        sudoku = Sudoku(grid.copy())
        _, closed, open, time = bestFS(sudoku,Sudoku.heuristic_1)
        bestfs_stats_1['closed'].append(closed)
        bestfs_stats_1['open'].append(open)
        bestfs_stats_1['time'].append(time)


        sudoku = Sudoku(grid.copy())
        _, closed, open, time = bestFS(sudoku,Sudoku.heuristic_2)
        bestfs_stats_2['closed'].append(closed)
        bestfs_stats_2['open'].append(open)
        bestfs_stats_2['time'].append(time)

        sudoku = Sudoku(grid.copy())
        _, closed, open, time = bestFS(sudoku,Sudoku.heuristic_3)
        bestfs_stats_3['closed'].append(closed)
        bestfs_stats_3['open'].append(open)
        bestfs_stats_3['time'].append(time)

    

    print(f"DFS: \n -> {sum(dfs_stats['closed'])} closed \n -> {sum(dfs_stats['open'])} open \n -> {sum(dfs_stats['time']):.4f}s")
    print(f"BestFS (least numbers of empty cells): \n -> {sum(bestfs_stats_1['closed'])} closed \n -> {sum(bestfs_stats_1['open'])} open \n -> {sum(bestfs_stats_1['time']):.4f}s")
    print(f"BestFS (Max possibilities): \n -> {sum(bestfs_stats_2['closed'])} closed \n -> {sum(bestfs_stats_2['open'])} open \n -> {sum(bestfs_stats_2['time']):.4f}s")
    print(f"BestFS (Least Constraing value): \n -> {sum(bestfs_stats_3['closed'])} closed \n -> {sum(bestfs_stats_3['open'])} open \n -> {sum(bestfs_stats_3['time']):.4f}s")



    algorithms = ['DFS', 'BestFS (H1)', 'BestFS (H2)', 'BestFS (H3)']
    closed_data = [dfs_stats['closed'], bestfs_stats_1['closed'], bestfs_stats_2['closed'], bestfs_stats_3['closed']]
    open_data = [dfs_stats['open'], bestfs_stats_1['open'], bestfs_stats_2['open'], bestfs_stats_3['open']]
    time_data = [dfs_stats['time'], bestfs_stats_1['time'], bestfs_stats_2['time'], bestfs_stats_3['time']]

    # Tworzenie wykresów pudełkowych
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 6))

    # Wykres dla Closed
    ax1.boxplot(closed_data, labels=algorithms)
    ax1.set_title('Liczba stanów w Closed')
    ax1.set_ylabel('Liczba stanów')
    ax1.tick_params(axis='x', rotation=45)

    # Wykres dla Open
    ax2.boxplot(open_data, labels=algorithms)
    ax2.set_title('Liczba stanów w Open')
    ax2.set_ylabel('Liczba stanów')
    ax2.tick_params(axis='x', rotation=45)

    # Wykres dla czasu wykonania
    ax3.boxplot(time_data, labels=algorithms)
    ax3.set_title('Czas wykonania (s)')
    ax3.set_ylabel('Czas (s)')
    ax3.tick_params(axis='x', rotation=45)

    # Dopasowanie układu i wyświetlenie
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
