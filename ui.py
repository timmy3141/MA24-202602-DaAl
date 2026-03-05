import pygame

BOARD_SIZE = 8
CELL_SIZE = 80
WINDOW_WIDTH = BOARD_SIZE * CELL_SIZE
WINDOW_HEIGHT = BOARD_SIZE * CELL_SIZE

GREEN = (0, 150, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class UI:

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            col = x // CELL_SIZE
            row = y // CELL_SIZE

            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                self.game.play_move(row, col)

    def draw(self):
        self.screen.fill((50, 50, 50))
        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                rect = pygame.Rect(
                    col * CELL_SIZE,
                    row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(self.screen, GREEN, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw_pieces(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                piece = self.game.board[row][col]
                if piece != 0:
                    center = (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    )
                    color = BLACK if piece == 1 else WHITE
                    pygame.draw.circle(
                        self.screen,
                        color,
                        center,
                        CELL_SIZE // 2 - 5
                    )
