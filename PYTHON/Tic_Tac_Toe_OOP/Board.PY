import numpy as np
class Board():
    """Board class make a board for Tic Tac Toe game
    """
    __BOARD:(int) = 3
    __player:(int) = 2


    def __init__(self):
        """Make numpy 2D array with default value zero, 
        this 2D array simulate the board
        """
        self.board = np.zeros((Board.__BOARD, Board.__BOARD))

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


    def is_full(self):
        """Check if there is free square on the board

        Returns:
            bool: True if there is no free square on the board
        """
        for row in range(Board.__BOARD):
            for col in range(Board.__BOARD):
                if self.board[row][col] == 0:
                    return False

        return True


    def available_square(self, row:int, col:int):
        """Check if player can play in this square

        Args:
            row (int): number of a square on Y-axiis
            col (int): number of a square on X-axiis

        Returns:
            bool: True if sqyare is available for player to play in
        """
        return self.board[row][col] == 0


    def mark_square(self, row, col):
        """Set value for square on the board

        Args:
            row (int): number of a square on Y-axiis
            col (int): number of a square on X-axiis
        """
        self.board[row][col] = Board.__player


