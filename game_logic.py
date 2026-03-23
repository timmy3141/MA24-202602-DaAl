"""
Projet : Jeu Othello
Auteur : David Vilela & Aleksander Johnson
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

BOARD_SIZE = 8
EMPTY = 0
BLACK = 1
WHITE = 2

# Directions possibles autour d'une case
DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

# Classe principale
class GameLogic:
    # Initialisation du plateau et du joueur
    def __init__(self):
        self.reset()

# ---- Gestion du jeu ----
    # Joue un coup si valide
    def play_move(self, row, col):
        if (row, col) in self.get_valid_moves():
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.switch_player()

            # Passe le tour si aucun coup possible
            if not self.get_valid_moves():
                self.switch_player()

    # Change le joueur
    def switch_player(self):
        self.current_player = WHITE if self.current_player == BLACK else BLACK

    # Réinitialise la partie
    def reset(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.board[3][3] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[4][4] = WHITE
        self.current_player = BLACK


    # Liste des coups possibles
    def get_valid_moves(self):
        valid_moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == EMPTY and self.can_flip(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    # Vérifie si un coup capture des pions
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

    # Vérifie si le jeu est terminé
    def is_game_over(self):
        current = self.current_player

        if self.get_valid_moves():
            return False
        self.switch_player()
        if self.get_valid_moves():
            self.current_player = current
            return False

        self.current_player = current
        return True

    # Calcule le score
    def get_score(self):
        black_score = sum(row.count(BLACK) for row in self.board)
        white_score = sum(row.count(WHITE) for row in self.board)

        return black_score, white_score