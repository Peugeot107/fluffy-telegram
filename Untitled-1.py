import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 14))
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def create_board(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                command=lambda r=row, c=col: self.make_move(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.highlight_winner()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def highlight_winner(self):
        # Highlight winning cells
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                for col in range(3):
                    self.buttons[row][col].config(bg="lightgreen")
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                for row in range(3):
                    self.buttons[row][col].config(bg="lightgreen")
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            for i in range(3):
                self.buttons[i][i].config(bg="lightgreen")
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            for i in range(3):
                self.buttons[i][2-i].config(bg="lightgreen")

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", bg="SystemButtonFace")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
