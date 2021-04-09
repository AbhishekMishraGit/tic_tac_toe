import random

#game board
boardList = [' ']*10


def gameboard(board):

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])



def whoGoesFirst():
    turn = random.randint(0,1)
    if turn == 0:
        return 'player'
    else:
        return 'computer'
    print('str(turn) + "will go first."')


def playerLetter():
    while True:
        myLetter = input("please choose a letter to start the game('X'or'O'): ").upper()
        
        if myLetter not in 'XO':
            print("you can enter either 'X' or 'O'")    
        else:
            break 
    return myLetter

def computerLetter(thisLetter):
    if thisLetter == 'X':
        computerLetter = 'O'
    else:
        computerLetter = 'X'
    return computerLetter


def move():
    while True:
        move = input('please enter one decimal value(1-9): ')
        if move not in '123456789':
            print('you can only enter one decimal value(1-9): ')
        else:
            break
    return int(move)

def boardMove(playerLetter, playerMove):
    while True:
        index = playerMove
        if boardList[index] == ' ':
            boardList[index] = playerLetter
            break
     

gameboard(boardList)
playerLetter = playerLetter()
computerLetter = computerLetter(playerLetter)
turn = whoGoesFirst()
move_Already_Played = []
while True:

    if turn = 'player':
            
        while True:
            playerMove = move()
            if playerMove in move_Already_Played:
                print('Move Already Played, enter a new move from 1-9')
            else:
                move_Already_Played.append(playerMove)
                break

    boardMove(playerLetter, playerMove)
    gameboard(boardList)






    
        



