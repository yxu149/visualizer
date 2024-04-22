import tkinter as tk

class Textbox(tk.Frame): 
    def __init__(self, root, text, mode, width, height): 
        tk.Frame.__init__(self, root, width=width, height=height)
        self.__root = root 

        self.__text = text 
        self.__mode = mode 
        
        self.__label = tk.Label(root, justify=mode, text=text)
