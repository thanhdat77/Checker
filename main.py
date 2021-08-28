import pygame
from checker.contains import SIZE_ROW_COL, WIDTH_X, HEGHT_Y
from checker.board import Board

WIN = pygame.display.set_mode((WIDTH_X, HEGHT_Y))
pygame.display.set_caption("CHECKER")
FPS = 60


def get_row_col_from_mouse(pos):
    x, y = pos

    row = int(y // SIZE_ROW_COL)
    col = int(x // SIZE_ROW_COL)
    print(row, col)
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move_piece(piece, 3, 1)

        board.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
