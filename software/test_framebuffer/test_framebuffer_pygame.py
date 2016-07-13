import pygame
import sys
import time
import os

os.putenv('SDL_FBDEV', '/dev/fb1')

pygame.init()

size = (128, 160)
print pygame.display.Info().current_w
print pygame.display.Info().current_h
black = 0, 0, 255
screen = pygame.display.set_mode(size)

ball = pygame.image.load("../../img_128x/nigga128.bmp")
ballrect = ball.get_rect()

screen.fill(black)
screen.blit(ball, ballrect)
pygame.display.flip()

time.sleep(10)
