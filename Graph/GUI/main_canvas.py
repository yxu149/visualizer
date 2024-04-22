import tkinter as tk
from settings.settings import *
from wiring import l0, s0, s1, s2, s3, io
from modules import columns, panel6, panel8, cursor, textblock

"""
Some basic UI size definitions

* Not to Scale 
 x --> 

(h3) | Canvas | Standard Graph | User Graph     | Algorithm Selection | ( 
---
(h2) |< w1   >|< w1 > (h2)     |< w1 > (h2)     | Media Controls      | h0
---
(h1) | S0     | S1             | S2             | S3                  | )
      < w0                                                           >
w0 = total left to right <>
h0 = total top to buttom ()

"""
w1 = BUTTON_S_WIDTH*4 + BUTTON_S_PADX*5 
h1 = BUTTON_S_HEIGHT*4 + BUTTON_S_PADY*3
h2 = BUTTON_L_HEIGHT*3 + BUTTON_L_PADY*4
h3 = 20
w0 = w1 * 4
h0 = h3 + h2 + h1 


class MainCanvas(tk.Frame): 
    def __init__(self, root, width=200, height=200): 
        self.width = width
        self.height = height
        tk.Frame.__init__(self, root, width=width, height=height)
        cursor.mouse.set_root(self)
        
        self.__x0_top = textblock.Textbox(self, root, STR_X0_TOP, mode='center', width=w1, height=h3)
        self.__x1_top = textblock.Textbox(self, root, STR_X1_TOP, mode='center', width=w1, height=h3)
        self.__x2_top = textblock.Textbox(self, root, STR_X2_TOP, mode='center', width=w1, height=h3)

        self.__col0 = columns.Col(self, root, )
        self.__col1 = columns.Col(self, root, )
        self.__col2 = columns.Col(self, root, )

        self.__pack_on_screen()

    def __pack_on_screen(self): 
        pass