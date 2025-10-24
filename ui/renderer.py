import pygame
from pygame.locals import *

def setting_up(width,height):
    screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    return clock,screen

def refresh(clock,screen):
    screen.fill("gray")
    draw_board(screen)
    clock.tick(30)
    pygame.display.flip()

def draw_board(screen):
    pygame.draw.line(screen,"black",(125,0),(125,400),5)
    pygame.draw.line(screen,"black",(275,0),(275,400),5)
    pygame.draw.line(screen,"black",(0,125),(400,125),5)
    pygame.draw.line(screen,"black",(0,275),(400,275),5)