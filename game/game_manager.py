import pygame

def menu(screen):
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.Font(None, 40)
    title_font = pygame.font.Font(None, 60)

    options = ["Solo", "AI", "LAN"]
    selected = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected]

        screen.fill((0, 0, 0))

        title = title_font.render("Tic Tac Toe", True, (255, 255, 255))
        screen.blit(title, (100, 50))

        # Draw options
        y_offset = 150
        for i, option in enumerate(options):
            color = (255, 255, 255) if i != selected else (255, 200, 0)
            text = font.render(option, True, color)
            screen.blit(text, (140, y_offset))
            y_offset += 50

        pygame.display.update()
        clock.tick(30)


def show_end_screen(screen, clock, winner_name):
    pygame.font.init()
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 32)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "restart"
                if event.key == pygame.K_ESCAPE:
                    return "quit"

        # We do NOT clear the screen — board stays visible
        # Simply draw text overlay
        text = font.render(f"{winner_name} Wins!", True, (255, 255, 0))
        sub = small_font.render("Press ENTER to play again", True, (255, 255, 255))

        screen.blit(text, (125, 20))
        screen.blit(sub, (50, 300))

        pygame.display.update()
        clock.tick(30)