import tkinter as tk
import gui.instances.cols as cols

from settings.settings import *

class RootFrame(tk.Frame): 
    def __init__(self, root, width=200, height=200): 
        #cursor.mouse.set_root(self)
        tk.Frame.__init__(self, root, width=width, height=height, background=ROOT_BG) 
        self.__col0 = cols.Col0(self)
        self.__col1 = cols.Col1(self)
        self.__col2 = cols.Col2(self) 
        self.__col3 = cols.Col3(self)

        self.__pack_on_screen()

    def __pack_on_screen(self): 
        # Assemble Parts: 
        # Column 0
        self.__col0.grid(row=0, column=0, padx=COL_PADX, pady=COL_PADY, stick="NSEW")
        # Column 1
        self.__col1.grid(row=0, column=1, padx=COL_PADX, pady=COL_PADY, stick="NSEW")
        # Column 2
        self.__col2.grid(row=0, column=2, padx=COL_PADX, pady=COL_PADY, stick="NSEW")
        # Column 3
        self.__col3.grid(row=0, column=3, padx=COL_PADX, pady=COL_PADY, stick="NSEW")
        
if __name__ == "__main__": 
    pass