import tkinter as tk
from tkinter import ttk
from Ship import Ship


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Cockpit")

        container = tk.Frame(self, height=600, width=800)
        container.pack(side="top", fill="both", expand=True)


class Buttons:
    def __init__(self, xcord, ycord, msg, *args, **kwargs):
        self.x = xcord
        self.y = ycord
        self.text = msg

        self.btn = tk.ttk.Button(text=msg)
        self.btn.place(x=xcord, y=ycord)



