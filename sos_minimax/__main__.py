import sys
from functools import cache

sys.setrecursionlimit(10000)


MARKS = "SO"
MAX_DEPTH = 100
MAX_POSSIBLE_NEW_STATES = 100


# Can't cache this for some reason
def possible_new_states(board: str):
    board = list(board)
    for i, c in enumerate(board):
        if c != " ":
            continue
        for m in MARKS:
            board_copy = board[:]
            board_copy[i] = m
            yield "".join(board_copy)


@cache
def count_sos(board: str):
    return board.count("SOS")


@cache
def evaluate(board: str, is_maximizing: bool):
    if count_sos(board):
        # If the current move is maximizing, the last has completed the SOS
        # Therefore the -1 for the maximizing
        return -2 if is_maximizing else 1
    else:
        if is_full(board):
            # Draw
            return -1


@cache
def is_full(board: str):
    return " " not in board


@cache
def minimax(
    board: str,
    is_maximizing: bool,
    alpha=-1,
    beta=1,
    current_depth: int = 0
):
    current_depth += 1
    score = evaluate(board, is_maximizing)
    if score is not None:
        return score

    scores = []
    for i, new_board in enumerate(possible_new_states(board)):
        if i > MAX_POSSIBLE_NEW_STATES:
            print()
            break
        scores.append(
            score := minimax(
                new_board,
                not is_maximizing,
                alpha,
                beta,
                current_depth
            )
        )
        if current_depth > MAX_DEPTH:
            break
        if is_maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)
        if beta <= alpha:
            break
    return (max if is_maximizing else min)(scores)


@cache
def best_move(board: str):
    for new_board in possible_new_states(board):
        score = minimax(new_board, is_maximizing=False)
        if score > 0:
            break
    return score, new_board
