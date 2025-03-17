from itertools import count
import numpy as np
import heapq
from collections import deque
from tabulate import tabulate
import time
import matplotlib.pyplot as plt

class Sudoku:
    def __init__(self, state):
        self.state = state
        self.next_empty = self.find_next_empty()
        self.best_empty = self.find_best_next_empty()

    def find_next_empty(self):
        empty_cells = np.where(self.state == 0)
        if empty_cells[0].size > 0:
            return (empty_cells[0][0], empty_cells[1][0])
        return None

    def find_best_next_empty(self):
        empty_cells = np.where(self.state == 0)
        if empty_cells[0].size == 0:
            return None
        min_possibilities = 10
        best_position = None
        for i, j in zip(empty_cells[0], empty_cells[1]):
            possibilities = self.check_possible_nums_at(i, j)
            if len(possibilities) < min_possibilities:
                min_possibilities = len(possibilities)
                best_position = (i, j)
        return best_position

    def __str__(self):
        return tabulate(self.state, tablefmt="fancy_grid")

    def check_possible_nums_at(self, i, j):
        # Użycie NumPy dla szybszego sprawdzania
        row = self.state[i, :]
        col = self.state[:, j]
        start_row, start_col = (i // 3) * 3, (j // 3) * 3
        square = self.state[start_row:start_row + 3, start_col:start_col + 3].flatten()
        used_nums = np.union1d(np.union1d(row, col), square)
        return np.setdiff1d(np.arange(1, 10), used_nums).tolist()

    def heuristic_1(self):
        return np.count_nonzero(self.state == 0)

    def heuristic_2(self):
        total_possibilities = 0
        empty_cells = np.where(self.state == 0)
        for i, j in zip(empty_cells[0], empty_cells[1]):
            total_possibilities += len(self.check_possible_nums_at(i, j))
        return total_possibilities

    def heuristic_3(self):
        # Heurystyka "Najmniej ograniczająca wartość"
        empty_cells = np.where(self.state == 0)
        if empty_cells[0].size == 0:
            return 0
        min_restrictions = float('inf')
        for i, j in zip(empty_cells[0], empty_cells[1]):
            possibilities = self.check_possible_nums_at(i, j)
            for num in possibilities:
                # Symulacja wstawienia liczby
                new_state = self.state.copy()
                new_state[i, j] = num
                temp_sudoku = Sudoku(new_state)
                # Liczenie ograniczeń dla sąsiadujących pustych komórek
                restrictions = 0
                for x, y in self._get_neighbors(i, j):
                    if temp_sudoku.state[x, y] == 0:
                        restrictions += len(temp_sudoku.check_possible_nums_at(x, y))
                min_restrictions = min(min_restrictions, restrictions)
        return min_restrictions if min_restrictions != float('inf') else 0

    def _get_neighbors(self, i, j):
        # Zwraca współrzędne pustych komórek w tym samym wierszu, kolumnie i kwadracie
        neighbors = set()
        empty_cells = np.where(self.state == 0)
        for x, y in zip(empty_cells[0], empty_cells[1]):
            if x == i or y == j or (x // 3 == i // 3 and y // 3 == j // 3):
                neighbors.add((x, y))
        neighbors.discard((i, j))
        return neighbors

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

        i, j = curr_sudoku.next_empty
        possibilities = curr_sudoku.check_possible_nums_at(i, j)

        new_state = curr_sudoku.state.copy()
        for num in possibilities:
            new_state[i, j] = num
            open_stack.append(Sudoku(new_state))
            open_count += 1
            new_state[i, j] = 0
    return None, len(closed_set), open_count, time.time() - start_time

def bestFS(sudoku, heuristic_func):
    start_time = time.time()
    open_count = 0
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

        if curr_sudoku.best_empty is None:
            end_time = time.time()
            return curr_sudoku.state, len(closed_set), open_count, end_time - start_time

        i, j = curr_sudoku.best_empty
        possibilities = curr_sudoku.check_possible_nums_at(i, j)

        new_state = curr_sudoku.state.copy()
        for num in possibilities:
            new_state[i, j] = num
            new_sudoku = Sudoku(new_state)
            heapq.heappush(open_pq, (heuristic_func(new_sudoku), next(counter), new_sudoku))
            open_count += 1
            new_state[i, j] = 0
    return None, len(closed_set), open_count, time.time() - start_time

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
                buffer = []
    return sudoku_dict

def main():
    # Wczytanie danych
    data = load_data("G:/Users/mateu/Pulpit/Github/STUDIA/STUDIA/py/AI/Sudoku/p096_sudoku.txt")  # Zmień ścieżkę na poprawną
    dfs_stats = {'closed': [], 'open': [], 'time': []}
    bestfs_stats_1 = {'closed': [], 'open': [], 'time': []}
    bestfs_stats_2 = {'closed': [], 'open': [], 'time': []}
    bestfs_stats_3 = {'closed': [], 'open': [], 'time': []}

    # Analiza wszystkich plansz
    for id, grid in data.items():
        sudoku = Sudoku(grid.copy())
        _, closed, open, time_taken = dfs(sudoku)
        dfs_stats['closed'].append(closed)
        dfs_stats['open'].append(open)
        dfs_stats['time'].append(time_taken)

        sudoku = Sudoku(grid.copy())
        _, closed, open, time_taken = bestFS(sudoku, Sudoku.heuristic_1)
        bestfs_stats_1['closed'].append(closed)
        bestfs_stats_1['open'].append(open)
        bestfs_stats_1['time'].append(time_taken)

        sudoku = Sudoku(grid.copy())
        _, closed, open, time_taken = bestFS(sudoku, Sudoku.heuristic_2)
        bestfs_stats_2['closed'].append(closed)
        bestfs_stats_2['open'].append(open)
        bestfs_stats_2['time'].append(time_taken)

        sudoku = Sudoku(grid.copy())
        _, closed, open, time_taken = bestFS(sudoku, Sudoku.heuristic_3)
        bestfs_stats_3['closed'].append(closed)
        bestfs_stats_3['open'].append(open)
        bestfs_stats_3['time'].append(time_taken)

    # Wyświetlanie sumarycznych statystyk
    print(f"DFS: \n -> {sum(dfs_stats['closed'])} closed \n -> {sum(dfs_stats['open'])} open \n -> {sum(dfs_stats['time']):.3f}s")
    print(f"BestFS (H1 - least empty cells): \n -> {sum(bestfs_stats_1['closed'])} closed \n -> {sum(bestfs_stats_1['open'])} open \n -> {sum(bestfs_stats_1['time']):.3f}s")
    print(f"BestFS (H2 - sum of possibilities): \n -> {sum(bestfs_stats_2['closed'])} closed \n -> {sum(bestfs_stats_2['open'])} open \n -> {sum(bestfs_stats_2['time']):.3f}s")
    print(f"BestFS (H3 - least constraining value): \n -> {sum(bestfs_stats_3['closed'])} closed \n -> {sum(bestfs_stats_3['open'])} open \n -> {sum(bestfs_stats_3['time']):.3f}s")

    # Wykresy pudełkowe
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    ax1.boxplot([dfs_stats['open'], bestfs_stats_1['open'], bestfs_stats_2['open'], bestfs_stats_3['open']],
                labels=['DFS', 'BestFS H1', 'BestFS H2', 'BestFS H3'])
    ax1.set_title('Liczba stanów w Open')
    ax2.boxplot([dfs_stats['closed'], bestfs_stats_1['closed'], bestfs_stats_2['closed'], bestfs_stats_3['closed']],
                labels=['DFS', 'BestFS H1', 'BestFS H2', 'BestFS H3'])
    ax2.set_title('Liczba stanów w Closed')
    ax3.boxplot([dfs_stats['time'], bestfs_stats_1['time'], bestfs_stats_2['time'], bestfs_stats_3['time']],
                labels=['DFS', 'BestFS H1', 'BestFS H2', 'BestFS H3'])
    ax3.set_title('Czas wykonania (s)')
    plt.tight_layout()
    plt.show()

    # Odpowiedzi na pytania
    print("\nOdpowiedzi na pytania:")
    print("1. Jak się różni liczba stanów w zbiorach Closed i Open dla badanych algorytmów?")
    print("   - DFS: Open jest mniejsze, bo stany są szybko przenoszone do Closed. Closed rośnie liniowo z eksploracją.")
    print("   - BestFS: Open może być większe, bo heurystyka utrzymuje więcej stanów do oceny, a Closed rośnie wolniej dzięki optymalizacji.")
    print("2. Co wpływa na rozmiar każdego ze zbiorów Closed i Open?")
    print("   - DFS: Open zależy od głębokości eksploracji, Closed od liczby odwiedzonych unikalnych stanów.")
    print("   - BestFS: Open zależy od heurystyki (lepsza heurystyka -> mniejsze Open), Closed od liczby stanów prowadzących do rozwiązania.")
    print("   - Trudność sudoku (liczba pustych komórek, ich rozmieszczenie) wpływa na oba zbiory.")
    print("3. Który algorytm daje najlepsze wyniki? Dlaczego?")
    print("   - BestFS z heurystyką 2 (suma możliwości) zwykle działa najlepiej, bo dobrze ocenia bliskość rozwiązania, redukując niepotrzebne eksploracje.")
    print("   - DFS jest szybki, ale nieoptymalny. H1 działa podobnie do DFS, a H3 (najmniej ograniczająca wartość) może być skuteczna w specyficznych przypadkach.")

if __name__ == "__main__":
    main()