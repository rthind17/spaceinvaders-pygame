import pygame
import sys
from settings import *

pygame.init()

class Space_Invaders:
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
        
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.state = 'playing'
    
    def intro_updates(self):
        pass
    
    def intro_draw(self):
        self.main_screen.fill(black)

   


    










        
        
