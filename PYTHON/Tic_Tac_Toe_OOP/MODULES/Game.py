import Board
import GameUI
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
        for col in range(Board.Board.get_BOARD()):
            if Board.Board.board[0][col] == Board.Board.board[1][col] == Board.Board.board[2][col] == Board.Board.get_player():
                GameUI.draw_vertical_winning_line(col)
                return True

        # horizontal win check
        for row in range(Board.Board.get_BOARD()):
            if Board.Board.board[row][0] == Board.Board.board[row][1] == Board.Board.board[row][2] == Board.Board.get_player():
                GameUI.draw_horizontal_winning_line(row)
                return True

        # diagonal win check
        if Board.Board.board[2][0] == Board.Board.board[1][1] == Board.Board.board[0][2] == Board.Board.get_player():
            GameUI.draw_asc_diagonal()
            return True
        if Board.Board.board[0][0] == Board.Board.board[1][1] == Board.Board.board[2][2] == Board.Board.get_player():
            GameUI.draw_desc_diagonal()
            return True

        return False    
    

    def restart():
        """Restart the game
        """
        GameUI.SCREEN.fill(GameUI.BACK_GROUND_COLOR)
        GameUI.draw_lines()
        for row in range(Board.Board.get_BOARD()):
            for col in range(Board.Board.get_BOARD()):
                Board.Board.board[row][col] = 0


    def SET_COLOR():    
        if Board.Board.get_player() == 1:
            COLOR =  GameUI.GameUI.O_COLOR
        elif Board.Board.get_player == 2:
            COLOR = GameUI.GameUI.X_COLOR

        return COLOR