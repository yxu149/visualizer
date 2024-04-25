import tkinter as tk 
from settings import *

class Col(tk.Frame): 
    
    def __init__(self, root, w=10, h=10, top=None, mid=None, down=None): 
        tk.Frame.__init__(self, root, width=w, height=h) 
        self.__root = root 
        self.__width = w 
        self.__height = h
        self.__top = top 
        self.__mid = mid 
        self.__down = down
         
        self.__pack(self) 

    def __pack(self): 
        self.__top.grid(row=0, column=0, padx=COL_PADX, pady=COL_PADY)
        self.__mid.grid(row=1, column=0, padx=COL_PADX, pady=COL_PADY)
        self.__down.grid(row=2, column=0, padx=COL_PADX, pady=COL_PADY)
