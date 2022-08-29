import gui
import SeaBattle as sb


class SeaBattle:
    def __init__(self):
        self.gp1 = sb.GamePole(10)
        self.gp2 = sb.GamePole(10)
        self.gui_app = gui.MainWindow()
        self.connect_poles_with_gui()

    def connect_poles_with_gui(self):
        self.gui_app.gamepole_player1.connect(self.gp1)
        self.gui_app.gamepole_player2.connect(self.gp2)

    def play(self):
        self.gp2.init()
        self.gui_app.gamepole_player2.update()
        self.gui_app.run()


if __name__ == "__main__":
    game = SeaBattle()
    game.play()

