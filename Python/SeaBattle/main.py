import gui
import backend as sb


class SeaBattle:
    def __init__(self):
        self.gp1 = sb.GamePole(10)
        self.gp2 = sb.GamePole(10)
        self.gui_app = gui.MainWindow()

        # configure
        self.gui_app.start_button.configure(command=self.start)
        self.gui_app.random_button.configure(command=self.generate_ships)

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


if __name__ == "__main__":
    game = SeaBattle()
    game.open_app()

