import pygame
import sys
from settings import *

pygame.init()

class Space_Invaders(object):
    def __init__(self):
        self.main_screen = main_screen
        self.caption = pygame.display.set_caption('Space Invaders')
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'intro'

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_updates()
                self.intro_draw()
                
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

   


    










        
        
