import tkinter as tk 
import gui.modules.buttons as buttons
import settings.settings as settings

class Panel(tk.Frame): 
    def __init__(self, root, events=[], icons=[], tips=[], width=0, height=0): 
        tk.Frame.__init__(self, root, width=width, height=height, background=settings.PANEL6_BG)
        self.root = root 
        self.events = events 
        self.icons = icons
        # make 6 buttons
        self.__b0 = buttons.create_button(self, icons[0], events[0], tips[0])
        self.__b1 = buttons.create_button(self, icons[1], events[1], tips[1])
        self.__b2 = buttons.create_button(self, icons[2], events[2], tips[2])
        self.__b3 = buttons.create_button(self, icons[3], events[3], tips[3])
        self.__b4 = buttons.create_button(self, icons[4], events[4], tips[4])
        self.__b5 = buttons.create_button(self, icons[5], events[5], tips[5])
        """
        Place buttons on grid
        Scheme
        | 0 | 1 |
        ---------
        | 2 | 3 | 
        ---------
        | 4 | 5 |
        """
        self.__pack_on_screen()

    def __pack_on_screen(self):
        self.__b0.grid(row=0, column=0, padx=settings.BUTTON_L_PADX, pady=settings.BUTTON_L_PADY, stick="NSEW")
        self.__b1.grid(row=0, column=1, padx=settings.BUTTON_L_PADX, pady=settings.BUTTON_L_PADY, stick="NSEW")
        self.__b2.grid(row=1, column=0, padx=settings.BUTTON_L_PADX, pady=settings.BUTTON_L_PADY, stick="NSEW")
        self.__b3.grid(row=1, column=1, padx=settings.BUTTON_L_PADX, pady=settings.BUTTON_L_PADY, stick="NSEW")
        self.__b4.grid(row=2, column=0, padx=settings.BUTTON_L_PADX, pady=settings.BUTTON_L_PADY, stick="NSEW")
        self.__b5.grid(row=2, column=1, padx=settings.BUTTON_L_PADX, pady=settings.BUTTON_L_PADY, stick="NSEW")
        print("packed 6 buttons")