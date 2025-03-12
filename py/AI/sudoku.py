import numpy as np
from collections import deque
from tabulate import tabulate



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
        self.next_empty = self.find_next_empty()  # Znajdź pierwsze puste pole

    def find_next_empty(self):
        """Znajduje indeks najbliższego pustego elementu (wiersz, kolumna)."""
        for row in range(9):
            for col in range(9):
                if self.state[row, col] == 0:
                    return [row, col]
        return None

    def __str__(self):
        return tabulate(self.state,tablefmt="fancy_grid")




def check_col(sudoku):
    i,j = sudoku.next_empty
    column = sudoku.state[0:9,j:j+1]
    used_numbers = set()
    for num in column:
        used_numbers.add(num[0])
    return used_numbers
                

def check_row(sudoku,used_numbers=set()):
    i,j = sudoku.next_empty
    row = sudoku.state[i:i+1,0:9]
    for num in row[0]:
        used_numbers.add(num)
    return used_numbers

def check_square(sudoku,used_numbers=set()):
    i,j = sudoku.next_empty
    squere = sudoku.state[i:i+3,j:j+3]
    print(squere)







test = Sudoku(grid)
print(test)
# print(np.where(test.state[0] == 0)[0][0])
# print(test.next_empty)
print(check_col(test))
print(check_row(test,check_col(test)))
print(check_square(test))

# print(grid[0:9,1:2])


