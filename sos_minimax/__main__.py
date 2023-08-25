from functools import cache

BOARD_LENGTH = 20
MARKS = "SO"


def possible_new_states(board: str):
    board = list(board)
    for i, c in enumerate(board):
        if c != " ":
            continue
        for m in MARKS:
            board_copy = board[:]
            board_copy[i] = m
            yield "".join(board_copy)


def count_sos(board: str):
    return board.count("SOS")


def evaluate(board: str, is_maximizing: bool):
    if count_sos(board):
        # If the current move is maximizing, the last has completed the SOS
        # Therefore the -1 for the maximizing
        return -1 if is_maximizing else 1
    else:
        if is_full(board):
            # Draw
            return 2


def is_full(board: str):
    return " " not in board


@cache
def minimax(board: str, is_maximizing: bool, alpha=-1, beta=1):
    score = evaluate(board, is_maximizing)
    if score is not None:
        return score

    scores = []
    for new_board in possible_new_states(board):
        scores.append(
            score := minimax(new_board, not is_maximizing, alpha, beta)
        )
        if is_maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break
    return (max if is_maximizing else min)(scores)


def best_move(board: str):
    for new_board in possible_new_states(board):
        score = minimax(new_board, is_maximizing=False)
        if score > 0:
            break
