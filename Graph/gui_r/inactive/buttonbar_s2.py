import sys
import os 

from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

class ButtonPanel_S2(Frame): 
    def __init__(self, root, width=BUTTON_S_WIDTH, height=BUTTON_S_HEIGHT): 
        Frame.__init__(self, root, width=width, height=height) 
        self.root = root

        self.__button_S2_1 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_1.png'),\
                          self.event_S2_1)
        self.__button_S2_2 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_2.png'),\
                          self.event_S2_2)
        self.__button_S2_3 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_3.png'),\
                          self.event_S2_3)
        self.__button_S2_4 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_4.png'),\
                          self.event_S2_4)
        self.__button_S2_5 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_5.png'),\
                          self.event_S2_5)
        self.__button_S2_6 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_6.png'),\
                          self.event_S2_6)
        self.__button_S2_7 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_7.png'),\
                          self.event_S2_7)
        self.__button_S2_8 = ButtonPanel_S2.create_button(self, \
                          os.path.join(BASE_DIR,'gui','parts','icons','S2_8.png'),\
                          self.event_S2_8)
        
        self.__button_S2_1.grid(row=0, column=0, padx=10, pady=10)
        self.__button_S2_2.grid(row=0, column=1, padx=10, pady=10)
        self.__button_S2_3.grid(row=0, column=2, padx=10, pady=10)
        self.__button_S2_4.grid(row=0, column=3, padx=10, pady=10)
        self.__button_S2_5.grid(row=1, column=0, padx=10, pady=10)
        self.__button_S2_6.grid(row=1, column=1, padx=10, pady=10)
        self.__button_S2_7.grid(row=1, column=2, padx=10, pady=10)
        self.__button_S2_8.grid(row=1, column=3, padx=10, pady=10)
        
    @staticmethod
    def create_button(parent, img_path, callback): 
        img = PhotoImage(file=img_path)
        button = Button(parent, image=img, command=callback)
        button.image = img 
        return button 
    
    def event_S2_1(self): 
        print("Button S2_1 Pressed")
    def event_S2_2(self): 
        print("Button S2_2 Pressed")
    def event_S2_3(self): 
        print("Button S2_3 Pressed")
    def event_S2_4(self): 
        print("Button S2_4 Pressed")
    def event_S2_5(self): 
        print("Button S2_5 Pressed")
    def event_S2_6(self): 
        print("Button S2_6 Pressed")
    def event_S2_7(self): 
        print("Button S2_7 Pressed")
    def event_S2_8(self): 
        print("Button S2_8 Pressed")

if __name__ == "__main__": 
    root = Tk() 
    
    root.mainloop() 