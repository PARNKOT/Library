import tkinter as tk
from tkinter import ttk


class GuiOptions:
    MAINWINDOW_WIDTH = 1000
    MAINWINDOW_HEIGHT = 700
    MENU_WIDTH_PERCENT = 0.2


class NButton(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.propagate(False)
        self.button = ttk.Button(self)
        self.button.pack(expand=1)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # MainWindow
        self.geometry(f'{GuiOptions.MAINWINDOW_WIDTH}x{GuiOptions.MAINWINDOW_HEIGHT}')

        # Frames
        self.main_frame = ttk.Frame(self, padding=10)
        self.menu_frame = ttk.Frame(self, padding=10)
        self.menu_frame.propagate(False)

        # Buttons
        #self.start_button = NButton(self.menu_frame)
        self.start_button = ttk.Button(self.menu_frame)

        # Styles
        ttk.Style().configure('Menu.TFrame', background='green')
        ttk.Style().configure('Main.TFrame', background='#f5f5f5')
        ttk.Style().configure('Menu.TButton')

    def init_frames(self):
        # Configuring
        menu_frame_width = GuiOptions.MAINWINDOW_WIDTH * GuiOptions.MENU_WIDTH_PERCENT
        main_frame_width = GuiOptions.MAINWINDOW_WIDTH * (1 - GuiOptions.MENU_WIDTH_PERCENT)
        self.menu_frame.configure(style='Menu.TFrame', width=menu_frame_width)
        self.main_frame.configure(style='Main.TFrame', width=main_frame_width)

        # Packing
        self.menu_frame.pack(side=tk.LEFT, fill='both')
        self.main_frame.pack(side=tk.LEFT, fill='both')

    def init_buttons(self):
        self.start_button.configure(text='START')
        self.start_button.pack(fill='x')


    def run(self):
        self.init_frames()
        self.init_buttons()
        self.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()


