# Mateusz Podporski, nr. alb. 152774

import copy
from functools import lru_cache

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    return O if o_count < x_count else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i,row in enumerate(board):
        for j,cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise ValueError("Invalid action")
    board_copy = copy.deepcopy(board)
    row,cell = action
    current_move = player(board)
    board_copy[row][cell] = current_move
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    possible_wins = [[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                     [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
                     [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    
    for win in possible_wins:
        values = [board[i][j] for i,j in win]
        if values.count(X) == 3:
            return X
        if values.count(O) == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    return not any(EMPTY in row for row in board)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    possible_actions = {action:None for action in actions(board)}
    for action in actions(board):
        new_board = result(board, action)
        possible_actions[action] = recursion(board_to_tuple(new_board))

    if player(board) == X:
        return max(possible_actions,key=possible_actions.get)
    else:
        return min(possible_actions,key=possible_actions.get)
    

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)



@lru_cache(maxsize=None)
def recursion(tuppled_board,alpha=float('-inf'), beta=float('inf')):

    board = [list(row) for row in tuppled_board]

    if terminal(board):
        return utility(board)

    if player(board) == X:
        value = float("-inf")
        for action in actions(board):
            value = max(value,recursion(board_to_tuple(result(board, action)),alpha,beta))
            alpha = max(alpha,value)
            if beta <= alpha:
                break
    else:
        value = float("inf")
        for action in actions(board):
            value = min(value,recursion(board_to_tuple(result(board,action)),alpha,beta))
            beta = min(beta,value)
            if beta <= alpha:
                break


    return value

# print(recursion.cache_info())

# board = initial_state()
# minimax(board)