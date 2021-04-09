import random

#game board
boardList = [' ']*10


def gameboard(board):

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])



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
        index = int(playerMove)
        if boardList[index] == ' ':
            boardList[index] = playerLetter
            break
     

gameboard(boardList)
playerLetter, computerLetter = inputPlayerLetter()
turn = 'player'#whoGoesFirst()
move_Already_Played = []
playerMove = ' '
while True:

    if turn == 'player':
            
        while True:
            playerMove = inputPlayerMove()
            if playerMove in move_Already_Played:
                print('Move Already Played, enter a new move from 1-9')
            else:
                move_Already_Played.append(playerMove)
                break

    boardMove(playerLetter, playerMove)
    gameboard(boardList)






    
        



