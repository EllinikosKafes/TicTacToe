from game import game_manager
from ui import renderer
import pygame

pygame.init()
clock,screen = renderer.setting_up(400,400)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


    renderer.refresh(clock,screen)

pygame.quit()