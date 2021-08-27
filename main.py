import pygame
from checker.contains import WIDTH_X, HEGHT_Y
from checker.board import Board

WIN = pygame.display.set_mode((WIDTH_X, HEGHT_Y))
pygame.display.set_caption("CHECKER")
FPS = 60


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
                pass
        board.draw(WIN)
        pygame.display.update()
    pygame.quit()


main()
