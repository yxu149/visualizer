import sys
import os 

from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

class ButtonPanel_S1(Frame): 
    def __init__(self, root, width=BUTTON_S_WIDTH, height=BUTTON_S_HEIGHT): 
        Frame.__init__(self, root, width=width, height=height) 
        self.root = root

        self.__button_S1_1 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_1.png'),\
                          self.event_S1_1)
        self.__button_S1_2 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_2.png'),\
                          self.event_S1_2)
        self.__button_S1_3 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_3.png'),\
                          self.event_S1_3)
        self.__button_S1_4 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_4.png'),\
                          self.event_S1_4)
        self.__button_S1_5 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_5.png'),\
                          self.event_S1_5)
        self.__button_S1_6 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_6.png'),\
                          self.event_S1_6)
        self.__button_S1_7 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_7.png'),\
                          self.event_S1_7)
        self.__button_S1_8 = ButtonPanel_S1.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S1_8.png'),\
                          self.event_S1_8)
        
        self.__button_S1_1.grid(row=0, column=0, padx=10, pady=10)
        self.__button_S1_2.grid(row=0, column=1, padx=10, pady=10)
        self.__button_S1_3.grid(row=0, column=2, padx=10, pady=10)
        self.__button_S1_4.grid(row=0, column=3, padx=10, pady=10)
        self.__button_S1_5.grid(row=1, column=0, padx=10, pady=10)
        self.__button_S1_6.grid(row=1, column=1, padx=10, pady=10)
        self.__button_S1_7.grid(row=1, column=2, padx=10, pady=10)
        self.__button_S1_8.grid(row=1, column=3, padx=10, pady=10)
        
    @staticmethod
    def create_button(parent, img_path, cmd): 
        img = PhotoImage(file=img_path)
        button = Button(parent, image=img, command=cmd)
        button.image = img 
        return button 
    
    def event_S1_1(self): 
        """
        Upload Graph
        """
        print("Button S1_1 Pressed")
    def event_S1_2(self): 
        """
        Save Graph
        """
        print("Button S1_2 Pressed")
    def event_S1_3(self): 
        """
        Clear Graph
        """
        print("Button S1_3 Pressed")
    def event_S1_4(self): 
        """
        Reset Cursor
        """
        print("Button S1_4 Pressed")
    def event_S1_5(self): 
        print("Button S1_5 Pressed")
    def event_S1_6(self): 
        print("Button S1_6 Pressed")
    def event_S1_7(self): 
        print("Button S1_7 Pressed")
    def event_S1_8(self): 
        print("Button S1_8 Pressed")

if __name__ == "__main__": 
    root = Tk() 
    
    root.mainloop() 