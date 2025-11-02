from game import game_manager,player,board,settings
from ui import renderer,events
from network import client as lan_client
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
    
    # Initialize board and client
    game_board = board.Board()
    my_player = player.Player("Me", "x")
    client = lan_client.LANClient()

    # Determine whose turn this client plays
    turn = 0
    print(f"My player ID (turn): {client.play_on_turn}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        renderer.refresh(clock, screen, game_board.get_board())

        # ✅ Only allow input on your turn
        if turn == client.play_on_turn:
            number = events.check_box()
            if number and not game_board.check_if_pressed(number):
                game_board.press_square(number, my_player.symbol)
                client.update(game_board.get_board())
                # Wait for server update (new board + next turn)
                game_board.board, turn = client.listen(game_board.board)

                win = game_board.check_win()
                if win:
                    renderer.refresh(clock, screen, game_board.get_board())
                    pygame.display.update()
                    action = game_manager.show_end_screen(screen, clock, my_player.name)
                    return action

                if game_board.is_full():
                    renderer.refresh(clock, screen, game_board.get_board())
                    pygame.display.update()
                    action = game_manager.show_end_screen(screen, clock, False)
                    return action
        else:
            # Wait for opponent move
            game_board.board, turn = client.listen(game_board.board)

        renderer.refresh(clock, screen, game_board.get_board())
                    


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
