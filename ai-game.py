import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import random

first_player_score=0
second_player_score=0
root = Tk()
root.title('3D-tic-tac-toe')
root.iconbitmap(default='error')
#root.geometry("1200x710")
#x start so true
clicked = True
count = 0
board3d=[]
def init_board():
    for x in range(0, 27):
        board3d.append(x)
def reset_board():
    for x in range(0, 27):
        board3d[x]=x
def isMovesLeft(board):
    for x in range(0, 27):
            if (board[x] == x):
                return True
    return False
def disable_all_buttons():
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9,
               c10, c11, c12, c13, c14, c15, c16, c17, c18,
               d19, d20, d21, d22, d23, d24, d25, d26, d27]

    for button in buttons:
        button.config(state=DISABLED)
# def ai_move(board):
#     ai_move_index = findBestMove(board)
#     buttons[ai_move_index].config(text='O', state=DISABLED)
#     board3d[ai_move_index]='O'
#     check_if_won()

def ai_move(board):
    alpha = -100000000
    beta = 100000000
    ai_move_index = findBestMove(board, alpha, beta)
    buttons[ai_move_index].config(text='O', state=DISABLED)
    board3d[ai_move_index] = 'O'
    check_if_won()


def evaluate(board):
    combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [9, 10, 11], [12, 13, 14], [15, 16, 17],
    [18, 19, 20], [21, 22, 23], [24, 25, 26],
    # Columns
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [9, 12, 15], [10, 13, 16], [11, 14, 17],
    [18, 21, 24], [19, 22, 25], [20, 23, 26],
    # Diagonals
    [0, 4, 8], [2, 4, 6],
    [9, 13, 17], [11, 13, 15],
    [18, 22, 26], [20, 22, 24],
    # Layers
    [0, 9, 18], [1, 10, 19], [2, 11, 20],
    [3, 12, 21], [4, 13, 22], [5, 14, 23],
    [6, 15, 24], [7, 16, 25], [8, 17, 26],
    # Pillars Diagonals
    [0, 12, 24], [6, 12, 18], [2, 12, 22],
    [8, 12, 16]
]
    for combination in combinations:
        if all(board[index] == 'X' for index in combination):
            return -10
        if all(board[index] == 'O' for index in combination):
            return 10

    # Else if none of them have won then return 0
    return 0

# def minimax(board, depth, isMax):
#     score = evaluate(board)
#
#     # If Maximizer has won the game return his/her
#     # evaluated score
#     if (score == 10):
#         return score
#
#     # If Minimizer has won the game return his/her
#     # evaluated score
#     if (score == -10):
#         return score
#
#     # If there are no more moves and no winner then
#     # it is a tie
#     if (isMovesLeft(board) == False):
#         return 0
#
#     # If this maximizer's move
#     if (isMax):
#         best = -100000000
#
#         # Traverse all cells
#         for x in range(0, 27):
#
#                 # Check if cell is empty
#                 if (board[x] == x):
#                     # Make the move
#                     board[x] = 'O'
#
#                     # Call minimax recursively and choose
#                     # the maximum value
#                     best = max(best, minimax(board,
#                                              depth + 1,
#                                              not isMax))
#
#                     # Undo the move
#                     board[x] = x
#         return best
#
#     # If this minimizer's move
#     else:
#         best = 1000000
#
#         # Traverse all cells
#         for x in range(0, 27):
#
#                 # Check if cell is empty
#                 if (board[x] == x):
#                     # Make the move
#                     board[x] = 'X'
#
#                     # Call minimax recursively and choose
#                     # the minimum value
#
#                     best = min(best, minimax(board, depth + 1, not isMax))
#
#                     # Undo the move
#                     board[x] = x
#         return best



def minimax(board, depth, isMax, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score
    if score == -10:
        return score
    if not isMovesLeft(board):
        return 0

    if isMax:
        best = -100000000
        for x in range(0, 27):
            if board[x] == x:
                board[x] = 'O'
                best = max(best, minimax(board, depth + 1, not isMax, alpha, beta))
                alpha = max(alpha, best)
                board[x] = x

                if beta <= alpha:
                    break
        return best
    else:
        best = 100000000
        for x in range(0, 27):
            if board[x] == x:
                board[x] = 'X'
                best = min(best, minimax(board, depth + 1, not isMax, alpha, beta))
                beta = min(beta, best)
                board[x] = x

                if beta <= alpha:
                    break
        return best


# def findBestMove(board):
#     bestVal = -1000000000
#     bestMove = -1
#
#     # Traverse all cells, evaluate minimax function for
#     # all empty cells. And return the cell with optimal
#     # value.
#     for  x in range(0, 27):
#
#             # Check if cell is empty
#             if (board[x] == x):
#
#                 # Make the move
#                 board[x] = 'O'
#
#                 # compute evaluation function for this
#                 # move.
#                 moveVal = minimax(board, 0, False)
#
#                 # Undo the move
#                 board[x] = x
#
#                 # If the value of the current move is
#                 # more than the best value, then update
#                 # best/
#                 if (moveVal > bestVal):
#                     bestMove = x
#                     bestVal = moveVal
#
#     print("The value of the best Move is :", bestVal)
#     print()
#     return bestMove


def findBestMove(board, alpha, beta):
    bestVal = -1000000000
    bestMove = -1

    for x in range(0, 27):
        if board[x] == x:
            board[x] = 'O'
            moveVal = minimax(board, 0, False, alpha, beta)
            board[x] = x

            if moveVal > bestVal:
                bestMove = x
                bestVal = moveVal

            if moveVal >= beta:
                return bestMove

            alpha = max(alpha, moveVal)
    return bestMove

#check to see if someone won
def check_if_won():
    global winner
    global second_player_score
    global first_player_score
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

            first_player_score+=1
            messagebox.showinfo('3D-tic-tac-toe', 'Congratulations! '+first_player+ ' won')
            messagebox.showinfo('3D-tic-tac-toe', second_player + ' score is: ' + str(second_player_score) + " " +first_player + ' score is: ' + str(first_player_score))


            winner = True
            disable_all_buttons()
            reset_board()
            return
        elif all(button['text'] == 'O' for button in combination):
            for button in combination:
                button.config(bg='red')

            second_player_score += 1
            messagebox.showinfo('3D-tic-tac-toe', 'Congratulations! '+second_player+ ' won')
            messagebox.showinfo('3D-tic-tac-toe', second_player + ' score is: ' + str(second_player_score)  +" " + first_player + ' score is: ' + str(first_player_score))


            winner = True
            disable_all_buttons()
            reset_board()
            return
    if count == 27 and not winner:
        messagebox.showinfo('3D-tic-tac-toe', 'It\'s a tie')
        disable_all_buttons()
        reset_board()
#button b_click function

def b_click(b,num):
    global clicked, count,board3d
    print(board3d)
   # print(num)
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        board3d[num] = 'X'

        print(board3d)
        clicked = False
        count += 1
        check_if_won()
        board=board3d
        ai_move(board)

def c_click(c,num):
    global clicked, count,board3d
    print(board3d)
    if c['text'] == ' ' and clicked == True:
        c['text'] = 'X'
        board3d[num] = 'X'
        clicked = False
        count += 1
        check_if_won()
        board=board3d

        ai_move(board)

def d_click(d,num):
    global clicked, count,board3d
    print(board3d)

    if d['text'] == ' ' and clicked == True:
        d['text'] = 'X'
        clicked = False
        board3d[num]= 'X'
        count += 1
        check_if_won()
        board=board3d

        ai_move(board)

def choose_players(first_player,second_player):
    # first_player = input("Enter the First Player Name: ")
    # second_player = input("Enter the Second Player Name: ")

    players = [first_player, second_player]
    random.shuffle(players)

    first_player, second_player = players

    first_player_token = random.choice(['X', 'O'])
    second_player_token = 'X' if first_player_token == 'O' else 'O'

    print(f"{first_player} will play as {first_player_token}")
    print(f"{second_player} will play as {second_player_token}")

    return first_player, second_player, first_player_token, second_player_token



#start the game over
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, c10, c11, c12, c13, c14, c15, c16, c17, c18, d19, d20, d21, d22, d23, d24, d25, d26, d27
    global clicked, count
    clicked = True
    count = 0

# Build our buttons
    b1 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b1,0))
    b2 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b2,1))
    b3 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b3,2))
    b4 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b4,3))
    b5 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b5,4))
    b6 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b6,5))
    b7 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b7,6))
    b8 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b8,7))
    b9 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: b_click(b9,8))

    c10 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c10,9))
    c11 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c11,10))
    c12 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c12,11))
    c13 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c13,12))
    c14 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c14,13))
    c15 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c15,14))
    c16 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c16,14))
    c17 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c17,16))
    c18 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: c_click(c18,17))

    d19 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d19,18))
    d20 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d20,19))
    d21 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d21,20))
    d22 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d22,21))
    d23 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d23,22))
    d24 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d24,23))
    d25 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d25,24))
    d26 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d26,25))
    d27 = Button(root, text=' ', font=('Helvetica', 12), height=1, width=3, bg='SystemButtonFace', command=lambda: d_click(d27,26))

    #grid buttons to the screen
    b1.grid(row=2, column=1)
    b2.grid(row=2, column=2)
    b3.grid(row=2, column=3)
    b4.grid(row=3, column=1)
    b5.grid(row=3, column=2)
    b6.grid(row=3, column=3)
    b7.grid(row=4, column=1)
    b8.grid(row=4, column=2)
    b9.grid(row=4, column=3)

    c10.grid(row=5, column=4)
    c11.grid(row=5, column=5)
    c12.grid(row=5, column=6)
    c13.grid(row=6, column=4)
    c14.grid(row=6, column=5)
    c15.grid(row=6, column=6)
    c16.grid(row=7, column=4)
    c17.grid(row=7, column=5)
    c18.grid(row=7, column=6)

    d19.grid(row=8, column=7)
    d20.grid(row=8, column=8)
    d21.grid(row=8, column=9)
    d22.grid(row=9, column=7)
    d23.grid(row=9, column=8)
    d24.grid(row=9, column=9)
    d25.grid(row=10, column=7)
    d26.grid(row=10, column=8)
    d27.grid(row=10, column=9)

init_board()
font1=('Times',10,'normal')
my_s1= simpledialog.askstring("Input", "inter first player name",parent=root)
my_s2 = simpledialog.askstring("Input", "inter second player name",parent=root)
first_player, second_player, first_player_token, second_player_token=choose_players(my_s1,my_s2)


l1=tkinter.Label(root,text="welcome "+first_player+" is the x player "+second_player + " is the o player")
l1.grid(row=0,column=0,padx=10,pady=20)
#print(my_s)

#root.mainloop()

#create menue
my_menu = Menu(root)
root.config(menu=my_menu)
# print(board3d)


#create options menu
options_menu = Menu(my_menu, tearoff=False)
# print(board3d)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='scores', command=reset)
options_menu.add_command(label='Reset game', command=reset)
# print(board3d)

reset()
buttons= [b1, b2, b3, b4, b5, b6, b7, b8, b9,
               c10, c11, c12, c13, c14, c15, c16, c17, c18,
               d19, d20, d21, d22, d23, d24, d25, d26, d27]
root.mainloop()

