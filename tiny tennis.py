import pygame
import time
import time
pygame.init()
r=(255, 0, 0)
o=(255, 127.5, 0)
y=(255, 255, 0)
g=(0, 255, 0)
b=(0, 0, 255)
screenwidth=900
screenheight=900
game_screen=pygame.display.set_mode((screenheight, screenwidth))
pygame.display.set_caption('Tiny Tennis')
font=pygame.font('monospace', 75)
ball_x=int(screenwidth/2)
ball_y=int(screenheight/2)
ball_xv=3
ball_yv=3
ball.r=10
