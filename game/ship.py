# -- coding: utf-8 --

import pygame

class ship():
    def __init__(self,ali_settings,screen):
        self.settings=ali_settings
        self.screen=screen
        #load the photo
        self.image = pygame.image.load("ship.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #控制相对位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center =float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        #自身绘制
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        self.rect.centerx = self.center