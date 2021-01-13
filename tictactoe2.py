import tkinter as tk


def grid_create(root):
    buttons = []
    game_frame = tk.Frame(root)
    game_frame.grid(row=1, column=0, padx=(100, 0), pady=(100, 0))
    for i in range(9):
        row = i // 3
        col = i % 3
        print(row, ",", col)
        btn = tk.Button(game_frame, height=5, width=10, font='Arial')
        btn.grid(row=row, column=col)
        buttons.append(btn)
        for j in buttons:
            j.config(command=lambda button=j: xo_buttons(j))
    return buttons


def xo_buttons(button):
    global bclick
    print(button)
    if button["text"] == "" and bclick is True:
        print("if")
        button.config(text="X")
        bclick = False
    elif button["text"] == "" and bclick is False:
        print("else")
        button["text"] = "0"
        bclick = True


if __name__ == "__main__":
    bclick = True
    root = tk.Tk()
    root.geometry('500x500')
    buttons = grid_create(root)
    root.mainloop()
