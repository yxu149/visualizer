import sys 
from gui.screens import std_screen
import settings

sys.path.append(settings.BASE_DIR)

import tkinter as tk 
from gui.canvas import canvas
from gui.panels import panels, media_ctrl, pen_ctrl, io_ctrl, extra_ctrl
from gui.screens import std_screen, usr_screen
from gui.cursor import mouse

class MainCanvas(tk.Frame): 
    """
    Params: tk widght

    Main GUI Assembler
    """
    def __init__(self, root, width=200, height=200): 
        self.width = width 
        self.height = height 

        tk.Frame.__init__(self, root, width=width, height=height) 

        self.__cursor = mouse.CursorState()
        self.__cursor.set_root(self)

        self.__canvas = canvas.Sketchpad(\
            self, event_root=root, \
            onselect=self.__on_element_selection, \
            onrelease=self.__on_element_release)
        self.__std_screen = std_screen.StdScreen(self)
        self.__pen_ctrl = panels.PenCtrl(self)
        self.__buttons 