from MODULES.Board import Board
from MODULES.GameUI import GameUI
class Game():
    """Game class run the Tic Tac Toe game
    """
    game_over = False

    def check_win(): 
        """Check if player win

        Returns:
            bool: True if player win
        """
        # vertical win check
        for col in range(Board.get_BOARD()):
            if Board.board[0][col] == Board.board[1][col] == Board.board[2][col] == Board.get_player():
                GameUI.draw_vertical_winning_line(col)
                return True

        # horizontal win check
        for row in range(Board.get_BOARD()):
            if Board.board[row][0] == Board.board[row][1] == Board.board[row][2] == Board.get_player():
                GameUI.draw_horizontal_winning_line(row)
                return True

        # diagonal win check
        if Board.board[2][0] == Board.board[1][1] == Board.board[0][2] == Board.get_player():
            GameUI.draw_asc_diagonal()
            return True
        if Board.board[0][0] == Board.board[1][1] == Board.board[2][2] == Board.get_player():
            GameUI.draw_desc_diagonal()
            return True

        return False    
    

    def restart():
        """Restart the game
        """
        GameUI.screen.fill(GameUI.BACK_GROUND_COLOR)
        GameUI.draw_lines()
        for row in range(Board.get_BOARD()):
            for col in range(Board.get_BOARD()):
                Board.board[row][col] = 0
