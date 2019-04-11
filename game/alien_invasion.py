# -- coding: utf-8 --

import sys
import pygame
from game.settings import Settings
from pygame.sprite import Group
from game.ship import ship
import game.game_function as gf


def run_game():
    #初始化类
    pygame.init()
    ali_settings = Settings()
    #对屏幕的大小控制
    screen = pygame.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))
    ali_ship = ship(ali_settings,screen)
    bullets = Group();
    pygame.display.set_caption(ali_settings.title)
    while True:
        gf.check_events(ali_ship)
        ali_ship.update()
        bullets.update()
        gf.update_screen(ali_settings,screen,ali_ship)
run_game()
