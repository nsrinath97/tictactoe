import tkinter as tk


# ------ Functions ------

def grid(mW):
    # create a 3x3 grid for tictactoe
    entries = []
    row_1 = []
    row_2 = []
    row_3 = []
    for i in range(0, 9):
        row = i // 3
        col = i % 3
        padx = (0, 0)
        pady = (0, 0)
        entry = tk.Entry(mW, width=4, relief='flat', highlightthickness=1, highlightbackground='#000000',
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

    return entries


def xo_buttons(mW):
    # 'X' and 'O' buttons
    button_frame = tk.Frame(mW)
    button_frame.grid(row=3, column=0, columnspan=3, padx=(22, 0))
    x_button = tk.Button(button_frame, width=4, height=1, text="X", font=('Arial', 32),
                         justify='center', relief='groove',
                         command=lambda: (set_entry_text("X", mW), x_turn(x_button, o_button)))

    o_button = tk.Button(button_frame, width=4, height=1, text="O", font=('Arial', 32),
                         justify='center', relief='groove',
                         command=lambda: (set_entry_text("O", mW), o_turn(x_button, o_button)))
    ng_button = tk.Button(button_frame, height=1, text="New Game", font=('Arial', 16),
                          justify='center', relief='groove', command=new_game())

    x_button.grid(row=0, column=0)
    o_button.grid(row=0, column=1, padx=(10, 0), pady=10)
    ng_button.grid(row=0, column=2, padx=(10,0), pady=10)


def set_entry_text(text, mW):
    # input text into the selected entry box (select by clicking into it)
    while True:
        try:
            focus_entry = mW.focus_get()
            focus_entry.insert(0, text)
            focus_entry.config(state='disabled')
            return focus_entry
        except AttributeError:
            error_frame = tk.Frame(mW)
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
    # destroy the current frame, create a new one and restore the game state to the beginning
    pass


def play():
    # start the main loop for the game (supposed to be used with function new_game to create a new grid)
    mainWindow.mainloop()

def win_conditions():
    # set the conditions for winning the game ( 8 conditions for 'X' and 'O' each)
    pass


# ------ Main ------

mainWindow = tk.Tk()
mainWindow.geometry('500x600')

tiles = grid(mainWindow)
xo_buttons(mainWindow)


if __name__ == '__main__':
    play()
