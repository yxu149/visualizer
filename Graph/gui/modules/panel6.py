import tkinter as tk 
from gui.wiring.l0 import *
from settings.settings import *

class Panel(tk.Frame): 
    def __init__(self, root, events=[], icons=[], width=230, height=340): 
        tk.Frame.__init__(self, root, width=width, height=height)
        self.root = root 
        self.events = events 
        self.icons = icons
        # make 6 buttons
        self.__b0 = Panel.create_button(self, icons[0], events[0])
        self.__b1 = Panel.create_button(self, icons[1], events[1])
        self.__b2 = Panel.create_button(self, icons[2], events[2])
        self.__b3 = Panel.create_button(self, icons[3], events[3])
        self.__b4 = Panel.create_button(self, icons[4], events[4])
        self.__b5 = Panel.create_button(self, icons[5], events[5])
        """
        Place buttons on grid
        Scheme
        | 0 | 1 |
        ---------
        | 2 | 3 | 
        ---------
        | 4 | 5 |
        """
        self.__b0.grid(row=0, column=0, padx=BUTTON_L_PADX, pady=BUTTON_L_PADY)
        self.__b1.grid(row=0, column=1, padx=BUTTON_L_PADX, pady=BUTTON_L_PADY)
        self.__b2.grid(row=1, column=0, padx=BUTTON_L_PADX, pady=BUTTON_L_PADY)
        self.__b3.grid(row=1, column=1, padx=BUTTON_L_PADX, pady=BUTTON_L_PADY)
        self.__b4.grid(row=2, column=0, padx=BUTTON_L_PADX, pady=BUTTON_L_PADY)
        self.__b5.grid(row=2, column=1, padx=BUTTON_L_PADX, pady=BUTTON_L_PADY)
    
    # call Button to have a button made
    @staticmethod
    def create_button(parent, img_path, callback): 
        img = tk.PhotoImage(file=img_path)
        button = tk.Button(parent, image=img, command=callback)
        button.image = img 
        return button 
    