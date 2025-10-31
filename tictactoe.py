from game import game_manager,player,board,settings
from ui import renderer,events
from network import client
import pygame


def main_game():

    player1 = player.Player("Me",'x')
    player2 = player.Player("John","o")
    current_player = player1
    board.clear()
    while True:
        
        number = events.check_box()
        if number:
            if not board.check_if_pressed(number):
                board.press_square(number,current_player.symbol)
                win=board.check_win()
                if win == True:
                    print(f"{current_player.name} wins!")

                    renderer.refresh(clock, screen, board.get_board())
                    pygame.display.update()

                    action = game_manager.show_end_screen(screen, clock, current_player.name)
                    return action
                    
                if board.is_full():
                    renderer.refresh(clock, screen, board.get_board())
                    pygame.display.update()

                    action = game_manager.show_end_screen(screen, clock, False)
                    return action
                   
                current_player = player2 if current_player==player1 else player1
        
        renderer.refresh(clock,screen,board.get_board())


def lan_game():
    my_player = player.Player("yo",'x')
    board.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        try:
            if client.connect():  # returns True when connected
                break
        except Exception as e:
            print("Connection error:", e)
        renderer.connecting(clock, screen)

    # 2️⃣ Wait for both players to be ready
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        try:
            if client.check_if_ready():  # returns True when server signals ready
                break
        except Exception as e:
            print("Waiting error:", e)
        renderer.waiting(clock, screen)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                
        renderer.refresh(clock,screen,board.get_board())
                    


pygame.init()
clock, screen = renderer.setting_up(settings.WIDTH, settings.HEIGHT)

mode = game_manager.menu(screen)

if mode == "Solo":
    while True:
        action = main_game()
        if action == "quit":
            break

if mode == "LAN":
    while True:
        action = lan_game()
        if action == "quit":
            break

pygame.quit()
