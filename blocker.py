import pygame
from settings import *
from spaceinvader import *

class Blocker(pygame.sprite.Sprite):
    def __init__(self, size, color, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):   
        self.game.main_screen.blit(self.image, self.rect)
