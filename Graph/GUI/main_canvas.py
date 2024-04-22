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

        self.__vline_1 = Separator(root, orient=VERTICAL)
        self.__vline_2 = Separator(root, orient=VERTICAL)
        self.__vline_3 = Separator(root, orient=VERTICAL)
        self.__vline_4 = Separator(root, orient=VERTICAL)
        self.__vline_5 = Separator(root, orient=VERTICAL)

        self.__hline_1 = Separator(root, orient=HORIZONTAL)
        self.__hline_2 = Separator(root, orient=HORIZONTAL)
        self.__hline_3 = Separator(root, orient=HORIZONTAL)

        self.__buttonbar_l = ButtonPanel_L(root) 
        self.__buttonbar_s0 = ButtonPanel_S0(root) 
        self.__buttonbar_s1 = ButtonPanel_S1(root) 
        self.__buttonbar_s2 = ButtonPanel_S2(root) 
        self.__buttonbar_s3 = ButtonPanel_S3(root) 
        
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        self.__buttonbar_l.grid(row=1, column=7)
        self.__buttonbar_s0.grid(row=3, column=1)
        self.__buttonbar_s1.grid(row=3, column=3)
        self.__buttonbar_s2.grid(row=3, column=5)
        self.__buttonbar_s3.grid(row=3, column=7)

        self.__vline_1.grid(row=0, column=0, rowspan=8, sticky='ns')
        self.__vline_2.grid(row=0, column=2, rowspan=8, sticky='ns')
        self.__vline_3.grid(row=0, column=4, rowspan=8, sticky='ns')
        self.__vline_4.grid(row=0, column=6, rowspan=8, sticky='ns')
        self.__vline_5.grid(row=0, column=8, rowspan=8, sticky='ns')

        self.__hline_1.grid(row=0, column=0, columnspan=8, sticky='ew')
        self.__hline_2.grid(row=2, column=0, columnspan=8, sticky='ew')
        self.__hline_3.grid(row=4, column=0, columnspan=8, sticky='ew')
