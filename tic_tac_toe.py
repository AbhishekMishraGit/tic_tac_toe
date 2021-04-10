import random

#game board
boardList = [' ']*10


def gameboard(board):

    print()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print()



def whoGoesFirst():# decides who will go first
    turn = random.randint(0,1)
    if turn == 0:
        return 'player'
    else:
        return 'computer'
    print('str(turn) + "will go first."')


def inputPlayerLetter():#asks to player to choose between 'X' or 'O'
    while True:
        myLetter = input("please choose a letter to start the game('X'or'O'): ").upper()
        
        if myLetter not in 'XO':
            print("you can enter either 'X' or 'O'")
        elif len(myLetter) == 2:
            print("You can choose either 'X' or 'O'")
        else:
            break 
    
    if myLetter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    


def inputPlayerMove():
    while True:
        move = input('please enter one decimal value(1-9): ')
        if move not in ['1','2','3','4','5','6','7','8','9']:
            print('you can only enter one decimal value(1-9): ')
        else:
            break
    return move

def boardMove(playerLetter, playerMove):
    while True:
        index = playerMove
        if boardList[index] == ' ':
            boardList[index] = playerLetter
            break

def checkIfWin(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter) 

def checkIfTie():
    for i in range(1, 10):
        if boardList[i] == ' ':
            return False 
    return True
    
gameboard(boardList)
playerLetter, computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
move_Already_Played = []
playerMove = ' '

while True:

    if turn == 'player':
            
        while True:
            playerMove = int(inputPlayerMove())
            if playerMove in move_Already_Played:
                print('Move Already Played, enter a new move from 1-9')
            else:
                move_Already_Played.append(playerMove)
                break

        boardMove(playerLetter, playerMove)
        gameboard(boardList)
        if checkIfWin(boardList, playerLetter):
            print('player win')
            break
        if checkIfTie():
            print('Game is Tie')
            break
        turn = 'computer'



    if turn == 'computer':

        while True:
            computerMove = int(input('input for computer: '))
            if computerMove in move_Already_Played:
                print('computer ji enter another value')
            else:
                move_Already_Played.append(computerMove)
                break

        boardMove(computerLetter, computerMove)
        gameboard(boardList)
        if checkIfWin(boardList, computerLetter):
            print('computer wins')
            break
        if checkIfTie():
            print('Game is Tie')
            break
        turn = 'player'



    
        
