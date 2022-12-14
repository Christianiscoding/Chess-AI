import pygame
from pygame.locals import *

pygame.init()


def CREATE_CHESSBOARD(window_width, window_height, surface):
    rect_width = window_width / 8
    rect_height = window_height / 8
    x = y = 0
    color = None
    white = (245, 245, 220)
    black = (139, 90, 43)

    def create_horizontal_rects(x, y, color, color2):
        for i in range(8):

            rects = pygame.Rect(x, y, rect_width, rect_height)

            if i % 2 == 0:
                pygame.draw.rect(surface, color, rects)
                x += rect_width

            else:
                pygame.draw.rect(surface, color2, rects)
                x += rect_width

    x = 0

    for i in range(8):

        if i % 2 == 0:
            create_horizontal_rects(x, y, white, black)
            y += rect_height

        if i % 2 == 1:
            create_horizontal_rects(x, y, black, white)
            y += rect_width

