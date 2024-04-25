import tkinter as tk

class Textbox(): 
    def __init__(self, root, width, height, justify, text): 
        self.label = tk.Label(root, justify=justify, text=text)
        self.root = root 

        self.text = text 
        self.justify = justify 
        
        self.label.configure(textvariable=text)

if __name__ == "__main__": 
    root = tk.Tk() 
    
    root.mainloop() 