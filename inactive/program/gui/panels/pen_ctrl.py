import os 
import tkinter as tk 

from settings import *

class PenCtrl(tk.Frame): 
    def __init__(self, root, width=BUTTON_L_WIDTH, height=BUTTON_L_HEIGHT): 
        tk.Frame.__init__(self, root, width=width, height=height) 
        self.root = root

        self.__button_L1 = PenCtrl.create_button(self, \
                           os.path.join(BASE_DIR,'gui','icons','L1.png'),\
                           self.event_L1)
        self.__button_L2 = PenCtrl.create_button(self, \
                           os.path.join(BASE_DIR,'gui','icons','L2.png'),\
                           self.event_L2)
        self.__button_L3 = PenCtrl.create_button(self, \
                           os.path.join(BASE_DIR,'gui','icons','L3.png'),\
                           self.event_L3)
        self.__button_L4 = PenCtrl.create_button(self, \
                           os.path.join(BASE_DIR,'gui','icons','L4.png'),\
                           self.event_L4)
        self.__button_L5 = PenCtrl.create_button(self, \
                           os.path.join(BASE_DIR,'gui','icons','L5.png'),\
                           self.event_L5)
        self.__button_L6 = PenCtrl.create_button(self, \
                           os.path.join(BASE_DIR,'gui','icons','L6.png'),\
                           self.event_L6)
        
        self.__button_L1.grid(row=0, column=0, padx=10, pady=10)
        self.__button_L2.grid(row=0, column=1, padx=10, pady=10)
        self.__button_L3.grid(row=1, column=0, padx=10, pady=10)
        self.__button_L4.grid(row=1, column=1, padx=10, pady=10)
        self.__button_L5.grid(row=2, column=0, padx=10, pady=10)
        self.__button_L6.grid(row=2, column=1, padx=10, pady=10)
        
    @staticmethod
    def create_button(parent, img_path, callback): 
        img = tk.PhotoImage(file=img_path)
        button = tk.Button(parent, image=img, command=callback)
        button.image = img 
        return button 
    
    """
    Events
    """
    def event_L1(self): 
        """
        Play
        """
        print("Play Button (L1) Pressed")
        pass
    def event_L2(self): 
        """
        Next Step
        """
        print("Next Step Button (L2) Pressed")
    def event_L3(self): 
        """
        Pause
        """
        print("Pause Button (L3) Pressed")
    def event_L4(self): 
        """
        Prev Step
        """
        print("Prev Step Button (L4) Pressed")
    def event_L5(self): 
        """
        Stop
        """
        print("Stop Button (L5) Pressed")
    def event_L6(self): 
        """
        Clear
        """
        print("Empty Button (L6) Pressed")

if __name__ == "__main__": 
    root = tk.Tk() 
    
    root.mainloop() 