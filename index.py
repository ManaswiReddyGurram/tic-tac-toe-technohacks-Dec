import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Create buttons for the game board
        self.buttons = [[tk.Button(root, text=' ', font=('normal', 20), width=6, height=3, command=lambda i=i, j=j: self.click(i, j)) for j in range(3)] for i in range(3)]

        # Place buttons on the grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            self.buttons[i][j]['text'] = self.current_player
            if self.check_winner(i, j):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            return True
        # Check diagonals
        if row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ' '
                self.board[i][j] = ' '
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()