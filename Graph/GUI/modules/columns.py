from tkinter import *

class Col(Frame): 
    def __init__(self, root, \
                 top, mid, down, \
                 width=10, height=10): 
        Frame.__init__(self, root, width=width, height=height)
        self.root = root 

        self.__top = top 
        self.__mid = mid 
        self.__down = down 

        self.__top.grid(row=0, column=0, padx=5, pady=5)
        if self.__mid is not None:
            self.__mid.grid(row=1, column=0, padx=5, pady=5) 
        
        self.__down.grid(row=2, column=0, padx=5, pady=5)

