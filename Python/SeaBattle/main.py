import gui
import backend as sb
from functools import partial


class SeaBattle:
    def __init__(self):
        self.gp1 = sb.GamePole(10)
        self.gp2 = sb.GamePole(10)
        self.gui_app = gui.MainWindow()

        # configure
        self.gui_app.start_button.configure(command=self.start)
        self.gui_app.random_button.configure(command=self.generate_ships)
        self.define_cells_action(self.gui_app.gamepolegui_player2)
        self.define_cells_action(self.gui_app.gamepolegui_player1)

    def define_cells_action(self, gamepolegui: gui.GamePoleGui):
        for row_index in range(10):
            for column_index in range(10):
                gamepolegui.cells[row_index][column_index].configure(
                    command=partial(self.hit, sb.Point(column_index, row_index)))

    def generate_ships(self):
        self.gui_app.gamepolegui_player2.clear()

        while True:
            try:
                self.gp2.init()
                break
            except ValueError:
                pass
        for ship in self.gp2.get_ships():
            self.gui_app.gamepolegui_player2.draw_ship(ship)

    def start(self):
        pass

    def open_app(self):
        self.gui_app.run()

    def hit(self, point: sb.Point):
        if self.gp2.is_ship_on_point(point):
            self.gui_app.gamepolegui_player2.cells[point.y][point.x].configure(style=gui.STYLES['hitted_cell'])



if __name__ == "__main__":
    game = SeaBattle()
    game.open_app()

