import pygame
import Board
class GameUI():
    """GameUI class make UI screen of the Tic Tac Toe game
    """

    def __init__(self):
        pygame.init()
        Board

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

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
SCREEN.fill(BACK_GROUND_COLOR)


def draw_lines():
    """Draw the screen lines
    """
    # horizontal
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # vertical
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    """[summary]
    """
    for ROW in range(Board. BOARD_ROWS):
        for COL in range(BOARD_COLS):
            if BOARD[ROW][COL] == 1:
                pygame.draw.circle(SCREEN, O_COLOR, (int(COL * SQUARE_SIZE + SQUARE_SIZE//2 ), int(ROW * SQUARE_SIZE + SQUARE_SIZE//2 )), O_RADIUS, O_WIDTH)
            elif BOARD[ROW][COL] == 2:
                pygame.draw.line(SCREEN, X_COLOR, (COL * SQUARE_SIZE + SPACE_FOR_X, ROW * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X), (COL * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X, ROW * SQUARE_SIZE + SPACE_FOR_X), X_WIDTH)	
                pygame.draw.line(SCREEN, X_COLOR, (COL * SQUARE_SIZE + SPACE_FOR_X, ROW * SQUARE_SIZE + SPACE_FOR_X), (COL * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X, ROW * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X), X_WIDTH)

