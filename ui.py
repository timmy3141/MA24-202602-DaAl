"""
Projet : Jeu Othello
Auteur : David Vilela & Aleksander Johnson
Date : 09/02/2026
Version : 1.0

Description :
Ce fichier gère l'interface graphique du jeu avec pygame.
Il s'occupe de :
- dessiner le plateau
- afficher les pions
- afficher le score et le joueur courant
- détecter les clics du joueur
"""

import pygame

# Taille du plateau et de l'interface
BOARD_SIZE = 8
CELL_SIZE = 650 // BOARD_SIZE
INFO_HEIGHT = 100

# Couleurs utilisées dans le jeu
GREEN = (0, 150, 0)
DARK_GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class UI:

    # Réference à l'ecran et à la logique du jeu
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont(None, 36)

    # Gère les clics de souris sur le plateau
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            y -= INFO_HEIGHT
            col = x // CELL_SIZE
            row = y // CELL_SIZE

            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                self.game.play_move(row, col)

    # Dessine tous les éléments du jeu
    def draw(self):
        self.screen.fill((50, 50, 50))
        self.draw_info()
        self.draw_board()
        self.draw_valid_moves()
        self.draw_pieces()

    # Zone d'information avec le score et le joueur courant
    def draw_info(self):
        rect = pygame.Rect(0, 0, 650, INFO_HEIGHT)
        pygame.draw.rect(self.screen, DARK_GREEN, rect)

        black_score, white_score = self.game.get_score()

        player = "Noir" if self.game.current_player == 1 else "Blanc"
        text = f"Noir: {black_score}    Blanc: {white_score}    Tour: {player}"

        img = self.font.render(text, True, WHITE)
        self.screen.blit(img, (20, 35))

    # Affichage de la grille du plateau
    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                rect = pygame.Rect(
                    col * CELL_SIZE,
                    row * CELL_SIZE + INFO_HEIGHT,
                    CELL_SIZE,
                    CELL_SIZE
                )

                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    # Affichage des pions présents sur le plateau
    def draw_pieces(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                piece = self.game.board[row][col]

                if piece != 0:

                    center = (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2 + INFO_HEIGHT
                    )

                    color = BLACK if piece == 1 else WHITE

                    pygame.draw.circle(
                        self.screen,
                        color,
                        center,
                        CELL_SIZE // 2 - 6
                    )

    # Affichage des coups valides pour le joueur courant
    def draw_valid_moves(self):
        moves = self.game.get_valid_moves()

        color = BLACK if self.game.current_player == 1 else WHITE

        for row, col in moves:

            center = (
                col * CELL_SIZE + CELL_SIZE // 2,
                row * CELL_SIZE + CELL_SIZE // 2 + INFO_HEIGHT
            )

            pygame.draw.circle(
                self.screen,
                color,
                center,
                8
            )