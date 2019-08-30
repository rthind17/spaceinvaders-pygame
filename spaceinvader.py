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
        self.load()

    def run(self):
        while self.running:
            if self.state == 'intro':
                self.intro_events()
                self.intro_updates()
                self.intro_draw()
                
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
        
    def main_text(self, words, screen, pos, color, Font, center=False):
        text = Font.render(words, False, color)
        text_size = text.get_size()
        
        if center:
            pos[0] = pos[0] - text_size[0]//2
            pos[1] = pos[1] - text_size[1]//2
        main_screen.blit(text, pos)
        
    def load(self):
        self.background = pygame.image.load('./Images/background.jpg')
        self.background = pygame.transform.scale(self.background, (width, height))
        
    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.state = 'playing'
    
    def intro_updates(self):
        pass
    
    def intro_draw(self):
        self.main_screen.blit(self.background, (0, 0))
        
        pygame.display.update()


   


    










        
        
