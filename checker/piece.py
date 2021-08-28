from .contains import C_BLACK, C_ORANGE, C_PUR, C_TAN, SIZE_ROW_COL
import pygame


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == C_PUR:
            self.derection = 1
        elif self.color == C_ORANGE:
            self.derection = -1
        self.x = 0
        self.y = 0
        self.PADDING = 17
        self.piece_pos()

    def piece_pos(self):
        self.x = self.col * SIZE_ROW_COL + int(SIZE_ROW_COL // 2)
        self.y = self.row * SIZE_ROW_COL + int(SIZE_ROW_COL // 2)

    def make_king(self):
        self.king = True

    def move(self, row, col):
        self.col = col
        self.row = row
        self.piece_pos()

    def piece_draw(self, win):
        pygame.draw.circle(
            win, self.color, (self.x, self.y), SIZE_ROW_COL // 2 - self.PADDING
        )
        if self.king:
            pygame.draw.circle(
                win, C_BLACK, (self.x, self.y), SIZE_ROW_COL // 2 - self.PADDING * 2
            )

    def __repr__(self):
        return str(self.color)
