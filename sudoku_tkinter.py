import tkinter
from random import randint, shuffle


# ----- Functions -----


def grid_layout(mW, grid_dim):
    entries = []
    row_1 = []
    row_2 = []
    row_3 = []
    row_4 = []
    row_5 = []
    row_6 = []
    row_7 = []
    row_8 = []
    row_9 = []
    for i in range(0, grid_dim ** 2):
        row = i // grid_dim
        col = i % grid_dim
        pad_y = (0, 0)
        pad_x = (0, 0)
        entry = (tkinter.Entry(mW, width=3, highlightthickness=1, highlightbackground='#000000',
                               font='cambria 12', justify='center'))
        if (row + 1) % 3 == 0 and (row + 1) < grid_dim:
            pad_y = (0, 10)
        if (col + 1) % 3 == 0 and (col + 1) < grid_dim:
            pad_x = (0, 10)

        entry.grid(row=row, column=col, padx=pad_x, pady=pad_y, ipadx=5, ipady=5)

        if row == 0:
            row_1.append(entry)
        if row == 1:
            row_2.append(entry)
        if row == 2:
            row_3.append(entry)
        if row == 3:
            row_4.append(entry)
        if row == 4:
            row_5.append(entry)
        if row == 5:
            row_6.append(entry)
        if row == 6:
            row_7.append(entry)
        if row == 7:
            row_8.append(entry)
        if row == 8:
            row_9.append(entry)

    entries.append(row_1)
    entries.append(row_2)
    entries.append(row_3)
    entries.append(row_4)
    entries.append(row_5)
    entries.append(row_6)
    entries.append(row_7)
    entries.append(row_8)
    entries.append(row_9)

    return entries


# Checks if the grid has any numbers in it
def check_grid(grid):
    for i in grid:
        for j in i:
            if not j.get():
                return False
    return True


def grid_fill(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col].get() not in numberList:
                shuffle(numberList)
                for value in numberList:
                    if value not in grid[row]:
                        if value not in (grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col],
                                         grid[5][col], grid[6][col], grid[7][col], grid[8][col]):
                            if row < 3:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(0, 3)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(0, 3)]
                                else:
                                    square = [grid[i][6:9] for i in range(0, 3)]
                            elif row < 6:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(3, 6)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(3, 6)]
                                else:
                                    square = [grid[i][6:9] for i in range(3, 6)]
                            else:
                                if col < 3:
                                    square = [grid[i][0:3] for i in range(6, 9)]
                                elif col < 6:
                                    square = [grid[i][3:6] for i in range(6, 9)]
                                else:
                                    square = [grid[i][6:9] for i in range(6, 9)]

                            if value not in (square[0] + square[1] + square[2]):
                                grid[row][col].insert(0, value)
                                if check_grid(entries):
                                    return True
                                # else:
                                #     if grid_fill(entries):
                                #         return True


# ----- Main -----
# grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0]
#         ]
mW = tkinter.Tk()
mW.title('Sudoku')
entries = grid_layout(mW, 9)
# print(entries)
numberList = list(range(1, 10))
check_grid(entries)
grid_fill(entries)
mW.mainloop()
