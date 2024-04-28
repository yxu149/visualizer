import tkinter as tk 
import tkinter.constants as constants
import tkinter.messagebox as messagebox 
import gui.wiring.element_ctrl as element_ctrl 
import settings.settings as settings

class Stage(tk.Frame): 
    def __init__(self, root, width=settings.w1, height=settings.h2,\
                 event_root=None, onselect=None, onrelease=None): 
        self.__root = root 
        tk.Frame.__init__(self, root) 
        self.__node_count = 0 
        self.h_scrollbar = tk.Scrollbar(self, orient=constants.HORIZONTAL)
        self.v_scrollbar = tk.Scrollbar(self, orient=constants.VERTICAL) 

        self.__stage = tk.Canvas(self, bg=settings.STAGE_BG_COLOR)