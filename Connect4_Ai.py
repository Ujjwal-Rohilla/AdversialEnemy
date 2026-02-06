# Connect 4 Algorithm via Minimax Algorithm (Alpha-Beta pruning)

"""
X - Max Player
O - Min Player

X Win = 1
Draw = 0
O Win = -1
"""

# Imports
from collections import Counter
from copy import deepcopy
from numpy import array

# Variables
global moves
moves = 0 # Updated from Connect4.py

# Functions

def check_win(player, board):
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

def player(board):
    f_board = array(board).flatten()
    x_o = Counter(tuple(f_board))
    if x_o['X'] == x_o['O']:
        return 'X'
    else:
        return 'O'
    
def actions(board):
    return [i for i in range(7) if board[0][i] == ' ']

def result(board, action):
    new_board = deepcopy(board)  # Make a deep copy of the board
    for i in range(5, -1, -1):
        if new_board[i][action] == ' ':
            new_board[i][action] = player(board)
            break
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
        return depth - 10
    else:
        return 0

def minimax(board, depth_limit=10):
    best_move = None
    for depth in range(1, depth_limit + 1):
        if player(board) == 'X':
            _, move = max_value(board, 0, float("-inf"), float("inf"), depth)
        elif player(board) == 'O':
            _, move = min_value(board, 0, float("-inf"), float("inf"), depth)
        if move is not None:
            best_move = move
    return best_move

def min_value(board, depth, alpha, beta, depth_limit):
    if terminal(board) or depth == depth_limit:
        return utility(board, depth), None
    v = float('inf')
    best_move = None
    for move in actions(board):
        new_board = result(board, move)
        value, _ = max_value(new_board, depth + 1, alpha, beta, depth_limit)
        if value is not None and value < v:
            v = value
            best_move = move
        if v <= alpha:
            return v, best_move
        beta = min(beta, v)
    return v, best_move

def max_value(board, depth, alpha, beta, depth_limit):
    if terminal(board) or depth == depth_limit:
        return utility(board, depth), None
    v = float('-inf')
    best_move = None
    for move in actions(board):
        new_board = result(board, move)
        value, _ = min_value(new_board, depth + 1, alpha, beta, depth_limit)
        if value is not None and value > v:
            v = value
            best_move = move
        if v >= beta:
            return v, best_move
        alpha = max(alpha, v)  
    return v, best_move