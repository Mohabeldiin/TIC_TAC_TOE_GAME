
from MODULES.Board import Board
class GameUI():
    """GameUI class make UI self.screen of the Tic Tac Toe game
    """
    import pygame
    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    SQUARE_SIZE = 200
    O_RADIUS = 60
    O_WIDTH = 15
    X_WIDTH = 25
    SPACE_FOR_X = 55
    BACK_GROUND_COLOR = (0, 0, 0)
    BACK_GROUND_LINE_COLOR = (111, 111, 111)
    O_COLOR = (254, 132, 255)
    X_COLOR = (219, 88, 136)

    def __init__(self):
        GameUI.pygame.init()
        self.screen = GameUI.pygame.display.set_mode((GameUI.WIDTH, GameUI.HEIGHT))
        GameUI.pygame.display.set_caption('TIC TAC TOE')
        self.screen.fill(GameUI.BACK_GROUND_COLOR)

            
    def draw_lines(self):
        """Draw the self.screen lines
        """
        # horizontal
        GameUI.pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (0, GameUI.SQUARE_SIZE), (GameUI.WIDTH, GameUI.SQUARE_SIZE), GameUI.LINE_WIDTH)
        GameUI.pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (0, 2 * GameUI.SQUARE_SIZE), (GameUI.WIDTH, 2 * GameUI.SQUARE_SIZE), GameUI.LINE_WIDTH)
        # vertical
        GameUI.pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (GameUI.SQUARE_SIZE, 0), (GameUI.SQUARE_SIZE, GameUI.HEIGHT), GameUI.LINE_WIDTH)
        GameUI.pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (2 * GameUI.SQUARE_SIZE, 0), (2 * GameUI.SQUARE_SIZE, GameUI.HEIGHT), GameUI.LINE_WIDTH)


    def draw_figures(self):
        """Draw figure of X or O
        """
        for row in range(Board.get_BOARD()):
            for col in range(Board.get_BOARD()):
                if Board.board[row][col] == 1:
                    GameUI.pygame.draw.circle(self.screen, GameUI.O_COLOR, (int(col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE//2 ), int(row * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE//2 )), GameUI.O_RADIUS, GameUI.O_WIDTH)
                elif Board.board[row][col] == 2:
                    GameUI.pygame.draw.line(self.screen, GameUI.X_COLOR, (col * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE - GameUI.SPACE_FOR_X), (col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE - GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X), GameUI.X_WIDTH)	
                    GameUI.pygame.draw.line(self.screen, GameUI.X_COLOR, (col * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X), (col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE - GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE +GameUI. SQUARE_SIZE - GameUI.SPACE_FOR_X), GameUI.X_WIDTH)


    def SET_COLOR():    
        if Board.get_player() == 1:
            COLOR =  GameUI.O_COLOR
        elif Board.get_player == 2:
            COLOR = GameUI.X_COLOR

        return COLOR


    def draw_vertical_winning_line(self , col):
        """Draw a Vertical Line on the Board used when player win

        Args:
            COL (int):  Number of coulme on board to Draw the line on
        """
        posX = col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE//2
        GameUI.pygame.draw.line(self.screen, GameUI.SET_COLOR(), (posX, 15), (posX, GameUI.HEIGHT - 15), GameUI.LINE_WIDTH)


    def draw_horizontal_winning_line(self, row):
        """Draw a Vertical Line on the Board used when player win

        Args:
            ROW (int): Number of row on board to Draw the line on
        """
        posY = row * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE//2
        GameUI.pygame.draw.line(self.screen, GameUI.SET_COLOR(), (15, posY), (GameUI.WIDTH - 15, posY), GameUI.WIN_LINE_WIDTH)


    def draw_asc_diagonal(self):
        """Draw a ASC Diagonal Line on the Board used when player win
        """
        GameUI.pygame.draw.line(self.screen, GameUI.SET_COLOR(), (15, GameUI.HEIGHT - 15), (GameUI.WIDTH - 15, 15), GameUI.WIN_LINE_WIDTH)


    def draw_desc_diagonal(self):
        """Draw a DESC Diagonal Line on the Board used when player win
        """
        GameUI.pygame.draw.line(self.screen, GameUI.SET_COLOR(), (15, 15), (GameUI.WIDTH - 15, GameUI.HEIGHT - 15), GameUI.WIN_LINE_WIDTH)
