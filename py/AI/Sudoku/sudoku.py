from itertools import count
import numpy as np
import heapq
from collections import deque
from tabulate import tabulate
import time
import matplotlib.pyplot as plt


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
        self.next_empty = self.find_next_empty()
        self.best_empty = self.find_best_next_empty()

    
    def find_next_empty(self):
        for i in range(9):
            for j in range(9):
                if self.state[i,j] == 0:
                    return (i, j)
        return None

    def find_best_next_empty(self):
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
        used_nums = self.check_row(i) | self.check_col(j) | self.check_square(i,j)
        return [i for i in range(1,10) if i not in used_nums]
    


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
        min_possibilities = float('inf') 
        for i in range(9):
            for j in range(9):
                if self.state[i, j] == 0:
                    possibilities = len(self.check_possible_nums_at(i, j))
                    min_possibilities = min(min_possibilities, possibilities)
        return min_possibilities if min_possibilities != float('inf') else 0



    


def dfs(sudoku):
    start_time = time.time()
    open_count = 0
    open_stack = deque([sudoku])
    closed_set = set()
    while open_stack:
        curr_sudoku = open_stack.pop()
        state_id = curr_sudoku.state.tobytes()
        if state_id in closed_set:
            continue
        closed_set.add(state_id)
        if curr_sudoku.next_empty is None:
            end_time = time.time()
            return curr_sudoku.state, len(closed_set), open_count, end_time - start_time

        i,j = curr_sudoku.next_empty
        possibilities = curr_sudoku.check_possible_nums_at(i,j)

        new_state = curr_sudoku.state.copy()
        for num in possibilities:
            new_state[i,j] = num
            open_stack.append(Sudoku(new_state))
            open_count += 1
            new_state[i,j] = 0
    return None, len(closed_set), open_count, time.time() - start_time
    

def bestFS(sudoku,heuristic_func):
    start_time = time.time()
    open_count = 0
    open_pq = []
    closed_set = set()
    counter = count()
    heapq.heappush(open_pq,(heuristic_func(sudoku),next(counter),sudoku))
    while open_pq:
        _,_,curr_sudoku = heapq.heappop(open_pq)
        state_id = curr_sudoku.state.tobytes()
        if state_id in closed_set:
            continue
        closed_set.add(state_id)

        if curr_sudoku.best_empty is None:
            end_time = time.time()
            return curr_sudoku.state, len(closed_set), open_count, end_time - start_time

        i,j = curr_sudoku.best_empty
        possibilities = curr_sudoku.check_possible_nums_at(i,j)

        new_state = curr_sudoku.state.copy()
        for num in possibilities:
            new_state[i,j] = num
            new_sudoku = Sudoku(new_state)
            heapq.heappush(open_pq,(heuristic_func(new_sudoku),next(counter),new_sudoku))
            open_count += 1
            new_state[i,j] = 0

    return None, len(closed_set), open_count, time.time() - start_time



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


    for id,grid in data.items():
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

    

    print(f"DFS: \n -> {sum(dfs_stats['closed'])} closed \n -> {sum(dfs_stats['open'])} open \n -> {sum(dfs_stats['time']):.3f}s")
    print(f"BestFS (least numbers of empty cells): \n -> {sum(bestfs_stats_1['closed'])} closed \n -> {sum(bestfs_stats_1['open'])} open \n -> {sum(bestfs_stats_1['time']):.3f}s")
    print(f"BestFS (Max possibilities): \n -> {sum(bestfs_stats_2['closed'])} closed \n -> {sum(bestfs_stats_2['open'])} open \n -> {sum(bestfs_stats_2['time']):.3f}s")
    print(f"BestFS (Least possibilities): \n -> {sum(bestfs_stats_3['closed'])} closed \n -> {sum(bestfs_stats_3['open'])} open \n -> {sum(bestfs_stats_3['time']):.3f}s")



if __name__ == "__main__":
    main()
