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
        playerLetter = input("please choose a letter to start the game('X'or'O')")
        if len(playerLetter) != 1:
            print("you can enter either 'X' or 'O'")
        elif playerLetter not in 'XO':
            print("you can enter either 'X' or 'O'")
        else:
            break 
        return playerLetter

def computerLetter(playerLetter):
    if playerLetter == 'X':
        computerLetter = 'O'
    else:
        computerLetter = 'X'
    return computerLetter


def move():
    while True:
        move = input("please choose a position: ")
        if len(move) != 1:
            print("you can enter one value at a time.")
        elif move not in '123456789':
            print('please enter a integer value.')
        else:
            break
    return move

def playerMove():
    while True:
        index = int(move())
        if boardList[index] == ' ':
            boardList[index] = playerLetter
            break
     

gameboard(boardList)
playerLetter = playerLetter()
computerLetter = computerLetter(playerLetter)
turn = whoGoesFirst()
while True:
    playerMove()






    
        



