import pygame
from ui import UI
from game_logic import GameLogic

pygame.display.set_caption("Othello")

def main():
    pygame.init()

    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 640
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    game = GameLogic()
    ui = UI(screen, game)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            ui.handle_event(event)

        ui.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
