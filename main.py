
board3d=[]
def init_board():
    for x in range(0, 27):
        board3d.append(x)

def validate(index):
    valid=0 #true value
    try:
        number = int(index)  # Convert input to an integer

        if 0 <= number <= 27:
            if (takenCell(index)=="notTaken" ):
                 print("Valid input")
                 return valid
            else:
                print ("the cell is already assigned")
                valid=1
                return valid


        else:
            print("Number is outside the range of 0 to 27")
            valid=1
            return valid

    except ValueError:
        print("Invalid input. Please enter a number.")
        valid = 1
        return valid

def takenCell(index):
    #checks if the cell is already assigned to x or o
    if board3d[index]==index:
        return "notTaken"
    else:
        return "taken"







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # init_board()
    # board3d[3]="o"
    # r=validate(3)
    # e=validate(4)
    # t=takenCell(3)
    # tt=takenCell(4)
    #
    # x=1


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
