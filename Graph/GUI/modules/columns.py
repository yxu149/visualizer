import tkinter as tk

class Col(tk.Frame): 
    def __init__(self, root, \
                 part_top, part_mid, part_down, \
                 width=10, height=10): 
        tk.Frame.__init__(self, root, width=width, height=height)
        self.root = root 

        self.__part_top = part_top 
        self.__part_mid = part_mid 
        self.__part_down = part_down 

        self.__part_top.grid(row=0, column=0, padx=5, pady=5)
        self.__part_mid.grid(row=1, column=0, padx=5, pady=5) 
        self.__part_down.grid(row=2, column=0, padx=5, pady=5)

