import numpy as np

class Board():
    """Board class make a board for Tic Tac Toe game
    """
    __board_rows:(int) = 3
    __board_cols:(int) = 3
    __player:(int) = 2


    def __init__(self):
        """Make numpy 2D array with default value zero, 
        this 2D array simulate the board
        """
        self.board = np.zeros((Board.__board_rows, Board.__board_cols))

    @classmethod
    def set_player(cls, player):
        """Set Board class player

        Args:
            player (int): player 1 for X and 2 for O
        """
        cls.__player = player

    @classmethod
    def get_player(cls):
        """Get Board class player

        Returns:
            int: 1 for X and 2 for O
        """
        return cls.__player;


    def is_full(self)->bool:
        for row in range(Board.board_rows):
            for col in range(Board.board_cols):
                if self.BOARD[row][col] == 0:
                    return False

        return True


    def available_square(self, row:int, col:int)->bool:
        return self.board[row][col] == 0


    def mark_square(self, row, col):
        """Set value for square on the board

        Args:
            row (int): number of a square on Y-axiis
            col (int): number of a square on X-axiis
        """
        self.board[row][col] = Board.__player


    