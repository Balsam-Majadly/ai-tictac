from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('3D-tic-tac-toe')
root.iconbitmap(default='error')
#root.geometry("1200x710")
#x start so true

# count = 0

count = 0
clicked = True
#
# win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6),
#             (9,10,11),(12,13,14),(15,16,17),(9,12,15),(10,13,16),(11,14,17),(9,13,17),(11,13,15),
#             (18,19,20),(21,22,23),(24,25,26),(18,21,24),(19,22,25),(20,23,26),(18,22,26),(20,22,24),
#             (0,9,18),(1,10,19),(2,11,20),(3,12,21),(4,13,23),(5,14,23),(6,15,24),(7,16,25),(8,17,26),
#             (0,10,20),(2,10,18),(2,14,26),(8,14,20),(8,16,24),(6,16,26),(6,12,18),(0,12,24),(3,13,23),
#             (5,13,21),(1,13,25),(7,13,19),(0,13,26),(2,13,24),(8,13,18),(6,13,20),(4,13,22)]


#disable buttons
def disable_all_buttons():
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9,
               c10, c11, c12, c13, c14, c15, c16, c17, c18,
               d19, d20, d21, d22, d23, d24, d25, d26, d27]

    for button in buttons:
        button.config(state=DISABLED)
#check to see if someone won

def check_if_won():
    global winner
    winner = False
    winning_combinations = [
        [b1, b2, b3], [b4, b5, b6], [b7, b8, b9],
        [c10, c11, c12], [c13, c14, c15], [c16, c17, c18],
        [d19, d20, d21], [d22, d23, d24], [d25, d26, d27],
        # Columns
        [b1, b4, b7], [b2, b5, b8], [b3, b6, b9],
        [c10, c13, c16], [c11, c14, c17], [c12, c15, c18],
        [d19, d22, d25], [d20, d23, d26], [d21, d24, d27],
        # Diagonals
        [b1, b5, b9], [b3, b5, b7],
        [c10, c14, c18], [c12, c14, c16],
        [d19, d23, d27], [d21, d23, d25],
        # Layers
        [b1, c10, d19], [b2, c11, d20], [b3, c12, d21],
        [b4, c13, d22], [b5, c14, d23], [b6, c15, d24],
        [b7, c16, d25], [b8, c17, d26], [b9, c18, d27],
        # Pillars Diagonals
        [b1, c13, d25], [b7, c13, d19], [b3, c13, d23],
        [b9, c13, c17]
    ]
    for combination in winning_combinations:
        if all(button['text'] == 'X' for button in combination):
            for button in combination:
                button.config(bg='red')
            messagebox.showinfo('3D-tic-tac-toe', 'Congratulations! X player won')

            winner = True
            disable_all_buttons()
            return
        elif all(button['text'] == 'O' for button in combination):
            for button in combination:
                button.config(bg='red')
            messagebox.showinfo('3D-tic-tac-toe', 'Congratulations! O player won')
            winner = True
            disable_all_buttons()
            return
    if count == 27 and not winner:
        messagebox.showinfo('3D-tic-tac-toe', 'It\'s a tie')
        disable_all_buttons()

#button b_click function

def b_click(b):
    global clicked, count
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False
        count += 1
        check_if_won()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        count += 1
        check_if_won()

def c_click(c):
    global clicked, count
    if c['text'] == ' ' and clicked == True:
        c['text'] = 'X'
        clicked = False
        count += 1
        check_if_won()
    elif c['text'] == ' ' and clicked == False:
        c['text'] = 'O'
        clicked = True
        count += 1
        check_if_won()

def d_click(d):
    global clicked, count
    if d['text'] == ' ' and clicked == True:
        d['text'] = 'X'
        clicked = False
        count += 1
        check_if_won()
    elif d['text'] == ' ' and clicked == False:
        d['text'] = 'O'
        clicked = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror('3D-tic-tac-toe', 'the box is already selected')

#start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, c10, c11, c12, c13, c14, c15, c16, c17, c18, d19, d20, d21, d22, d23, d24, d25, d26, d27
    global clicked, count
    clicked = True
    count = 0


#
# # Build our buttons
    b1 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b1))
    b2 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b2))
    b3 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b3))
    b4 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b4))
    b5 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b5))
    b6 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b6))
    b7 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b7))
    b8 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b8))
    b9 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b9))

    c10 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c10))
    c11 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c11))
    c12 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c12))
    c13 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c13))
    c14 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c14))
    c15 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c15))
    c16 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c16))
    c17 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c17))
    c18 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c18))

    d19 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d19))
    d20 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d20))
    d21 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d21))
    d22 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d22))
    d23 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d23))
    d24 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d24))
    d25 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d25))
    d26 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d26))
    d27 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d27))
#     button_grid = [
#         [b1, b2, b3],
#         [b4, b5, b6],
#         [b7, b8, b9],
#         [c10, c11, c12],
#         [c13, c14, c15],
#         [c16, c17, c18],
#         [d19, d20, d21],
#         [d22, d23, d24],
#         [d25, d26, d27]
#     ]
#     flag=0
#     for count in range(3):
#         # Your code block here
#         # This block will be executed three times
#         print("Running the code block")
#     for i, row in enumerate(button_grid):
#         for j, button in enumerate(row):
#             button.grid(row=i, column=j+flag)
#         flag=flag+3
#     #grid buttons to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    c10.grid(row=3, column=3)
    c11.grid(row=3, column=4)
    c12.grid(row=3, column=5)
    c13.grid(row=4, column=3)
    c14.grid(row=4, column=4)
    c15.grid(row=4, column=5)
    c16.grid(row=5, column=3)
    c17.grid(row=5, column=4)
    c18.grid(row=5, column=5)

    d19.grid(row=6, column=6)
    d20.grid(row=6, column=7)
    d21.grid(row=6, column=8)
    d22.grid(row=7, column=6)
    d23.grid(row=7, column=7)
    d24.grid(row=7, column=8)
    d25.grid(row=8, column=6)
    d26.grid(row=8, column=7)
    d27.grid(row=8, column=8)
#create menue
my_menu = Menu(root)
root.config(menu=my_menu)
#create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Reset game', command=reset)

reset()
root.mainloop()