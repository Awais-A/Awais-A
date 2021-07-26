
# This file is for a tictactoe game. I will be using functional programming

from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# First I will be creating a visual representation of the board and initialising the list

board = [' ' for int in range(9)]


def display_board(board):
    clear()
    print('              |            |          ')
    print(f'       {board[0]}      |      {board[1]}     |     {board[2]}') 
    print('              |            |          ')
    print('--------------------------------------')
    print('              |            |          ')
    print(f'       {board[3]}      |      {board[4]}     |     {board[5]}')
    print('              |            |          ')
    print('--------------------------------------')
    print('              |            |          ')
    print(f'       {board[6]}      |      {board[7]}     |     {board[8]}')
    print('              |            |          ')
    


# Now I will let the players pick their marker. This will return a tuple I will unpack in the
# final game logic

def choose_marker():
    marker = ''
    while marker.upper() not in ['X','O']:
        marker = input('Player 1 please choose your marker, X or O: ')
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

# Now I will randomly decide who goes first

def goes_first():
    import random
    num = random.randint(0,1)
    if num == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
# This function will check if the chosen position is empty

def is_empty(board,position):
    return board[position-1] == ' '

# Now I will create a function that takes a position from the player and changes the board

def update(board,marker):
    position = 0
    while position not in range(1,10):
            position = int(input('Please enter a position from 1-9: '))
    if is_empty(board,position):
        board[position-1] = marker
    else:
        while position not in range(1,10):
            position = int(input('Please enter a valid position: '))
        board[position-1] = marker

# This function will check if the game has been drawn

def drawn(board):
    return ' ' not in board


# This function will check if the game has been won

def win_check(board,marker):
    
    return ((board[0] == board[1] == board[2] == marker) or 
    (board[3] == board[4] == board[5] == marker) or
    (board[6] == board[7] == board[8] == marker) or
    (board[0] == board[3] == board[6] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[0] == board[4] == board[8] == marker) or
    (board[2] == board[4] == board[6] == marker))
    
# This function will ask the user whether they want to play again

def play_game():
    playAgain = ' '
    while playAgain[0] not in ['Y','N']:
        playAgain = input('Would you like to play? Please enter yes or no: ').upper()
    if playAgain[0] == 'Y':
        return True
    else:
        return False
    
# I will get the players position

print('Welcome to Tic Tac Toe!')

while True:
    player1_marker,player2_marker = choose_marker()
    print(player2_marker)
    print(player1_marker)
    turn =  goes_first()
    print(f'{turn} goes first!')
    board = [' ' for int in range(9)]
    
    if play_game():
        game_on = True
    while game_on:
        if turn == 'Player 1':
            display_board(board)
            update(board,player1_marker)
            display_board(board)
            
            if win_check(board,player1_marker):
                display_board(board)
                print('Congratulations player 1! You have won!')
                game_on = False
            else:
                if drawn(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            update(board,player2_marker)
            display_board(board)
            
            if win_check(board,player2_marker):
                display_board(board)
                print('Congratulations player 2! You have won!')
                game_on = False
            else:
                if drawn(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not play_game():
        break
                        
    