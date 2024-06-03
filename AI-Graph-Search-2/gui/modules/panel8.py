import tkinter as tk
import gui.modules.buttons as buttons
import settings.settings as settings

class Panel(tk.Frame): 
    def __init__(self, root, events=[], icons=[], tips=[], width=0, height=0): 
        tk.Frame.__init__(self, root, width=width, height=height, background=settings.PANEL8_BG)
        self.root = root 
        
        # make 8 buttons
        self.__b0 = buttons.create_button(self, icons[0], events[0], tips[0])
        self.__b1 = buttons.create_button(self, icons[1], events[1], tips[1])
        self.__b2 = buttons.create_button(self, icons[2], events[2], tips[2])
        self.__b3 = buttons.create_button(self, icons[3], events[3], tips[3])
        self.__b4 = buttons.create_button(self, icons[4], events[4], tips[4])
        self.__b5 = buttons.create_button(self, icons[5], events[5], tips[5])
        self.__b6 = buttons.create_button(self, icons[6], events[6], tips[6])
        self.__b7 = buttons.create_button(self, icons[7], events[7], tips[7])
        """
        Place buttons on grid
        Scheme
        | 0 | 1 | 2 | 3 |
        ----------------- 
        | 4 | 5 | 6 | 7 |
        """
        self.__pack_on_screen() 

    def __pack_on_screen(self): 
        self.__b0.grid(in_=self, row=0, column=0, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b1.grid(in_=self, row=0, column=1, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b2.grid(in_=self, row=0, column=2, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b3.grid(in_=self, row=0, column=3, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b4.grid(in_=self, row=1, column=0, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b5.grid(in_=self, row=1, column=1, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b6.grid(in_=self, row=1, column=2, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        self.__b7.grid(in_=self, row=1, column=3, padx=settings.BUTTON_S_PADX, pady=settings.BUTTON_S_PADY, stick="NSEW")
        print("packed 8 buttons")

