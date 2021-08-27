import pygame
from checker.contains import COLOMNS, C_GRAY, ROWS, SIZE_ROW_COL, C_WHITE
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.select_piece = None
        self.red_left = self.white = 12
        self.red_king = self.white_king = 0
        self.create_piece()

    def draw_br(self, win):
        win.fill(C_GRAY)
        for row in range(ROWS):
            for col in range(row % 2, COLOMNS, 2):
                pygame.draw.rect(
                    win,
                    C_WHITE,
                    (
                        row * SIZE_ROW_COL,
                        col * SIZE_ROW_COL,
                        SIZE_ROW_COL,
                        SIZE_ROW_COL,
                    ),
                )

    def create_piece(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLOMNS):
                if row % 2 == (col + 1) % 2:
                    if row <= 2:
                        self.board[row].append(Piece(row, col, C_WHITE))
                    elif row >= 5:
                        self.board[row].append(Piece(row, col, C_GRAY))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_br(win)
        for row in range(ROWS):
            for col in range(COLOMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.piece_draw(win)
