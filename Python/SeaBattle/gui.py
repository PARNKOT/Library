import tkinter as tk
from tkinter import ttk
from utils import Point


STYLES = {
    'menu_frame': 'Menu.TFrame',
    'main_frame': 'Main.TFrame',
    'menu_button': 'Menu.TButton',
    'default_cell': 'Cell.TButton',
    'ship_cell': 'ShipCell.TButton',
    'hitted_cell': 'HittedPoint.TButton',
}


class GuiOptions:
    MAINWINDOW_WIDTH = 650
    MAINWINDOW_HEIGHT = 700
    MENU_WIDTH_PERCENT = 0.3

    SHIP_COLOR = 'red'
    HITTEDPOINT_COLOR = 'black'


class NButton(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.propagate(False)
        self.button = ttk.Button(self)
        self.button.pack(expand=1)


def stub(point: Point):
    print(point)


class GamePoleGui(ttk.Frame):
    __slots__ = ['cells', 'is_enabled']

    def __init__(self, master):
        super().__init__(master)

        # Styles
        ttk.Style().configure('GamePole.TFrame', background='#f5f5f5')
        self.configure(style='GamePole.TFrame', padding=5)
        self.cells = [[ttk.Button(self) for _ in range(10)] for _ in range(10)]
        self.is_enabled = False

        self.make_pole()

    def make_pole(self):
        self.clear()

        for row in range(10):
            for column in range(10):
                self.cells[row][column].grid(row=row, column=column, ipady=3)

    def draw_point(self, point: Point):
            self.cells[point.y][point.x].configure(style=STYLES['ship_cell'])

    def draw_ship(self, ship): #ship_points: Iterable):
        for point in ship.get_all_cells_of_ship():
            self.draw_point(point)

#    def update(self):
#        for ship in self.__connected_gamepole.get_ships():
#            self.draw_ship(ship.get_all_cells_of_ship())

    def clear(self):
        for row in self.cells:
            for cell in row:
                cell.configure(width=5, style=STYLES['default_cell'])

    def enabled(self, enabled: bool | None):
        for row in self.cells:
            for cell in row:
                if enabled:
                    cell.configure(state='enabled')
                    self.is_enabled = True
                else:
                    cell.configure(state='disabled')
                    self.is_enabled = False


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # MainWindow
        ttk.Style().theme_use("default")
        self.geometry(f'{GuiOptions.MAINWINDOW_WIDTH}x{GuiOptions.MAINWINDOW_HEIGHT}')
        self.title('SeaBattle')
        self.resizable(True, False)

        # Frames
        self.main_frame = ttk.Frame(self, padding=10)
        self.menu_frame = ttk.Frame(self, padding=10)
        self.menu_frame.propagate(False)
        self.main_frame.propagate(False)

        # Separator
        ttk.Style().configure('Sep.TSeparator', background='black')
        self.separator = ttk.Separator(self, orient=tk.VERTICAL, style='Sep.TSeparator')

        # Buttons
        self.start_button = ttk.Button(self.menu_frame)
        self.random_button = ttk.Button(self.menu_frame)

        # Styles
        ttk.Style().configure('Menu.TFrame', background='green')
        ttk.Style().configure('Main.TFrame', background='#f5f5f5')
        ttk.Style().configure('Menu.TButton')
        ttk.Style().map('Cell.TButton',
                        background=[('!active', 'blue'), ('pressed', 'red'), ('active', 'white')],
                        relief=tk.GROOVE)
        ttk.Style().map('ShipCell.TButton',
                        background=[('!active', GuiOptions.SHIP_COLOR),
                                    ('pressed', GuiOptions.SHIP_COLOR),
                                    ('active', GuiOptions.SHIP_COLOR)],
                        relief=tk.GROOVE)
        ttk.Style().map('HittedPoint.TButton',
                        background=[('!active', GuiOptions.HITTEDPOINT_COLOR),
                                    ('pressed', GuiOptions.HITTEDPOINT_COLOR),
                                    ('active', GuiOptions.HITTEDPOINT_COLOR)],
                        relief=tk.GROOVE)

        # GamePoles
        self.gamepolegui_player1 = GamePoleGui(self.main_frame)
        self.gamepolegui_player2 = GamePoleGui(self.main_frame)

    def init_frames(self):
        # Configuring
        menu_frame_width = GuiOptions.MAINWINDOW_WIDTH * GuiOptions.MENU_WIDTH_PERCENT
        main_frame_width = GuiOptions.MAINWINDOW_WIDTH * (1 - GuiOptions.MENU_WIDTH_PERCENT)
        self.menu_frame.configure(style='Menu.TFrame', width=menu_frame_width)
        self.main_frame.configure(style='Main.TFrame', width=main_frame_width)

        # Packing
        self.menu_frame.pack(side=tk.LEFT, fill='both')
        self.separator.pack(side=tk.LEFT, fill='both')
        self.main_frame.pack(side=tk.LEFT, fill='both')

    def init_buttons(self):
        self.start_button.configure(text='START')
        self.start_button.pack(fill='x', ipady=50, pady=10)
        self.random_button.configure(text='GENERATE SHIPS')
        self.random_button.pack(fill='x', ipady=50, pady=10)

    def init_gamepoles(self):
        self.gamepolegui_player1.pack(side=tk.TOP)
        self.gamepolegui_player2.pack(side=tk.BOTTOM)

    def run(self):
        self.init_frames()
        self.init_buttons()
        self.init_gamepoles()
        self.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()


