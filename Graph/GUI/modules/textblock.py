from tkinter import *

class Textbox(Frame): 
    def __init__(self, root, text, mode, width, height): 
        Frame.__init__(self, root, width=width, height=height)
        self.__root = root 

        self.__text = text 
        self.__mode = mode 
        
        self.__label = Label(root, justify=mode, text=text)
