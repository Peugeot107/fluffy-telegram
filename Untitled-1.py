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
        tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 14))\
            .grid(row=3, column=0, columnspan=3, sticky="nsew")

    def create_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c] = tk.Button(
                    self.root, text="", font=("Arial", 24), width=5, height=2,
                    command=lambda row=r, col=c: self.make_move(row, col)
                )
                self.buttons[r][c].grid(row=r, column=c)

    def make_move(self, row, col):
        if self.board[row][col] or self.check_winner():
            return

        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)

        if self.check_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.highlight_winner()
            self.disable_buttons()
        elif self.check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.disable_buttons()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = (
            # Rows
            [self.board[r] for r in range(3)] +
            # Columns
            [[self.board[r][c] for r in range(3)] for c in range(3)] +
            # Diagonals
            [[self.board[i][i] for i in range(3)],
             [self.board[i][2-i] for i in range(3)]]
        )
        return any(line[0] == line[1] == line[2] != "" for line in lines)

    def highlight_winner(self):
        winning_positions = []
        # Rows
        for r in range(3):
            if self.board[r][0] == self.board[r][1] == self.board[r][2] != "":
                winning_positions.extend([(r, c) for c in range(3)])
        # Columns
        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] != "":
                winning_positions.extend([(r, c) for r in range(3)])
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            winning_positions.extend([(i, i) for i in range(3)])
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            winning_positions.extend([(i, 2-i) for i in range(3)])

        for r, c in winning_positions:
            self.buttons[r][c].config(bg="lightgreen")

    def check_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def disable_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text="", bg="SystemButtonFace", state="normal")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
