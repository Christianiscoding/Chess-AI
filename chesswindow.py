import pygame, sys
from Chessgame import CREATE_CHESSBOARD

pygame.init()

WIDTH = HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
climage = pygame.image.load("files/cl.png")

def mainloop():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        CREATE_CHESSBOARD(WIDTH, HEIGHT, WINDOW)
        WINDOW.blit(climage, (20,20))

        pygame.display.update()


mainloop()