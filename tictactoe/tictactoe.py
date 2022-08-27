"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def movesonboard(board):
    count = 0
    for row in board:
        for move in row:
            if move != EMPTY:
                count += 1
    return count

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0 
    for row in board:
        for move in row:
            if move == X:
                countX += 1
            elif move == O:
                countO += 1
    if countX <= countO:
        return X
    return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = list()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                moves.append((row,col))
    return moves

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a = player(board)
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = a
    return result

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        set_row = set(row)
        if len(set_row) == 1 and list(set_row)[0] != EMPTY:
            return list(set_row)[0]
    for j in range(len(board)):
        set_col = set()
        for i in range(len(board)):
            set_col.add(board[i][j])
        if len(set_col) == 1 and list(set_col)[0] != EMPTY:
            return list(set_col)[0]
    set_dia_1 = {board[0][0],board[1][1],board[2][2]}
    set_dia_2 = {board[0][2],board[1][1],board[2][0]}
    if len(set_dia_1) == 1 and list(set_dia_1)[0] != EMPTY:
        return list(set_dia_1)[0]
    if len(set_dia_2) == 1 and list(set_dia_2)[0] != EMPTY:
        return list(set_dia_2)[0]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or movesonboard(board) == 9:
        return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play = player(board)
    if terminal(board):
        return None
    if play == X:
        x, move = max_value(board)
    else:
        x, move = min_value(board)
    return move
    raise NotImplementedError

def max_value(board):
    act = actions(board)
    var = float('-inf')
    move = None
    if terminal(board):
        return utility(board),None
    for action in act:
        x,dont = min_value(result(board,action))
        if x>var:
            var = x
            move = action
    return var,move

def min_value(board):
    act = actions(board)
    var = float('inf')
    move = None
    if terminal(board):
        return utility(board),None
    for action in act:
        if action == None:
            continue
        x,dont = max_value(result(board,action))
        if x<var:
            var = x
            move = action
    return var,move