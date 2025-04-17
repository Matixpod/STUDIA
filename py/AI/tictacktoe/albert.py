import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.HUMAN = 1  # kółko
        self.COMPUTER = -1  # krzyżyk
        
    def print_board(self):
        chars = {1: 'O', -1: 'X', 0: ' '}
        for i in range(3):
            print('-------------')
            for j in range(3):
                print(f'| {chars[self.board[i][j]]} ', end='')
            print('|')
        print('-------------')
        
    def is_winner(self, player):
        # Sprawdzanie wierszy, kolumn i przekątnych
        win_states = [
            [self.board[0], self.board[1], self.board[2]],
            [self.board[:,0], self.board[:,1], self.board[:,2]],
            [self.board.diagonal(), np.fliplr(self.board).diagonal()]
        ]
        return any(all(row == player) for sets in win_states for row in sets)
    
    def is_board_full(self):
        return not any(0 in row for row in self.board)
    
    def get_empty_cells(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    cells.append((i, j))
        return cells
    
    def minimax(self, depth, is_maximizing):
        # Warunki końcowe
        if self.is_winner(self.COMPUTER):
            return 10 - depth
        if self.is_winner(self.HUMAN):
            return -10 + depth
        if self.is_board_full():
            return 0
            
        # Ruch maksymalizujący (komputer)
        if is_maximizing:
            best_score = -float('inf')
            for i, j in self.get_empty_cells():
                self.board[i][j] = self.COMPUTER
                score = self.minimax(depth + 1, False)
                self.board[i][j] = 0
                best_score = max(score, best_score)
            return best_score
            
        # Ruch minimalizujący (człowiek)
        else:
            best_score = float('inf')
            for i, j in self.get_empty_cells():
                self.board[i][j] = self.HUMAN
                score = self.minimax(depth + 1, True)
                self.board[i][j] = 0
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self):
        best_score = -float('inf')
        best_move = None
        
        for i, j in self.get_empty_cells():
            self.board[i][j] = self.COMPUTER
            score = self.minimax(0, False)
            self.board[i][j] = 0
            
            if score > best_score:
                best_score = score
                best_move = (i, j)
                
        return best_move
    
    def play_game(self, human_starts=True):
        print("Witaj w grze Kółko i Krzyżyk!")
        print("Ty grasz kółkami (O), komputer krzyżykami (X)")
        self.print_board()
        
        current_player = self.HUMAN if human_starts else self.COMPUTER
        
        while True:
            if current_player == self.HUMAN:
                while True:
                    try:
                        row = int(input("Podaj wiersz (0-2): "))
                        col = int(input("Podaj kolumnę (0-2): "))
                        if 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == 0:
                            break
                        print("Nieprawidłowy ruch, spróbuj ponownie.")
                    except ValueError:
                        print("Wprowadź liczby od 0 do 2.")
                
                self.board[row][col] = self.HUMAN
            else:
                print("Ruch komputera:")
                row, col = self.get_best_move()
                self.board[row][col] = self.COMPUTER
            
            self.print_board()
            
            if self.is_winner(current_player):
                winner = "Ty" if current_player == self.HUMAN else "Komputer"
                print(f"Koniec gry! Wygrywa {winner}!")
                break
            
            if self.is_board_full():
                print("Koniec gry! Remis!")
                break
                
            current_player = self.COMPUTER if current_player == self.HUMAN else self.HUMAN

def main():
    game = TicTacToe()
    while True:
        choice = input("Kto ma zacząć? (1 - Ty, 2 - Komputer): ")
        if choice in ['1', '2']:
            human_starts = choice == '1'
            break
        print("Nieprawidłowy wybór. Wybierz 1 lub 2.")
    
    game.play_game(human_starts)

if __name__ == "__main__":
    main()