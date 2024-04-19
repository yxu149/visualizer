import sys
import os 

from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

class ButtonPanel_L(Frame): 
    def __init__(self, root, width=BUTTON_L_WIDTH, height=BUTTON_L_HEIGHT): 
        Frame.__init__(self, root, width=width, height=height) 
        self.root = root

        self.__button_L1 = ButtonPanel_L.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','L1.png'),\
                          self.event_L1)
        self.__button_L2 = ButtonPanel_L.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','L2.png'),\
                          self.event_L2)
        self.__button_L3 = ButtonPanel_L.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','L3.png'),\
                          self.event_L3)
        self.__button_L4 = ButtonPanel_L.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','L4.png'),\
                          self.event_L1)
        self.__button_L5 = ButtonPanel_L.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','L5.png'),\
                          self.event_L1)
        self.__button_L6 = ButtonPanel_L.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','L6.png'),\
                          self.event_L1)
        
        self.__button_L1.grid(row=0, column=0, padx = 10, pady=10)
        self.__button_L2.grid(row=0, column=1, padx = 10, pady=10)
        self.__button_L3.grid(row=1, column=0, padx = 10, pady=10)
        self.__button_L4.grid(row=1, column=1, padx = 10, pady=10)
        self.__button_L5.grid(row=2, column=0, padx = 10, pady=10)
        self.__button_L6.grid(row=2, column=1, padx = 10, pady=10)
        
    @staticmethod
    def create_button(parent, img_path, callback): 
        img = PhotoImage(file=img_path)
        button = Button(parent, image=img, command=callback)
        button.image = img 
        return button 
    
    