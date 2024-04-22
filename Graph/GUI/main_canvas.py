import tkinter as tk
from settings.settings import *
from wiring import l0, s0, s1, s2, s3
from modules import columns, panel6, panel8

class MainCanvas(tk.Frame): 
    def __init__(self, root, width=200, height=200): 
        self.width = width
        self.height = height
        tk.Frame.__init__(self, root, width=width, height=height)
        # cursor 
        
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        pass