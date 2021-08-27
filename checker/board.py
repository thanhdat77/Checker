import pygame
from checker.contains import C_GRAY, ROWS, SIZE_ROW_COL, C_WHITE


class Board:
    def __init__(self):
        self.board = []
        self.select_piece = None
        self.red_left = self.white = 12
        self.red_king = self.white_king = 0

    def raw_wd(self, win):
        win.fill(C_GRAY)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
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
