import sys
import os 

from tkinter import Misc

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

from settings.settings import *

panel_width = BUTTON_S_WIDTH*4 + BUTTON_S_PADX*5 
panel_height = BUTTON_S_HEIGHT*4 + BUTTON_S_PADY*3

class Panel8(Frame): 
    def __init__(self, root, events, icons, width=panel_width, height=panel_height): 
        Frame.__init__(self, root, width=width, height=height)
        self.root = root 
        
        # make 8 buttons
        self.__b0 = Panel8.create_button(self, icons[0], events[0])
        self.__b1 = Panel8.create_button(self, icons[1], events[1])
        self.__b2 = Panel8.create_button(self, icons[2], events[2])
        self.__b3 = Panel8.create_button(self, icons[3], events[3])
        self.__b4 = Panel8.create_button(self, icons[4], events[4])
        self.__b5 = Panel8.create_button(self, icons[5], events[5])
        self.__b6 = Panel8.create_button(self, icons[6], events[6])
        self.__b7 = Panel8.create_button(self, icons[7], events[7])
        """
        Place buttons on grid
        Scheme
        | 0 | 1 | 2 | 3 |
        ----------------- 
        | 4 | 5 | 6 | 7 |
        """
        self.__b0.grid(row=0, column=0, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b1.grid(row=0, column=1, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b2.grid(row=0, column=2, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b3.grid(row=0, column=3, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b4.grid(row=1, column=0, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b5.grid(row=1, column=1, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b6.grid(row=1, column=2, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)
        self.__b7.grid(row=1, column=3, padx=BUTTON_S_PADX, pady=BUTTON_S_PADY)

    # call Button to have a button made
    @staticmethod
    def create_button(parent, img_path, callback): 
        img = PhotoImage(file=img_path)
        button = Button(parent, image=img, command=callback)
        button.image = img 
        return button 
    