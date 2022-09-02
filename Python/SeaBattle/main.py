import random

import gui
import backend as sb
from functools import partial


class Player:
    def __init__(self, number: int, gamepolegui: gui.GamePoleGui):
        self.gamepolegui = gamepolegui
        self.is_your_turn = False
        self.number = number


class SeaBattle:
    def __init__(self):
        self.gp1 = sb.GamePole(10)
        self.gp2 = sb.GamePole(10)
        self.gui_app = gui.MainWindow()

        #
        self.is_player1_turn = False # random.choice([True, False])

        # configure
        self.gui_app.start_button.bind('<Button-1>', self.start_game,)

        self.gui_app.random_button.configure(command=self.generate_and_draw_ships)
        self.configure_cells(self.gui_app.gamepolegui_player2)
        self.configure_cells(self.gui_app.gamepolegui_player1)

        # disabling game poles
        self.gui_app.gamepolegui_player1.enabled(False)
        self.gui_app.gamepolegui_player2.enabled(False)

        # players
        self.player1 = Player(1, self.gui_app.gamepolegui_player1)
        self.player1 = Player(2, self.gui_app.gamepolegui_player2)

    def configure_cells(self, gamepolegui: gui.GamePoleGui):
        for row_index in range(10):
            for column_index in range(10):
                gamepolegui.cells[row_index][column_index].configure(
                    command=partial(self.cell_pressed, sb.Point(column_index, row_index)))

    def generate_and_draw_ships(self):
        # initializing (generating) game poles
        while True:
            try:
                self.gp1.init()
                self.gp2.init()
                break
            except ValueError:
                pass

        # clearing game poles
        self.gui_app.gamepolegui_player1.clear()
        self.gui_app.gamepolegui_player2.clear()

        # drawing ships for player2 gamepolegui
        for ship in self.gp2.get_ships():
            self.gui_app.gamepolegui_player2.draw_ship(ship)

    def run_app(self):
        self.gui_app.run()

    def who_is_first(self):
        pass

    def start_game(self, event):
        self.gui_app.gamepolegui_player1.enabled(True)

        print('Start button pressed')
        print(event)

    def cell_pressed(self,  point: sb.Point):
        self.hit(point)
        self.move_and_redraw_ships()
        self.change_turn()

    def hit(self, point: sb.Point):
        if self.gui_app.gamepolegui_player1.is_enabled:
            if self.gp1.is_ship_on_point(point):
                self.gui_app.gamepolegui_player1.cells[point.y][point.x].configure(style=gui.STYLES['hitted_cell'])
        else:
            if self.gp2.is_ship_on_point(point):
                self.gui_app.gamepolegui_player2.cells[point.y][point.x].configure(style=gui.STYLES['hitted_cell'])

    def move_and_redraw_ships(self):
        if self.gui_app.gamepolegui_player1.is_enabled:
            self.gp1.move_ships()
        else:
            self.gp2.move_ships()
        

    def change_turn(self):
        if self.gui_app.gamepolegui_player1.is_enabled:
            self.gui_app.gamepolegui_player1.enabled(False)
            self.gui_app.gamepolegui_player2.enabled(True)
        else:
            self.gui_app.gamepolegui_player1.enabled(True)
            self.gui_app.gamepolegui_player2.enabled(False)


if __name__ == "__main__":
    game = SeaBattle()
    game.run_app()
