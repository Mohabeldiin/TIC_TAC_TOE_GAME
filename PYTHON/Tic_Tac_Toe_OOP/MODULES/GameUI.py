import pygame
import Board
class GameUI():
    """GameUI class make UI self.screen of the Tic Tac Toe game
    """
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
        pygame.init()
        self.screen = pygame.display.set_mode((GameUI.WIDTH, GameUI.HEIGHT))
        pygame.display.set_caption('TIC TAC TOE')
        self.screen.fill(GameUI.BACK_GROUND_COLOR)

            




    def draw_lines(self):
        """Draw the self.screen lines
        """
        # horizontal
        pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (0, GameUI.SQUARE_SIZE), (GameUI.WIDTH, GameUI.SQUARE_SIZE), GameUI.LINE_WIDTH)
        pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (0, 2 * GameUI.SQUARE_SIZE), (GameUI.WIDTH, 2 * GameUI.SQUARE_SIZE), GameUI.LINE_WIDTH)
        # vertical
        pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (GameUI.SQUARE_SIZE, 0), (GameUI.SQUARE_SIZE, GameUI.HEIGHT), GameUI.LINE_WIDTH)
        pygame.draw.line(self.screen, GameUI.BACK_GROUND_LINE_COLOR, (2 * GameUI.SQUARE_SIZE, 0), (2 * GameUI.SQUARE_SIZE, GameUI.HEIGHT), GameUI.LINE_WIDTH)


    def draw_figures(self):
        """Draw figure of X or O
        """
        for row in range(Board.Board.get_BOARD):
            for col in range(Board.Board.get_BOARD):
                if Board.Board.board[row][col] == 1:
                    pygame.draw.circle(self.screen, GameUI.O_COLOR, (int(col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE//2 ), int(row * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE//2 )), GameUI.O_RADIUS, GameUI.O_WIDTH)
                elif Board.Board.board[row][col] == 2:
                    pygame.draw.line(self.screen, GameUI.X_COLOR, (col * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE - GameUI.SPACE_FOR_X), (col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE - GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X), GameUI.X_WIDTH)	
                    pygame.draw.line(self.screen, GameUI.X_COLOR, (col * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE + GameUI.SPACE_FOR_X), (col * GameUI.SQUARE_SIZE + GameUI.SQUARE_SIZE - GameUI.SPACE_FOR_X, row * GameUI.SQUARE_SIZE +GameUI. SQUARE_SIZE - GameUI.SPACE_FOR_X), GameUI.X_WIDTH)

