# Connect 4

"""
6 Vertical
7 Horizontal

X - P1
O - P2 / AI
"""

# Imports
import os
from colorama import Fore, Style, init
import random
import Connect4_Ai as AI

# Variables
game = True
isX = True
isY = False

# Functions
def clear_t():
    os.system('cls' if os.name == 'nt' else 'clear')

def boardInit():
    clear_t()
    for row in board:
        colored_row = []
        for cell in row:
            if cell == 'X':
                colored_row.append(Fore.LIGHTBLUE_EX + cell + Fore.RESET)
            elif cell == 'O':
                colored_row.append(Fore.LIGHTRED_EX + cell + Fore.RESET)
            else:
                colored_row.append(Fore.LIGHTBLACK_EX + cell + Fore.RESET)
        print('[{}] [{}] [{}] [{}] [{}] [{}] [{}]'.format(*colored_row))

def playerTurn(player):
    turnOver = False
    while not turnOver:
        turn = input(player + " turn: ")
        if not turn.isdigit() or int(turn) < 1 or int(turn) > 7:
            print(Fore.RED + "Invalid input! Please enter a number between 1 and 7.")
        else:
            column = int(turn) - 1
            for i in range(5, -1, -1):
                if board[i][column] == ' ':
                    board[i][column] = player
                    turnOver = True
                    break
            if not turnOver:
                print(Fore.RED + "This column is full! Please choose another one.")
    updateTerm()

def updateTerm():
    clear_t()
    for row in board:
        colored_row = []
        for cell in row:
            if cell == 'X':
                colored_row.append(Fore.LIGHTBLUE_EX + cell + Fore.RESET)
            elif cell == 'O':
                colored_row.append(Fore.LIGHTRED_EX + cell + Fore.RESET)
            else:
                colored_row.append(Fore.LIGHTBLACK_EX + cell + Fore.RESET)
        print('[{}] [{}] [{}] [{}] [{}] [{}] [{}]'.format(*colored_row))

def check_win(player):
    # Horizontal
    for row in board:
        for i in range(4):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                return True

    # Vertical
    for j in range(7):
        for i in range(3):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                return True

    # Diagonal
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                return True
    for i in range(3, 6):
        for j in range(4):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == player:
                return True

    return False

# Making board
board = [[' ' for i in range(7)] for i in range(6)]
boardInit()

# Game Loop
while game:
    isGUI = int(input(Fore.WHITE + "Terminal [0] or GUI [1]?\n"))
    if isGUI == 0:
        vsAI = int(input(Fore.WHITE + "PvP [0] or PvE [1]?\n"))
        if vsAI == 1:
            difflvl = int(input(Fore.WHITE + "Enter difficulty level from 0 [Stupidly Dumb] - 5 [Intermediate] - 10 [Expert]\nNote: Higher level will take more time to make a move.\n"))
            print(Fore.WHITE + "Please enter the number of the column where you want to place your disc.")
            while game:
                if isX:
                    playerTurn('X')
                    isX = False
                    isY = True
                elif isY:
                    if not AI.terminal(board):
                        move = AI.minimax(board, difflvl)
                        if move is not None:
                            AI.moves += 1
                            for i in range(5, -1, -1):
                                if board[i][move] == ' ':
                                    board[i][move] = 'O'
                                    break
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
                elif AI.moves == 42:
                    print(Fore.LIGHTWHITE_EX + "Draw!")
                    input()
                    exit()
            
            
        elif vsAI == 0:
            print(Fore.WHITE + "Please enter the number of the column where you want to place your disc.")
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
                elif AI.moves == 42:
                    print(Fore.LIGHTWHITE_EX + "Draw!")
                    input()
                    exit()