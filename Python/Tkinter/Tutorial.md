# Tkinter tutorial
from tkinter import * <br />
from tkinter import ttk

## Make and run app
root = Tk() <br />
root.mainloop()

## Make Frame
frame = ttk.Frame(root, padding=10), # padding - внутренний отступ  <br />
frame.grid() #размещение frame
