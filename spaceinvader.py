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
        self.enemy1 = pygame.image.load('./Images/invader3_1.png')
        self.enemy1 = pygame.transform.scale(self.enemy1, (width//25, height//20))

        self.enemy2 = pygame.image.load('./Images/invader2_2.png')
        self.enemy2 = pygame.transform.scale(self.enemy2, (width//25, height//20))

        self.enemy3 = pygame.image.load('./Images/invader1_2.png')
        self.enemy3 = pygame.transform.scale(self.enemy3, (width//25, height//20))

        self.enemy4 = pygame.image.load('./Images/invader4.png')
        self.enemy4 = pygame.transform.scale(self.enemy4, (width//14, height//19))
        
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
        self.main_screen.blit(self.enemy1, (width//2.4, height//2.1))
        self.main_screen.blit(self.enemy2, (width//2.4, height//1.825))
        self.main_screen.blit(self.enemy3, (width//2.4, height//1.6))
        self.main_screen.blit(self.enemy4, (width//2.489, height//1.435))
        
        self.main_text(
                'SPACE INVADERS',
                self.main_screen,
                [width//2, height//3],
                (white), 
                pygame.font.Font(font_path, font_size),
                center=True
            )

        self.main_text(
                'HIGH SCORE',
                self.main_screen,
                [75, 20],
                (white),
                pygame.font.Font(font_path, 20),
                center=True
            )
        
        self.main_text(
                'PRESS ANY KEY TO CONTINUE',
                self.main_screen,
                [width//2, height//2.3],
                (white),
                pygame.font.Font(font_path, 20),
                center=True
            )
        
        
        pygame.display.update()


   


    










        
        
