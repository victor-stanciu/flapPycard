import pygame
from settings import *

class BG(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        bg_image = pygame.image.load("../graphics/background.png").convert()


        self.image = pygame.transform.rotate(bg_image, 90)
        full_sized_image = pygame.transform.scale(self.image, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.image = pygame.Surface((WINDOW_WIDTH * 2, WINDOW_HEIGHT))
        self.image.blit(full_sized_image,(0,0))
        self.image.blit(full_sized_image,(WINDOW_WIDTH, 0))

        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 300 * dt
        #self.rect.x = round(self.pos.x)
        if self.rect.centerx <= 0:
            self.pos.x = 0

        self.rect.x = round(self.pos.x) 

