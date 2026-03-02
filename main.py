import pygame
from ui import UI
from game_logic import GameLogic


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))

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