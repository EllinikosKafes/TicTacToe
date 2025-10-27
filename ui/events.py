import pygame
from pygame.locals import *
from game import board

def check_hitbox(pos):
    x, y = pos
    
    # Must be inside 400x400 window
    if not (0 <= x < 400 and 0 <= y < 400):
        return None

    # Grid is 3x3 → each square is ~133.33 pixels
    box_width = 400 / 3

    col = int(x // box_width)   # 0,1,2         100//133 = 0
    row = int(y // box_width)   # 0,1,2         200//133 = 1

    # Convert row/col → box number 1–9
    square_id = row * 3 + col + 1              
    return square_id

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
            