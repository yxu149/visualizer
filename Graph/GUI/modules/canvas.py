from tkinter import *
from settings.settings import *

panel_width = BUTTON_L_WIDTH*2 + BUTTON_L_PADX*3 
panel_height = BUTTON_L_HEIGHT*3 + BUTTON_L_PADY*4

class Panel(Frame): 
    def __init__(self, root, events, icons, width=panel_width, height=panel_height): 
        Frame.__init__(self, root, width=width, height=height)
        self.root = root 
        
        # make 8 buttons
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
        img = PhotoImage(file=img_path)
        button = Button(parent, image=img, command=callback)
        button.image = img 
        return button 
    
    def get_width(): 
        return panel_width
    
    def get_height(): 
        return panel_height