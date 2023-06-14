import sys
import pygame
from constants_for_shooter_game import *

pygame.init()

screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Shooter")

fighter_img = pygame.image.load('img/fighter.png')
fighter_wight, fighter_height = fighter_img.get_size()
fighter_x, fighter_y = DISPLAY[0] / 2 - fighter_wight / 2, DISPLAY[1] - fighter_height

enemy_img = pygame.image.load('img/enemy.png')
enemy_wight, enemy_height = enemy_img.get_size()

rockets_img = pygame.image.load('img/rockets.png')
rockets_wight, rockets_height = rockets_img.get_size()

fighter_is_moving_left, fighter_is_moving_right = False, False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= 0 + FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= DISPLAY[0] - fighter_wight - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    screen.blit(pygame.image.load('img/display.png'), (0, 0))
    screen.blit(fighter_img, (fighter_x, fighter_y))

    pygame.display.update()
