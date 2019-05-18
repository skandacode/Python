import pygame
import time

pygame.init()

screen_width=600
screen_height=400

black=(0, 0, 0)
white=(255, 255, 255)
red=(255, 0, 0)
blue=(0, 0, 255)
green=(0,255, 0)

game_screen = pygame.display.set_mode((screen_width, screen_height))
game_screen.fill(red)
while True:
    pygame.draw.circle(game_screen, blue, (250,300), 20)
    pygame.display.update()
