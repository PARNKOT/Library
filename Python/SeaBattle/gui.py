import tkinter as tk
from tkinter import ttk
from utils import Point
from functools import partial


class GuiOptions:
    MAINWINDOW_WIDTH = 650
    MAINWINDOW_HEIGHT = 700
    MENU_WIDTH_PERCENT = 0.3


class NButton(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.propagate(False)
        self.button = ttk.Button(self)
        self.button.pack(expand=1)


def stub(point: Point):
    print(point)


class GamePoleGui(ttk.Frame):
    __slots__ = ['cells']

    def __init__(self, master):
        super().__init__(master)

        # Styles
        ttk.Style().configure('GamePole.TFrame', background='blue')
        ttk.Style().map('Cell.TButton', background=[('!active', 'blue'), ('pressed', 'red'), ('active', 'white')])

        self.configure(style='GamePole.TFrame', padding=5)
        self.cells = [[ttk.Button(self) for _ in range(10)] for _ in range(10)]

        self.make_pole()
        self.configure_cells()

    def make_pole(self):
        for row in self.cells:
            for cell in row:
                cell.configure(width=5, style='Cell.TButton')

        for row in range(10):
            for column in range(10):
                self.cells[row][column].grid(row=row, column=column, ipady=3)

    def configure_cells(self):
        for row_index in range(10):
            for column_index in range(10):
                self.cells[row_index][column_index].configure(command=partial(stub, Point(column_index, row_index)))


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

        # Styles
        ttk.Style().configure('Menu.TFrame', background='green')
        ttk.Style().configure('Main.TFrame', background='#f5f5f5')
        ttk.Style().configure('Menu.TButton')

        # GamePoles
        self.gamepole_player1 = GamePoleGui(self.main_frame)
        self.gamepole_player2 = GamePoleGui(self.main_frame)

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

    @staticmethod
    def func(e):
        print(e)

    def init_buttons(self):
        self.start_button.configure(text='START')
        self.start_button.pack(fill='x', ipady=50, pady=10)

    def init_gamepoles(self):
        self.gamepole_player1.pack(side=tk.TOP)
        self.gamepole_player2.pack(side=tk.BOTTOM)

    def run(self):
        self.init_frames()
        self.init_buttons()
        self.init_gamepoles()
        self.mainloop()


def func(e):
    print(e)


if __name__ == "__main__":
    app = MainWindow()
    app.run()


