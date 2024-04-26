import tkinter as tk

class Textbox(): 
    def __init__(self, root, width, height, justify, text): 
        self.label = tk.Label(self, width=width, height=height, justify=justify, text=text)
        self.root = root 
        self.label.grid()

if __name__ == "__main__": 
    root = tk.Tk() 
    
    root.mainloop() 