# Tic Tac Toe

'''Tic Tac Toe Board
[1][2][3]
[4][5][6]
[7][8][9]
'''

# Imports
import os
import XO_Ai
from colorama import Fore, Style, init
import random
import TicTacToeGUI as tgui
init(autoreset=True)

# Variables
game = True
isX = True
isY = False
turnOver = False

# Functions
def clear_t():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_win(player):
    for row in board:
        if row.count(player) == 3:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def playerTurn(player):
    global moves
    turnOver = False
    while not turnOver:
        turn = int(input(player + "turn: "))
        # Get the indices from the mapping
        if turn < 1 or turn > 9:
            print(Fore.RED + "Invalid input! Please enter a number between 1 and 9.")
        else:
            i, j = mapping[turn]
            if board[i][j] == ' ':
                # Insert player's symbol
                board[i][j] = player
                
                XO_Ai.moves += 1
                turnOver = True
                updateTerm()
                
            else:
                print(Fore.RED + "This square has already been used!!")

def updateTerm():
    clear_t()
    for row in board:
        colored_row = []
        for cell in row:
            if cell == 'X':
                colored_row.append(Fore.LIGHTBLUE_EX + cell + Fore.LIGHTBLACK_EX)
            elif cell == 'O':
                colored_row.append(Fore.LIGHTRED_EX + cell + Fore.LIGHTBLACK_EX)
            else:
                colored_row.append(cell)
        print(Fore.LIGHTBLACK_EX + '[{}] [{}] [{}]'.format(*colored_row))

def boardInit():
    clear_t()
    tic_tac_toe = list("TICTACTOE")
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX]
    for i in range(3):
        row = []
        for j in range(3):
            color = random.choice(colors)
            row.append(color + tic_tac_toe[i*3 + j] + Fore.RESET)
        print((Fore.LIGHTBLACK_EX + '[{}' + Fore.LIGHTBLACK_EX + ']' + ' [{}' + Fore.LIGHTBLACK_EX + ']' + ' [{}' + Fore.LIGHTBLACK_EX + ']').format(*row))

# Make board
board = [[' ' for i in range(3)] for i in range(3)]

# Create a mapping between the user's input and the indices of the board
mapping = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2)}

boardInit()

while game:
    isGUI = int(input(Fore.WHITE + "Terminal [0] or GUI [1]?\n"))

    if isGUI == 0:
        vsAI = int(input(Fore.WHITE + "PvP [0] or PvE [1]?\n"))
        if vsAI == 1:
            print(Fore.WHITE + "Please enter the number of the square you want to place your X in.")
            while game:
                if isX:
                    playerTurn('X')
                    isX = False
                    isY = True
                elif isY:
                    if not XO_Ai.terminal(board):
                        move = XO_Ai.minimax(board)
                        if move is not None:
                            XO_Ai.moves += 1
                            board[move[0]][move[1]] = 'O'
                            updateTerm()
                    isX = True
                    isY = False

                # Draw/Win Check
                if check_win('X'):
                    print(Fore.LIGHTWHITE_EX + "X won!")
                    input()
                    exit()
                elif check_win('O'):
                    print(Fore.LIGHTWHITE_EX + "O won!")
                    input()
                    exit()
                elif XO_Ai.moves == 9:
                    print(Fore.LIGHTWHITE_EX + "Draw!")
                    input()
                    exit()
            
        elif vsAI == 0:
            print(Fore.WHITE + "Please enter the number of the square you want to place your X in.")
            while game:
                if isX:
                    playerTurn('X')
                    isX = False
                    isY = True

                elif isY:
                    playerTurn('O')
                    isX = True
                    isY = False

                # Draw/Win Check
                if check_win('X'):
                    print(Fore.LIGHTWHITE_EX + "X won!")
                    input()
                    exit()
                elif check_win('O'):
                    print(Fore.LIGHTWHITE_EX + "O won!")
                    input()
                    exit()
                elif XO_Ai.moves == 9:
                    print(Fore.LIGHTWHITE_EX + "Draw!")
                    input()
                    exit()
    
    elif isGUI == 1:
        vsAI = int(input(Fore.WHITE + "PvP [0] or PvE [1]?\n"))
        if vsAI == 1:
            tgui.initGUI(board, True)
            
        elif vsAI == 0:
            tgui.initGUI(board)
    
    else:
        print(Fore.RED + "Invalid input! Please enter 0 or 1.")
