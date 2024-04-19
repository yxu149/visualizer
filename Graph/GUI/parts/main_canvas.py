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

        self.__buttonbar_l = ButtonPanel_L(root) 
        self.__buttonbar_s0 = ButtonPanel_S0(root) 
        self.__buttonbar_s1 = ButtonPanel_S1(root) 
        self.__buttonbar_s2 = ButtonPanel_S2(root) 
        self.__buttonbar_s3 = ButtonPanel_S3(root) 
        
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        self.__buttonbar_l.grid(row=1, column=3)
        self.__buttonbar_s0.grid(row=2, column=0)
        self.__buttonbar_s1.grid(row=2, column=1)
        self.__buttonbar_s2.grid(row=2, column=2)
        self.__buttonbar_s3.grid(row=2, column=3)