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


BOARD_SIZE = 8
CELL_SIZE = 650 // BOARD_SIZE
INFO_HEIGHT = 100

GREEN = (0, 150, 0)
DARK_GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Classe Ui
class UI:

    # Initialisation
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.font = pygame.font.SysFont(None, 36)
        self.button_rect = pygame.Rect(500, 25, 130, 40)


    # Gestion des évenements
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Bouton rejouer
            if self.button_rect.collidepoint(x, y):
                self.game.reset()
                return

            # Plateau
            y -= INFO_HEIGHT
            col = x // CELL_SIZE
            row = y // CELL_SIZE

            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                if not self.game.is_game_over():
                    self.game.play_move(row, col)


    # Affichage global
    def draw(self):
        self.screen.fill((50, 50, 50))
        self.draw_info()
        self.draw_board()
        self.draw_valid_moves()
        self.draw_pieces()


    # Header (score + bouton)
    def draw_info(self):
        rect = pygame.Rect(0, 0, 650, INFO_HEIGHT)
        pygame.draw.rect(self.screen, DARK_GREEN, rect)

        black_score, white_score = self.game.get_score()

        player = "Noir" if self.game.current_player == 1 else "Blanc"
        text = f"Noir: {black_score}    Blanc: {white_score}    Tour: {player}"

        img = self.font.render(text, True, WHITE)
        self.screen.blit(img, (20, 35))

        # Bouton rejouer
        pygame.draw.rect(self.screen, (200, 200, 200), self.button_rect)
        pygame.draw.rect(self.screen, BLACK, self.button_rect, 2)

        btn_text = self.font.render("Rejouer", True, BLACK)
        self.screen.blit(btn_text, (self.button_rect.x + 15, self.button_rect.y + 5))

        # Fin du jeu
        if self.game.is_game_over():
            if black_score > white_score:
                winner = "Noir gagne !"
            elif white_score > black_score:
                winner = "Blanc gagne !"
            else:
                winner = "Égalité !"

            end_text = f"FIN DU JEU - {winner}"
            end_img = self.font.render(end_text, True, WHITE)
            self.screen.blit(end_img, (20, 65))


    # Plateau
    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                rect = pygame.Rect(
                    col * CELL_SIZE,
                    row * CELL_SIZE + INFO_HEIGHT,
                    CELL_SIZE,
                    CELL_SIZE)
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)


    # Pions
    def draw_pieces(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                piece = self.game.board[row][col]

                if piece != 0:
                    center = (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2 + INFO_HEIGHT)

                    color = BLACK if piece == 1 else WHITE

                    pygame.draw.circle(
                        self.screen,
                        color,
                        center,
                        CELL_SIZE // 2 - 6)


    # Coups valides
    def draw_valid_moves(self):
        moves = self.game.get_valid_moves()
        color = BLACK if self.game.current_player == 1 else WHITE

        for row, col in moves:
            center = (
                col * CELL_SIZE + CELL_SIZE // 2,
                row * CELL_SIZE + CELL_SIZE // 2 + INFO_HEIGHT)

            pygame.draw.circle(
                self.screen,
                color,
                center,
                8)