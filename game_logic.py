class GameLogic:

    def __init__(self):

        self.board = [[0 for _ in range(8)] for _ in range(8)]

        self.board[3][3] = 2
        self.board[3][4] = 1
        self.board[4][3] = 1
        self.board[4][4] = 2

    def play_move(self, row, col):
        print(row,";",col)
