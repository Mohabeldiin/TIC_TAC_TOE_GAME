import numpy as np

class _BOARD_():

    BOARD_ROWS = 3
    BOARD_COLS = 3


    def __init__(self):
        self.BOARD_COLS = 3
        self.BOARD_ROWS = 3
        self.BOARD = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))


    def is_BOARD_full(self):
        for ROW in range(self.BOARD_ROWS):
            for COL in range(self.BOARD_COLS):
                if self.BOARD[ROW][COL] == 0:
                    return False

        return True