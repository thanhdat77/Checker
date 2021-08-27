from checker.contains import C_GRAY, C_WHITE, SIZE_ROW_COL
import pygame


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        if self.color == C_WHITE:
            self.derection = 1
        elif self.color == C_GRAY:
            self.derection = -1
        self.x = 0
        self.y = 0
        self.PADDING = 10

    def piece_pos(self):
        self.x = self.col * SIZE_ROW_COL + SIZE_ROW_COL // 2
        self.y = self.row * SIZE_ROW_COL + SIZE_ROW_COL // 2

    def piece_king(self):
        self.king = True

    def piece_draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), SIZE_ROW_COL - PADDING)
