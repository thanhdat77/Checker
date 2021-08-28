import pygame
from checker.contains import C_BLACK, COLOMNS, C_BE, C_ORANGE, ROWS, SIZE_ROW_COL, C_TAN,C_PUR
from checker.piece import Piece
import random


class Board:
    def C_RAND(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def __init__(self):
        self.board = []
        self.select_piece = None
        self.red_left = self.white_left = 12
        self.red_king = self.white_king = 0
        self.create_piece()

    def draw_br(self, win):
        win.fill(C_TAN)
        for row in range(ROWS):
            for col in range(row % 2, COLOMNS, 2):
                pygame.draw.rect(
                    win,
                    C_BE,
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
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, C_PUR))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, C_ORANGE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def move_piece(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )
        piece.move(row, col)
        if row == ROWS or row == 0:
            piece.make_king()

    def get_piece(self, row, col):
        return self.board[row][col]

    def draw(self, win):
        self.draw_br(win)
        for row in range(ROWS):
            for col in range(COLOMNS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.piece_draw(win)
