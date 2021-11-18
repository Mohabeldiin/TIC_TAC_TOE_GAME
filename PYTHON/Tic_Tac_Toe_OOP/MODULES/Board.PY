import numpy
class Board():
    """Board class make a board for Tic Tac Toe game
    """
    BOARD_OX = 3
    playerXO = 2
    board = numpy.zeros((BOARD_OX, BOARD_OX))


    def __init__(self):
        """Make numpy 2D array with default value zero, 
        this 2D array simulate the board
        """

    
    def set_player(player):
        """Set Board class player

        Args:
            player (int): player 1 for X and 2 for O
        """
        Board.playerXO = player

    @classmethod
    def get_player(cls):
        """Get Board class player

        Returns:
            int: 1 for X and 2 for O
        """
        return cls.playerXO;


    
    def get_BOARD():
        """Get Board class BOARD

        Returns:
            int: BOARD rows or cols
        """
        return Board.BOARD_OX


    @classmethod
    def is_full(cls):
        """Check if there is free square on the board

        Returns:
            bool: True if there is no free square on the board
        """
        for row in range(Board.BOARD_OX):
            for col in range(Board.BOARD_OX):
                if cls.board[row][col] == 0:
                    return False

        return True


    @classmethod
    def available_square(cls, row:int, col:int):
        """Check if player can play in this square

        Args:
            row (int): number of a square on Y-axiis
            col (int): number of a square on X-axiis

        Returns:
            bool: True if sqyare is available for player to play in
        """
        return cls.board[row][col] == 0


    def mark_square(row:int, col:int,player ):
        """Set value for square on the board

        Args:
            row (int): number of a square on Y-axiis
            col (int): number of a square on X-axiis
        """
        Board.board[row][col] = player
