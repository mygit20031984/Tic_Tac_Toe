#import random

board = [0,1,2,
         3,4,5,
         6,7,8]



def checkLine(char,spot1,spot2,spot3):
    if board[spot1] ==  char and board[spot2] ==  char and board[spot3] ==  char:
        return True

def checkAll(char):
    if checkLine(char,0,1,2):
        return True
    if checkLine(char,3,4,5):
        return True
    if checkLine(char,6,7,8):
        return True
    if checkLine(char,0,3,6):
        return True
    if checkLine(char,1,4,7):
        return True
    if checkLine(char,2,5,8):
        return True
    if checkLine(char,0,4,8):
        return True
    if checkLine(char,2,4,6):
        return True



def show():
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])

print("Your Current Borad is : ")
show()

while True:
    playerA = int(input('PlayerA, please spot number: '))

    if (board[playerA] != 'A' and board[playerA] != 'B'):
        board[playerA] = 'A'
        show()
        #Check
        if checkAll('A') == True:
            print('Player A Won :)')
            show()
            break;

        while True:
            PlayerB = int(input('PlayerB, please spot number: '))
            if (board[PlayerB] != 'A' and board[PlayerB] != 'B'):
                board[PlayerB] = 'B'
                show()

                #Check
                if checkAll('B') == True:
                    print('Player B Won)')
                    show()
                    winner = PlayerB
                    break;
                break;

            else:
                print('This spot is already taken.')

    else:
        print('This spot is already taken.')

