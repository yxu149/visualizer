import sys
import os 

from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

class ButtonPanel_S0(Frame): 
    def __init__(self, root, width=BUTTON_S_WIDTH, height=BUTTON_S_HEIGHT): 
        Frame.__init__(self, root, width=width, height=height) 
        self.root = root

        self.__button_S0_1 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_1.png'),\
                          self.event_S0_1)
        self.__button_S0_2 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_2.png'),\
                          self.event_S0_2)
        self.__button_S0_3 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_3.png'),\
                          self.event_S0_3)
        self.__button_S0_4 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_4.png'),\
                          self.event_S0_4)
        self.__button_S0_5 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_5.png'),\
                          self.event_S0_5)
        self.__button_S0_6 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_6.png'),\
                          self.event_S0_6)
        self.__button_S0_7 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_7.png'),\
                          self.event_S0_7)
        self.__button_S0_8 = ButtonPanel_S0.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S0_8.png'),\
                          self.event_S0_8)
        
        self.__button_S0_1.grid(row=0, column=0, padx=10, pady=10)
        self.__button_S0_2.grid(row=0, column=1, padx=10, pady=10)
        self.__button_S0_3.grid(row=0, column=2, padx=10, pady=10)
        self.__button_S0_4.grid(row=0, column=3, padx=10, pady=10)
        self.__button_S0_5.grid(row=1, column=0, padx=10, pady=10)
        self.__button_S0_6.grid(row=1, column=1, padx=10, pady=10)
        self.__button_S0_7.grid(row=1, column=2, padx=10, pady=10)
        self.__button_S0_8.grid(row=1, column=3, padx=10, pady=10)
        
    @staticmethod
    def create_button(parent, img_path, cmd): 
        img = PhotoImage(file=img_path)
        button = Button(parent, image=img, command=cmd)
        button.image = img 
        return button 
    
    def event_S0_1(self): 
        """
        Set start
        """
        print("Button S0_1 Pressed")
    def event_S0_2(self): 
        """
        Set goal
        """
        print("Button S0_2 Pressed")
    def event_S0_3(self): 
        """
        Set weight
        """
        print("Button S0_3 Pressed")
    def event_S0_4(self): 
        """
        Button 04
        """
        print("Button S0_4 Pressed")
    def event_S0_5(self): 
        """
        Add Node
        """
        print("Button S0_5 Pressed")
    def event_S0_6(self): 
        """
        Remove Node
        """
        print("Button S0_6 Pressed")
    def event_S0_7(self): 
        """
        Add Path
        """
        print("Button S0_7 Pressed")
    def event_S0_8(self): 
        """
        Remove Path
        """
        print("Button S0_8 Pressed")

if __name__ == "__main__": 
    root = Tk() 
    
    root.mainloop() 