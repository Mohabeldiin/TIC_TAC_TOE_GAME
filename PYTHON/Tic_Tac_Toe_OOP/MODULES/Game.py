
import GameUI
class Game():
    """Game class run the Tic Tac Toe game
    """
    def __init__(self) -> None:
        pass
    

    def check_win(): 
        """Check if player win

        Returns:
            bool: True if player win
        """
        # vertical win check
        for col in range(Board.__board_cols):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == PLAYER:
                GameUI.draw_vertical_winning_line(col)
                return True

        # horizontal win check
        for row in range(Board.__board_rows):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == PLAYER:
                GameUI.draw_horizontal_winning_line(row)
                return True

        # diagonal win check
        if self.board[2][0] == self.board[1][1] == self.board[0][2] == PLAYER:
            GameUI.draw_asc_diagonal()
            return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == PLAYER:
            GameUI.draw_desc_diagonal()
            return True

        return False    
    

    def restart():
        """Restart the game
        """
        GameUI.SCREEN.fill(GameUI.BACK_GROUND_COLOR)
        GameUI.draw_lines()
        for row in range(Board.__board_rows):
            for col in range(Board.__board_cols):
                Board.board[row][col] = 0