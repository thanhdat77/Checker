import pygame
from checker.contains import SIZE_ROW_COL, WIDTH_X, HEGHT_Y
from checker.game_mn import Game_mn

WIN = pygame.display.set_mode((WIDTH_X, HEGHT_Y))
pygame.display.set_caption("CHECKER")
FPS = 60


def get_row_col_from_mouse(pos):
    x, y = pos
    row = int(y // SIZE_ROW_COL)
    col = int(x // SIZE_ROW_COL)
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game_mn = Game_mn(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                

        game_mn.update()

    pygame.quit()


main()
