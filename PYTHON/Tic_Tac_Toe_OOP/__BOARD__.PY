import numpy as np

class Board():
    """Board class make a board for Tic Tac Toe game
    """
    board_rows = 3
    board_cols = 3
    player = 2


    def __init__(self):
        """Make numpy 2D array with default value zero, 
        this 2D array simulate the board
        """
        self.board = np.zeros((Board.board_rows, Board.board_cols))


    def is_full(self)->bool:
        for row in range(Board.board_rows):
            for col in range(Board.board_cols):
                if self.BOARD[row][col] == 0:
                    return False

        return True


    def available_square(self, row:int, col:int)->bool:
        return self.board[row][col] == 0


    def mark_square(self, row, col, player):
        """Set value for square on the board

        Args:
            row (int): number of a square on Y-axiis
            col (int): number of a square on X-axiis
            player (int): player 1 for X and 2 for O
        """
        self.board[row][col] = player


    