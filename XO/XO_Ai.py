# Tic Tac Toe AI via Minimax Algorithm

'''
X - Max Player
O - Min Player

X Win = 1
Draw = 0
O Win = -1
'''

# Imports
from collections import Counter
from copy import deepcopy
from numpy import array

# Variables
global moves 
moves = 0 # Updated from TicTacToe.py

# Functions

def check_win(player, board):
    for row in board:
        if row.count(player) == 3:
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def player(board):
    f_board = array(board).flatten()
    x_o = Counter(tuple(f_board))
    if x_o['X'] == x_o['O']:
        return 'X'
    else:
        return 'O'

def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def result(board, action):
    new_board = deepcopy(board)  # Make a deep copy of the board
    new_board[action[0]][action[1]] = player(board)
    return new_board

def terminal(board):
    if check_win('X', board) or check_win('O', board) or len(actions(board)) == 0:
        return True
    else:
        return False
    
def utility(board, depth):
    if check_win('X', board):
        return 10 - depth
    elif check_win('O', board):
        return -10 + depth
    else:  # The game is a draw
        return 0

def minimax(board):
    move = None
    if player(board) == 'X':
        _, move = max_value(board, 0)
    elif player(board) == 'O':
        _, move = min_value(board, 0)
    return move
        
def min_value(board, depth):
    if terminal(board):
        return utility(board, depth), None
    v = float('inf')
    best_move = None
    for move in actions(board):
        new_board = result(board, move)
        value, _ = max_value(new_board, depth + 1)
        if value is not None and value < v:
            v = value
            best_move = move
    return v, best_move

def max_value(board, depth):
    if terminal(board):
        return utility(board, depth), None
    v = float('-inf')
    best_move = None
    for move in actions(board):
        new_board = result(board, move)
        value, _ = min_value(new_board, depth + 1)
        if value is not None and value > v:
            v = value
            best_move = move
    return v, best_move
