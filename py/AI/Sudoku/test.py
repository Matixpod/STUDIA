from itertools import count
import numpy as np
import heapq
from collections import deque
from tabulate import tabulate
import time

# Przykładowa siatka sudoku
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


class Sudoku:
    def __init__(self, state):
        self.state = state


    def find_next_empty(self):
        for i in range(9):
            for j in range(9):
                if self.state[i, j] == 0:
                    return (i, j)
        return None

    def find_best_empty(self):
        min_possibilities = 10
        best_position = None
        for i in range(9):
            for j in range(9):
                if self.state[i, j] != 0:
                    continue
                possibilities = self.check_possible_nums_at(i, j)
                if len(possibilities) < min_possibilities:
                    min_possibilities = len(possibilities)
                    best_position = (i, j)
        return best_position

    def __str__(self):
        return tabulate(self.state, tablefmt="fancy_grid")

    def check_col(self, j):
        return set(self.state[:, j])

    def check_row(self, i):
        return set(self.state[i, :])

    def check_square(self, i, j):
        start_row, start_col = (i // 3) * 3, (j // 3) * 3
        return set(self.state[start_row:start_row+3, start_col:start_col+3].flatten())

    def check_possible_nums_at(self, i, j):
        used_nums = self.check_row(i) | self.check_col(j) | self.check_square(i, j)
        return [num for num in range(1, 10) if num not in used_nums]

    def heuristic_1(self):
        return np.count_nonzero(self.state == 0)

    def heuristic_2(self):
        total_possibilities = 0
        for i in range(9):
            for j in range(9):
                if self.state[i, j] == 0:
                    total_possibilities += len(self.check_possible_nums_at(i, j))
        return total_possibilities

    def heuristic_3(self):
        best_value = None
        min_constraint = float('inf')

        for i in range(9):
            for j in range(9):
                if self.state[i, j] == 0:
                    possible_nums = self.check_possible_nums_at(i, j)
                    for v in possible_nums:
                        neighbors = set()
                        for col in range(9):
                            if self.state[i, col] == 0 and (i, col) != (i, j):
                                neighbors.add((i, col))
                        for row in range(9):
                            if self.state[row, j] == 0 and (row, j) != (i, j):
                                neighbors.add((row, j))
                        start_row, start_col = 3 * (i // 3), 3 * (j // 3)
                        for r in range(start_row, start_row + 3):
                            for c in range(start_col, start_col + 3):
                                if self.state[r, c] == 0 and (r, c) != (i, j):
                                    neighbors.add((r, c))

                        constraint_count = 0
                        for x, y in neighbors:
                            neighbor_possibilities = self.check_possible_nums_at(x, y)
                            if v in neighbor_possibilities:
                                constraint_count += 1
                        if constraint_count < min_constraint:
                            min_constraint = constraint_count
                            best_value = (i, j, v)
        return best_value if best_value is not None else None


def generate_childs(sudoku, pos, possibilities):
    new_state = sudoku.state.copy()
    childs = []
    i, j = pos
    for num in possibilities:
        new_state[i, j] = num
        childs.append(Sudoku(new_state))
        new_state[i, j] = 0

    return childs


def dfs(sudoku):
    start_time = time.time()
    open_count = 1
    closed_count = 0
    open_stack = deque([sudoku])
    closed_set = set()

    while open_stack:
        curr_sudoku = open_stack.pop()
        closed_count += 1
        state_id = curr_sudoku.state.tobytes()

        if state_id in closed_set:
            continue

        closed_set.add(state_id)

        if curr_sudoku.find_next_empty() is None:
            end_time = time.time()
            return curr_sudoku.state, closed_count, open_count, end_time - start_time

        pos = curr_sudoku.find_next_empty()
        possibilities = curr_sudoku.check_possible_nums_at(pos[0], pos[1])

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
        closed_count += 1

        state_id = curr_sudoku.state.tobytes()
        if state_id in closed_set:
            continue
        closed_set.add(state_id)

        if curr_sudoku.find_best_empty() is None:
            end_time = time.time()
            return curr_sudoku.state, closed_count, open_count, end_time - start_time

        pos = curr_sudoku.find_best_empty()
        possibilities = curr_sudoku.check_possible_nums_at(pos[0], pos[1])

        childs = generate_childs(curr_sudoku, pos, possibilities)
        for child in childs:
            heapq.heappush(open_pq, (heuristic_func(child), next(counter), child))
            open_count += 1

    return None, closed_count, open_count, time.time() - start_time


def load_data(filename):
    sudoku_dict = {}
    with open(filename, 'r', encoding="utf-8") as f:
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
    # Jeśli masz plik z danymi, odkomentuj poniższą linijkę i ustaw poprawną ścieżkę
    data = load_data("G:/Users/mateu/Pulpit/Github/STUDIA/STUDIA/py/AI/Sudoku/p096_sudoku.txt")
    # Dla celów testowych wykonamy jeden przypadek – przykładową planszę
    # data = {"Przykład": grid.copy()}

    dfs_stats = {'open': [], 'closed': [], 'time': []}
    bestfs_stats_1 = {'open': [], 'closed': [], 'time': []}
    bestfs_stats_2 = {'open': [], 'closed': [], 'time': []}
    bestfs_stats_3 = {'open': [], 'closed': [], 'time': []}

    for id, grid_instance in data.items():
        sudoku = Sudoku(grid_instance.copy())
        _, open, closed, elapsed_time = dfs(sudoku)
        dfs_stats['open'].append(open)
        dfs_stats['closed'].append(closed)
        dfs_stats['time'].append(elapsed_time)

        sudoku = Sudoku(grid_instance.copy())
        _, open, closed, elapsed_time = bestFS(sudoku, Sudoku.heuristic_1)
        bestfs_stats_1['open'].append(open)
        bestfs_stats_1['closed'].append(closed)
        bestfs_stats_1['time'].append(elapsed_time)

        sudoku = Sudoku(grid_instance.copy())
        _, open, closed, elapsed_time = bestFS(sudoku, Sudoku.heuristic_2)
        bestfs_stats_2['open'].append(open)
        bestfs_stats_2['closed'].append(closed)
        bestfs_stats_2['time'].append(elapsed_time)

        sudoku = Sudoku(grid_instance.copy())
        _, open, closed, elapsed_time = bestFS(sudoku, Sudoku.heuristic_3)
        bestfs_stats_3['open'].append(open)
        bestfs_stats_3['closed'].append(closed)
        bestfs_stats_3['time'].append(elapsed_time)

    print("DFS: ")
    print(f" -> {sum(dfs_stats['open'])} open")
    print(f" -> {sum(dfs_stats['closed'])} closed")
    print(f" -> {sum(dfs_stats['time']):.3f}s\n")

    print("BestFS (least numbers of empty cells):")
    print(f" -> {sum(bestfs_stats_1['open'])} open")
    print(f" -> {sum(bestfs_stats_1['closed'])} closed")
    print(f" -> {sum(bestfs_stats_1['time']):.3f}s\n")

    print("BestFS (max possibilities):")
    print(f" -> {sum(bestfs_stats_2['open'])} open")
    print(f" -> {sum(bestfs_stats_2['closed'])} closed")
    print(f" -> {sum(bestfs_stats_2['time']):.3f}s\n")

    print("BestFS (least constraining value):")
    print(f" -> {sum(bestfs_stats_3['open'])} open")
    print(f" -> {sum(bestfs_stats_3['closed'])} closed")
    print(f" -> {sum(bestfs_stats_3['time']):.3f}s")


if __name__ == "__main__":
    main()