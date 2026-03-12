BOARD_SIZE = 8
EMPTY = 0
BLACK = 1
WHITE = 2

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


class GameLogic:

    def __init__(self):
        # plateau 8x8
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        # 4 pions de départ
        self.board[3][3] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK
        self.board[4][4] = WHITE

        # joueur courant (BLACK commence)
        self.current_player = BLACK

    def play_move(self, row, col):
        """Jouer un coup si valide et retourner les pions adverses"""
        if (row, col) in self.get_valid_moves():
            self.board[row][col] = self.current_player
            self.flip_pieces(row, col)
            self.switch_player()
        else:
            print("Coup invalide !")

    def switch_player(self):
        self.current_player = WHITE if self.current_player == BLACK else BLACK

    def get_valid_moves(self):
        """Retourne la liste des coups valides pour le joueur courant"""
        valid_moves = []
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] == EMPTY and self.can_flip(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def can_flip(self, row, col):
        """Vérifie si placer un pion ici retourne au moins un pion adverse"""
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

    def flip_pieces(self, row, col):
        """Retourne tous les pions adverses capturés par ce coup"""
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

    def is_game_over(self):
        """Vérifie si la partie est terminée"""
        if self.get_valid_moves():
            return False
        self.switch_player()
        if self.get_valid_moves():
            self.switch_player()
            return False
        return True

    def get_score(self):
        """Retourne le score sous forme (noirs, blancs)"""
        black_score = sum(row.count(BLACK) for row in self.board)
        white_score = sum(row.count(WHITE) for row in self.board)
        return black_score, white_score