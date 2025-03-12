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
        self.next_empty = self.find_best_next_empty()
        self.empty_fields = np.count_nonzero(self.state == 0)



    # def find_next_empty(self):
    #     """Znajduje indeks najbliższego pustego elementu (wiersz, kolumna)."""
    #     for row in range(9):
    #         for col in range(9):
    #             if self.state[row, col] == 0:
    #                 return [row, col]
    #     return None
    
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


    


def dfs(sudoku):
    heap = deque([sudoku])
    
    while heap:
        curr_sudoku = heap.pop()
        if curr_sudoku.next_empty is None:
            print("sudoku solved:")
            print(curr_sudoku)
            return
        i,j = curr_sudoku.next_empty
        possibilities = curr_sudoku.check_possible_nums_at(i,j)
        if possibilities:
            for num in possibilities:
                new_state = curr_sudoku.state.copy()
                new_state[i,j] = num
                heap.append(Sudoku(new_state))

def BestFS(sudoku):
    priority_queue = []
    counter = count()
    heapq.heappush(priority_queue,(sudoku.empty_fields,next(counter),sudoku))
    while priority_queue:
        _,_,curr_sudoku = heapq.heappop(priority_queue)
        if curr_sudoku.next_empty is None:
            print("sudoku solved:")
            print(curr_sudoku)
            return
        i,j = curr_sudoku.next_empty
        possibilities = curr_sudoku.check_possible_nums_at(i,j)
        if possibilities:
            for num in possibilities:
                new_state = curr_sudoku.state.copy()
                new_state[i,j] = num
                new_sudoku = Sudoku(new_state)
                heapq.heappush(priority_queue,(new_sudoku.empty_fields,next(counter),new_sudoku))



def main():
    test = Sudoku(grid)
    # print(test.empty_fields)
    # print(test)
    # print(np.where(test.state[0] == 0)[0][0])
    # print(test.next_empty)
    # print(check_col(test))
    # print(check_row(test,check_col(test)))
    # print(check_square(test))
    # print(possible_nums(test))

    start_time = time.time()
    BestFS(test)
    end_time = time.time()
    print(f"BestFS time: {end_time-start_time}s")


    start_time = time.time()
    dfs(test)
    end_time = time.time()
    print(f"DFS time: {end_time-start_time}s")





if __name__ == "__main__":
    main()
