import tkinter as tk


# ------ Functions ------
def initial_grid():
    global entries
    global row_1
    global row_2
    global row_3
    global padx
    global pady
    global row
    global col
    global entry
    entries = []
    row_1 = []
    row_2 = []
    row_3 = []
    for i in range(0, 9):
        row = i // 3
        col = i % 3
        padx = (0, 0)
        pady = (0, 0)
        entry = tk.Entry(entry_frame, width=4, relief='flat', highlightthickness=1, highlightbackground='#000000',
                         font=('Arial', 32), justify='center')
        if row == 0 and col == 0:
            pady = (100, 1)
            padx = (100, 0)
        if row == 1 and col == 0:
            pady = (0, 1)
            padx = (100, 0)
        if row == 2 and col == 0:
            pady = 0
            padx = (100, 0)

        if row == 0 and col > 0:
            pady = (100, 1)
            padx = (1, 0)
        if row == 1 and col > 0:
            pady = (0, 1)
            padx = (1, 0)
        if row == 2 and col > 0:
            pady = 0
            padx = (1, 0)

        entry.grid(row=row, column=col, ipady=23, padx=padx, pady=pady)

        if row == 0:
            row_1.append(entry)
        if row == 1:
            row_2.append(entry)
        if row == 2:
            row_3.append(entry)

        entries.append(row_1)
        entries.append(row_2)
        entries.append(row_3)


def set_entry_text(text):
    # input text into the selected entry box (select by clicking into it)
    while True:
        try:
            focus_entry = mainWindow.focus_get()
            focus_entry.insert(0, text)
            focus_entry.config(state='disabled')
            return focus_entry
        except AttributeError:
            error_frame = tk.Frame(mainWindow)
            error_frame.grid(row=4, column=0, columnspan=3, padx=(22, 0))
            error_label = tk.Label(error_frame, text='Please select a square to input a value')
            error_label.grid(row=0, column=0)
        break


def x_turn(b_1, b_2):
    # disable the 'X' button after click and enable 'O'
    b_1.config(state='disabled')
    b_2.config(state='normal')


def o_turn(b_1, b_2):
    # disable the 'O' button after click and enable 'X'
    b_1.config(state='normal')
    b_2.config(state='disabled')


def new_game():
    # destroy the current grid frame, create a new one and restore the game state to the beginning
    global entries
    global entry_frame
    entry_frame.destroy()
    entry_frame = tk.Frame(mainWindow)
    entry_frame.grid(row=0, column=0)
    initial_grid()
    o_turn(x_button, o_button)
    play()


def play():
    # start the main loop for the game (supposed to be used with function new_game to create a new grid)
    mainWindow.mainloop()


def win_conditions():
    # set the conditions for winning the game ( 8 conditions for 'X' and 'O' each)
    pass


# ------ Main ------

mainWindow = tk.Tk()
mainWindow.title("Tic Tac Toe")
mainWindow.geometry('500x600')

# create a 3x3 grid for tictactoe
entry_frame = tk.Frame(mainWindow)
entry_frame.grid(row=0, column=0)
entries = []
row_1 = []
row_2 = []
row_3 = []
for i in range(0, 9):
    row = i // 3
    col = i % 3
    padx = (0, 0)
    pady = (0, 0)
    entry = tk.Entry(entry_frame, width=4, relief='flat', highlightthickness=1, highlightbackground='#000000',
                     font=('Arial', 32), justify='center')
    if row == 0 and col == 0:
        pady = (100, 1)
        padx = (100, 0)
    if row == 1 and col == 0:
        pady = (0, 1)
        padx = (100, 0)
    if row == 2 and col == 0:
        pady = 0
        padx = (100, 0)

    if row == 0 and col > 0:
        pady = (100, 1)
        padx = (1, 0)
    if row == 1 and col > 0:
        pady = (0, 1)
        padx = (1, 0)
    if row == 2 and col > 0:
        pady = 0
        padx = (1, 0)

    entry.grid(row=row, column=col, ipady=23, padx=padx, pady=pady)

    if row == 0:
        row_1.append(entry)
    if row == 1:
        row_2.append(entry)
    if row == 2:
        row_3.append(entry)

    entries.append(row_1)
    entries.append(row_2)
    entries.append(row_3)

# 'X' and 'O' buttons
button_frame = tk.Frame(mainWindow)
button_frame.grid(row=1, column=0)
x_button = tk.Button(button_frame, width=4, height=1, text="X", font=('Arial', 32),
                     justify='center', relief='groove',
                     command=lambda: (set_entry_text("X"), x_turn(x_button, o_button)))

o_button = tk.Button(button_frame, width=4, height=1, text="O", font=('Arial', 32),
                     justify='center', relief='groove',
                     command=lambda: (set_entry_text("O"), o_turn(x_button, o_button)))
ng_button = tk.Button(button_frame, height=1, text="New Game", font=('Arial', 16),
                      justify='center', relief='groove', command=new_game)

x_button.grid(row=0, column=0)
o_button.grid(row=0, column=1, padx=(10, 0), pady=10)
ng_button.grid(row=0, column=2, padx=(10, 0), pady=10)

if __name__ == '__main__':
    play()
