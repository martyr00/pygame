import sys
import pygame
from constants_for_rectangle_game import *

pygame.init()

time = pygame.time.Clock()

display = pygame.display.set_mode((DISPLAY_WIGHT, DISPLAY_HEIGHT))
pygame.display.set_caption("Shooter")

rect_x, rect_y = DISPLAY_WIGHT / 2 - RECT_WIGHT / 2, DISPLAY_HEIGHT / 2 - RECT_HEIGHT / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and rect_y + RECT_HEIGHT <= DISPLAY_HEIGHT - STEP:
                rect_y += STEP
            if event.key == pygame.K_UP and rect_y >= 0 + STEP:
                rect_y -= STEP
            if event.key == pygame.K_RIGHT and rect_x + RECT_WIGHT <= DISPLAY_WIGHT - STEP:
                rect_x += STEP
            if event.key == pygame.K_LEFT and rect_x >= 0 + STEP:
                rect_x -= STEP

    display.fill(DISPLAY_COLOR)
    pygame.draw.rect(display, RECT_COLOR, (rect_x, rect_y, RECT_WIGHT, RECT_HEIGHT))

    pygame.display.update()
