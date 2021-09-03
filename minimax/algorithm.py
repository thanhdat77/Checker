import pygame
from checkers.constants import RED, WHITE
from copy import deepcopy


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float("-inf")
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(evaluation, maxEval)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move

    elif not max_player:
        minEval = float("inf")
        worse_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(evaluation, minEval)
            if minEval == evaluation:
                worse_move = move
        return minEval, worse_move


def simulate_move(temp_board, temp_piece, move, skip):
    temp_board.move(temp_piece, move[0], move[1])
    if skip:
        temp_board.remove(skip)
    return temp_board


def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_board, temp_piece, move, skip)
            moves.append(new_board)
    return moves
