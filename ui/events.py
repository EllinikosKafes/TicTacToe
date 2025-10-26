import pygame
from pygame.locals import *
from game import board

def check_hitbox(pos):          
    if pos[1] <=130:
        if pos[0]<=130:
            return 1
        elif pos[0]<=265 and pos[0]>135:
            return 2
        elif pos[0]<=400 and pos[0]>270:
            return 3
        else:
            print("limits")

    elif pos[1]<=265 and pos[1]>135:
        if pos[0]<=130:
            return 4
        elif pos[0]<=265 and pos[0]>135:
            return 5
        elif pos[0]<=400 and pos[0]>270:
            return 6
        else:
            print("limits")

    elif pos[1]<=400 and pos[1]>270:
        if pos[0]<=130:
            return 7
        elif pos[0]<=265 and pos[0]>135:
            return 8
        elif pos[0]<=400 and pos[0]>270:
            return 9
        else:
            return None

    else:
        return None


def check_box():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            if check_hitbox(mouse_pos):
                return check_hitbox(mouse_pos)
            else:
                return None
            