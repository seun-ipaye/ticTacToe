import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def update_gui(row, col):
    global current_player, board
    if board[row][col] == " ":
        board[row][col] = players[current_player]
        buttons[row][col].config(text=players[current_player], state='disabled')
        if check_win(board, players[current_player]):
            messagebox.showinfo("Game Over", f"Player {players[current_player]} wins!")
            reset_board()
        elif is_board_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        else:
            current_player = (current_player + 1) % 2

def reset_board():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ", state='active')

def create_board_gui():
    global board, players, current_player, buttons
    root = tk.Tk()
    root.title("Tic Tac Toe")

    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    buttons = [[None] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                                      command=lambda row=i, col=j: update_gui(row, col))
            buttons[i][j].grid(row=i, column=j)

    reset_button = tk.Button(root, text="Reset", command=reset_board)
    reset_button.grid(row=3, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    create_board_gui()