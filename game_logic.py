"""
Projet : Jeu Othello
Auteur : David Vilela & Aleksender Johnson
Date : 09/02/2026
Version : 1.0

Description :
Ce fichier contient toute la logique du jeu :
- création et gestion du plateau
- vérification des coups valides
- retournement des pions
- gestion des joueurs
- calcul du score et fin de partie
"""

# Constantes du jeu
BOARD_SIZE = 8
EMPTY = 0
BLACK = 1
WHITE = 2

# Les 8 directions possibles autour d'une case
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

class GameLogic:

    # Création du plateau 8x8 vide
    def __init__(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        # Placement des 4 pions de depart
        self.board[3][3] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[4][4] = WHITE
        # Le joueur noir
        self.current_player = BLACK

    #Joue un coup si valide
    def play_move(self, row, col):
        if (row, col) in self.get_valid_moves():
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.switch_player()

    # Change le joueur actuel
    def switch_player(self):
        self.current_player = WHITE if self.current_player == BLACK else BLACK

    # Retourne toutes les cases où le joueur peut jouer
    def get_valid_moves(self):
        valid_moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == EMPTY and self.can_flip(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    # Vérifie si un coup permet de capturer des pions adverses
    def can_flip(self, row, col):
        opponent = WHITE if self.current_player == BLACK else BLACK

        for dr, dc in DIRECTIONS:
            r, c = row + dr, col + dc
            found_opponent = False

            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                if self.board[r][c] == opponent:
                    found_opponent = True
                elif self.board[r][c] == self.current_player:
                    if found_opponent:
                        return True
                    break
                else:
                    break

                r += dr
                c += dc

        return False

    # Retourne les pions capturés
    def flip_pieces(self, row, col):
        opponent = WHITE if self.current_player == BLACK else BLACK

        for dr, dc in DIRECTIONS:
            pieces_to_flip = []
            r, c = row + dr, col + dc

            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                if self.board[r][c] == opponent:
                    pieces_to_flip.append((r, c))
                elif self.board[r][c] == self.current_player:
                    for pr, pc in pieces_to_flip:
                        self.board[pr][pc] = self.current_player
                    break
                else:
                    break

                r += dr
                c += dc

    # Vérifie si aucun joueur ne peut jouer
    def is_game_over(self):
        if self.get_valid_moves():
            return False

        self.switch_player()

        if self.get_valid_moves():
            self.switch_player()
            return False

        return True

    # Compte le nombre de pions noirs et blancs
    def get_score(self):
        black_score = sum(row.count(BLACK) for row in self.board)
        white_score = sum(row.count(WHITE) for row in self.board)

        return black_score, white_score