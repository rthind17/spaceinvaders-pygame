import pygame
from spaceinvader import *
from os.path import abspath, dirname 

#SCREEN
width = 800
height = 600
main_screen = pygame.display.set_mode((width, height))
FPS = 60

#COLORS
white = (247, 247, 247)
green = (70, 212, 66)
bright_green = (7, 250, 32)
purple = (195, 66, 255)
red = (245, 22, 22)
blue = (22, 245, 223)
yellow = (245, 234, 22)
black = (0, 0, 0)

#IMAGES
main_path = abspath(dirname(__file__))
image_path = main_path + '/Images/'
image_name = ['ship', 'invader1_1', 'invader1_2', 'invader2_1', 'invader2_2', 'invader3_1', 'invader3_2', 'invader4', 'invaderlaser', 'explosionblue', 'explosiongreen', 'explosionpurple', 'green_laser']  
images = {name: pygame.image.load(image_path + '{}.png'.format(name)).convert_alpha() for name in image_name} 

#FONT
start_text_size = 30
font_path = './font/space_invaders.ttf'
font_size = 55

#Sound
SOUND_PATH = main_path + '/sound/'
sound_path = './sound/Star Wars Theme Song By John Williams.wav'

#ENEMY POS
enemy_pos = 65
enemy_move_down = 35

#BLOCKER POS
blocker_pos = 450
