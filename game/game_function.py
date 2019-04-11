# -- coding: utf-8 --

import sys
import pygame

#响应 退出操作
def check_events(ship):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                ship.moving_right = True
                ship.moving_left = False
            elif events.key == pygame.K_LEFT:
                ship.moving_right = False
                ship.moving_left = True
        elif events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif events.key == pygame.K_LEFT:
                ship.moving_left = False



def update_screen(settings,screen,ship):
    screen.fill(settings.bg_color)
    ship.blitme()
    pygame.display.flip()