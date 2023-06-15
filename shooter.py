import sys

import pygame

from constants_for_shooter_game import *
from random import randint

pygame.init()

GAME_FONT = pygame.font.Font(None, 82)
time = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Shooter")

fighter_img = pygame.image.load('img/fighter.png')
fighter_wight, fighter_height = fighter_img.get_size()
fighter_x, fighter_y = DISPLAY[0] / 2 - fighter_wight / 2, DISPLAY[1] - fighter_height
fighter_is_moving_left, fighter_is_moving_right = False, False


enemy_img = pygame.image.load('img/enemy.png')
enemy_wight, enemy_height = enemy_img.get_size()
enemy_x, enemy_y = randint(0, DISPLAY[0] - enemy_wight), 0
enemy_was_area = True

rockets_img = pygame.image.load('img/rockets.png')
rockets_wight, rockets_height = rockets_img.get_size()
rockets_x, rockets_y = fighter_x + fighter_wight / 2 - rockets_wight / 2, fighter_y
rockets_was_fired = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rockets_was_fired = True
                rockets_x, rockets_y = fighter_x + fighter_wight / 2 - rockets_wight / 2, fighter_y
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left and fighter_x >= 0 + FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= DISPLAY[0] - fighter_wight - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if rockets_was_fired:
        rockets_y -= ROCKETS_STEP
    if rockets_was_fired and rockets_y + rockets_height < 0:
        rockets_was_fired = False
    if enemy_was_area:
        enemy_y += ENEMY_STEP

    screen.blit(pygame.image.load('img/display.png'), (0, 0))
    screen.blit(fighter_img, (fighter_x, fighter_y))

    if rockets_was_fired:
        screen.blit(rockets_img, (rockets_x, rockets_y))

    screen.blit(enemy_img, (enemy_x, enemy_y))

    pygame.display.update()

    if enemy_y + enemy_height > fighter_y:
        break

    if rockets_was_fired \
            and enemy_x < rockets_x < enemy_x + enemy_wight - rockets_wight \
            and enemy_y < rockets_y < enemy_y + enemy_height - rockets_height:
        rockets_was_fired = False
        enemy_x, enemy_y = randint(0, DISPLAY[0] - enemy_wight), 0

game_over_text = GAME_FONT.render("GAME OVER", True, 'yellow')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (DISPLAY[0] / 2, DISPLAY[1] / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
