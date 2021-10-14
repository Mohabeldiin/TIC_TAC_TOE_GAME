# MODULES
import pygame
import sys
import numpy as np
pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
O_RADIUS = 60
O_WIDTH = 15
X_WIDTH = 25
SPACE_FOR_X = 55
BACK_GROUND_COLOR = (0, 0, 0)
BACK_GROUND_LINE_COLOR = (111, 111, 111)
O_COLOR = (254, 132, 255)
X_COLOR = (219, 88, 136)
PLAYER = 2
GAME_OVER = False
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
SCREEN.fill(BACK_GROUND_COLOR)
BOARD = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    """Draw the Board lines
    """
    # horizontal
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # vertical
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(SCREEN, BACK_GROUND_LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    """Draw the shap of X or O based on Player turn
    """
    for ROW in range(BOARD_ROWS):
        for COL in range(BOARD_COLS):
            if BOARD[ROW][COL] == 1:
                pygame.draw.circle(SCREEN, O_COLOR, (int(COL * SQUARE_SIZE + SQUARE_SIZE//2 ), int(ROW * SQUARE_SIZE + SQUARE_SIZE//2 )), O_RADIUS, O_WIDTH)
            elif BOARD[ROW][COL] == 2:
                pygame.draw.line(SCREEN, X_COLOR, (COL * SQUARE_SIZE + SPACE_FOR_X, ROW * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X), (COL * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X, ROW * SQUARE_SIZE + SPACE_FOR_X), X_WIDTH)	
                pygame.draw.line(SCREEN, X_COLOR, (COL * SQUARE_SIZE + SPACE_FOR_X, ROW * SQUARE_SIZE + SPACE_FOR_X), (COL * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X, ROW * SQUARE_SIZE + SQUARE_SIZE - SPACE_FOR_X), X_WIDTH)


def mark_square(ROW, COL, PLAYER):
    """Set Square as not free for players to play in

    Args:
        ROW (int): Number of the Square on the Y-axies 
        COL (int): Number of the Square On the X-axies
        PLAYER (int): the Player that make the move
    """
    BOARD[ROW][COL] = PLAYER


def available_square(ROW, COL):
    """Check the Square Availablty for playing

    Args:
        ROW (int): Number of the Square On the Y-axies
        COL (int): Number of the Square On the X-axies

    Returns:
        bool: True if the Square is Available (==0)
    """
    return BOARD[ROW][COL] == 0


def is_BOARD_full():
    """Chech if All Board Squares are full

    Returns:
        bool: True if All board Squares are full
    """
    for ROW in range(BOARD_ROWS):
        for COL in range(BOARD_COLS):
            if BOARD[ROW][COL] == 0:
                return False

    return True

def check_win(PLAYER):
    """Check if a player have win and Draw a line on the wining Squares

    Args:
        PLAYER (int): Number of the player

    Returns:
        bool: True if a player have win
    """
    # vertical win check
    for COL in range(BOARD_COLS):
        if BOARD[0][COL] == BOARD[1][COL] == BOARD[2][COL] == PLAYER:
            draw_vertical_winning_line(COL)
            return True

    # horizontal win check
    for ROW in range(BOARD_ROWS):
        if BOARD[ROW][0] == BOARD[ROW][1] == BOARD[ROW][2] == PLAYER:
            draw_horizontal_winning_line(ROW)
            return True

    # diagonal win check
    if BOARD[2][0] == BOARD[1][1] == BOARD[0][2] == PLAYER:
        draw_asc_diagonal()
        return True
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] == PLAYER:
        draw_desc_diagonal()
        return True

    return False


def SET_COLOR():
    """Set Color of shapes based on player turn

    Returns:
        tuple: a tuple contane the HEX of the player color
    """
    if PLAYER == 1:
        COLOR = O_COLOR
    elif PLAYER == 2:
        COLOR = X_COLOR

    return COLOR


def draw_vertical_winning_line(COL):
    """Draw a Vertical Line on the Board used when player win

    Args:
        COL (int):  Number of coulme on board to Draw the line on
    """
    posX = COL * SQUARE_SIZE + SQUARE_SIZE//2
    pygame.draw.line(SCREEN, SET_COLOR(), (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_winning_line(ROW):
    """Draw a Vertical Line on the Board used when player win

    Args:
        ROW (int): Number of row on board to Draw the line on
    """
    posY = ROW * SQUARE_SIZE + SQUARE_SIZE//2
    pygame.draw.line(SCREEN, SET_COLOR(), (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_asc_diagonal():
    """Draw a ASC Diagonal Line on the Board used when player win
    """
    pygame.draw.line(SCREEN, SET_COLOR(), (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal():
    """Draw a DESC Diagonal Line on the Board used when player win
    """
    pygame.draw.line(SCREEN, SET_COLOR(), (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)


def restart():
    """Restart the game by seting all voard squares as avalibale to play and 
    """
    SCREEN.fill(BACK_GROUND_COLOR)
    draw_lines()
    for ROW in range(BOARD_ROWS):
        for COL in range(BOARD_COLS):
            BOARD[ROW][COL] = 0


draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_ROW = int(mouseY // SQUARE_SIZE)
            clicked_COL = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_ROW, clicked_COL):

                mark_square(clicked_ROW, clicked_COL, PLAYER)
                if check_win(PLAYER):
                    GAME_OVER = True
                PLAYER = PLAYER % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                PLAYER = PLAYER % 2 + 1
                GAME_OVER = False

    pygame.display.update()