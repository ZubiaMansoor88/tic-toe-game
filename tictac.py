import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe Game")

board = tk.Frame(root)
board.pack()

def create_button(x, y):
    button = tk.Button(board, text=" ", width=13, height=6, command=lambda row=x, col=y: button_click(row, col))
    return button

def button_click(row, col):
    if buttons[row][col]["state"] == tk.DISABLED:
        messagebox.showinfo("Invalid Move", "This position is already selected. Choose another.")
        return
    buttons[row][col].config(bg=current_player, state=tk.DISABLED)
    check_win()
    switch_player()
    check_tie()


buttons = []

for row in range(3):
    button_row = []
    for col in range(3):
        button = create_button(row, col)
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

game_over = ""

def check_win():
    for player in [light_blue, light_pink]:
        for row in range(3):
            if all(buttons[row][col]["bg"] == player for col in range(3)):
                messagebox.showinfo("Winner!", f"Player {player} wins!")
                root.quit()
                return game_over == True
        for col in range(3):
            if all(buttons[row][col]["bg"] == player for row in range(3)):
                messagebox.showinfo("Winner!", f"Player {player} wins!")
                root.quit()
                return game_over == True
        if all(buttons[i][i]["bg"] == player for i in range(3)) or all(buttons[i][2-i]["bg"] == player for i in range(3)):
            messagebox.showinfo("Winner!", f"Player {player} wins!")
            root.quit()
            return game_over == True

def check_tie():
    if game_over == False:
        for row in range(3):
            for col in range(3):
                if buttons[row][col]["state"] != tk.DISABLED:
                    return
        messagebox.showinfo("Tie!", "It's a tie!")
        root.quit()


def switch_player():
    global current_player
    if current_player == light_blue:
        current_player = light_pink
    else:
        current_player = light_blue

light_blue = "light blue"
light_pink = "light pink"
current_player = light_blue

root.mainloop()