# MODULES
from MODULES.Board import Board
from MODULES.GameUI import GameUI
from MODULES.Game import Game
import sys 

gameui = GameUI() 
gameui.draw_lines()

while True:
    for event in gameui.pygame.event.get():
        if event.type == gameui.pygame.QUIT:
            sys.exit()

        if event.type == gameui.pygame.MOUSEBUTTONDOWN and not Game.game_over:

            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            clicked_ROW = int(mouseY // gameui.SQUARE_SIZE)
            clicked_COL = int(mouseX // gameui.SQUARE_SIZE)

            if Board.available_square(clicked_ROW, clicked_COL):

                Board.mark_square(clicked_ROW, clicked_COL, Board.get_player())
                if Game.check_win():
                    Game.game_over = True
                Board.set_player(Board.get_player() % 2 + 1)

                gameui.draw_figures()
                

        if event.type == gameui.pygame.KEYDOWN:
            if event.key == gameui.pygame.K_r:
                Game.restart()
                Board.set_player(Board.get_player % 2 + 1)
                Game.game_over = False

    

    gameui.pygame.display.update()