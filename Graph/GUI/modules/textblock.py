import tkinter as tk

class Textbox(tk.Frame): 
    def __init__(self, root, width, height, justify, text): 
        tk.Frame.__init__(self, root, width=width, height=height)
        tk.Label.__init__(self, root, width=width, height=height)
        self.root = root 

        self.text = text 
        self.justify = justify 
        
        self.label = tk.Label(root, justify=justify, text=text)

if __name__ == "__main__": 
    root = tk.Tk() 
    
    root.mainloop() 