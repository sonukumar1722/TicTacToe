"""
Tic Tac Toe Player
"""

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


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
    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                x_count += 1
            elif (board[i][j] == O):
                o_count += 1
    if (x_count > o_count):
        return O
    elif (o_count > x_count):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that result from making move (i, j) on the board.
    """

    if not action:
        raise Exception

    new_copy = deepcopy(board)
    curr_player = player(board)
    i, j = action[0], action[1]
    new_copy[i][j] = curr_player
    return new_copy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows
    for i in range(3):
        if board[i].count(X) == 3:
            return X
        elif board[i].count(O) == 3:
            return O

    # Columns
    for i in range(3):
        column = ''
        for j in range(3):
            column += str(board[j][i])
        if column == "XXX":
            return X
        if column == "OOO":
            return O

    # Diagonals
    diagonal_1 = ''
    diagonal_2  = ''
    j = 2

    for i in range(3):
        diagonal_1 += str(board[i][i])
        diagonal_2 += str(board[i][j])

        if diagonal_1 == "XXX" or diagonal_2 == "XXX":
            return X
        if diagonal_1 == "OOO" or diagonal_2 == "OOO":
            return O
        j -= 1

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    if winning_player == O:
        return -1
    return 0


def min_value(board):
    if terminal(board):
        return (utility(board), None)
        # return utility(board)

    v = float("inf")
    best_move = None
    for action in actions(board):
        score = max_value(result(board, action))
        if  score[0] <= v:
            best_move = action
            v = score[0]

    return (v, best_move)

def max_value(board):
    if terminal(board):
        return (utility(board), None)

    v = float("-inf")
    best_move = None
    for action in actions(board):
        score = min_value(result(board, action))
        if ( score[0] > v):
            best_move = action
            v = score[0]

    return (v, best_move)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if (player(board) == O):
        return min_value(board)[1]
    if (player(board) == X):
        return max_value(board)[1]
