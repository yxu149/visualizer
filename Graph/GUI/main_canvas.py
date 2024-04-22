import sys
from tkinter import Misc

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

from gui.parts.buttonbar_l import * 
from gui.parts.buttonbar_s0 import * 
from gui.parts.buttonbar_s1 import * 
from gui.parts.buttonbar_s2 import * 
from gui.parts.buttonbar_s3 import * 

class MainCanvas(Frame): 
    def __init__(self, root, width=200, height=200): 
        self.width = width
        self.height = height
        Frame.__init__(self, root, width=width, height=height)
        # cursor 
        
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        pass