import pygame
from pygame.locals import *
from game import settings

pygame.font.init()
font = pygame.font.SysFont("Arial",50,bold=True)
small_font = pygame.font.SysFont("Arial",25,bold=True)


def draw_text(screen,text):
    img = font.render(text,True,(255,255,255))
    screen.blit(img,(settings.WIDTH/2,settings.HEIGHT/2))
    

def draw_boxes(screen,board):
    
    for i in range(len(board)):                         # run through the board (list)
        if board[i]!=0:                                 # if board[i] has x or o in it ...
            img = font.render(board[i],True,settings.X_COLOR) if board[i] == 'x' else font.render(board[i],True,settings.O_COLOR)# render the relative symbol (x or o)
            if i<=2:
                screen.blit(img,(50+130*i,50))
            elif i<=5:
                screen.blit(img,(50+130*(i-3),175))
            else:
                screen.blit(img,(50+130*(i-6),325))
        else:
            None

def setting_up(width,height):
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Tic-Tac-Toe")
    clock = pygame.time.Clock()
    return clock,screen

def refresh(clock,screen,board):
    screen.fill("black")
    draw_board(screen)
    draw_boxes(screen,board)
    clock.tick(settings.FPS)
    pygame.display.flip()

def draw_board(screen):
    pygame.draw.line(screen,"white",(130,0),(130,400),5)
    pygame.draw.line(screen,"white",(270,0),(270,400),5)
    pygame.draw.line(screen,"white",(0,130),(400,130),5)
    pygame.draw.line(screen,"white",(0,265),(400,265),5)

def connecting(clock,screen):
    screen.fill("black")
    img=small_font.render("Connecting to server",True,settings.white)
    screen.blit(img,(50,200))
    pygame.display.flip()
    clock.tick(settings.FPS)
    

def waiting(clock,screen):
    screen.fill("black")
    img=small_font.render("Waiting for others",True,settings.white)
    screen.blit(img,(50,200))
    pygame.display.flip()
    clock.tick(settings.FPS)
    