"""
Projet : Jeu Othello
Auteur : David Vilela & Aleksander Johnson
Date : 09/02/2026
Version : 1.0

Description :
Ce fichier lance le programme. Il initialise pygame,
crée la fenêtre du jeu et gère la boucle principale.
Il relie l'interface graphique (UI) avec la logique du jeu.
"""

import pygame
from ui import UI
from game_logic import GameLogic


WINDOW_WIDTH = 650
WINDOW_HEIGHT = 750
WINDOW_TITLE = "Othello"


#MAIN
def main():
    # Initialisation pygame
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    # Création fenêtre + objets
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game = GameLogic()
    ui = UI(screen, game)
    running = True

    # Boucle principale
    while running:
        # Gestion événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ui.handle_event(event)

        # Affichage
        ui.draw()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()