# MODULES
from MODULES import Board
from MODULES import GameUI
from MODULES import Game
import sys


Game.GameUI.draw_lines()

while True:
    for event in Game.GameUI.pygame.event.get():
        if event.type == Game.GameUI.pygame.pygame.QUIT:
            sys.exit()

        if event.type == Game.GameUI.pygame.pygame.MOUSEBUTTONDOWN and not Game.Game.game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_ROW = int(mouseY // GameUI.SQUARE_SIZE)
            clicked_COL = int(mouseX // GameUI.SQUARE_SIZE)

            if Game.Board.Board.available_square(clicked_ROW, clicked_COL):

                Board.mark_square(clicked_ROW, clicked_COL, Board.get_player())
                if Game.Game.check_win(Board.get_player()):
                    Game.game_over = True
                PLAYER = PLAYER % 2 + 1

                GameUI.draw_figures()
                

        if event.type == GameUI.pygame.KEYDOWN:
            if event.key == GameUI.pygame.K_r:
                Game.restart()
                PLAYER = PLAYER % 2 + 1
                Game.game_over = False

    

    GameUI.pygame.display.update()