import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# rgb
BLACK = (217, 136, 128)
BLUE = (248, 196, 113)
GREY = (20, 12, 12)
RED = (195, 142, 217)
WHITE = (130, 224, 170)
CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))
