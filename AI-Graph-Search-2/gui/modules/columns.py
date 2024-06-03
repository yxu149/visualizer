import tkinter as tk
import settings.settings as settings

class Col(tk.Frame): 
    def __init__(self, root, \
                 top, mid, down, \
                 width=10, height=10): 
        tk.Frame.__init__(self, root, width=width, height=height, bg=settings.COL_BG)
        
        self.__top = top 
        self.__mid = mid 
        self.__down = down
    
    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")

    def __len__(self): 
        return 0
