import numpy as np
from tabulate import tabulate

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3,3),dtype="int8")
        self.X = 1
        self.O = -1

    def __str__(self):
        return tabulate(self.board,tablefmt="fancy_grid")
    
    def turn(self):
        count_x = np.count_nonzero(self.board == 1)
        count_o = np.count_nonzero(self.board == -1)
        return self.X if count_x >= count_o else self.O

    


ttt = TicTacToe()
print(ttt.turn())