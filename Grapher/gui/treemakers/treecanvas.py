import tkinter as tk 
import tkinter.constants as constants
import settings.settings as settings 

class TreeCanvas(tk.Frame): 
    def __init__(self, root, w=100, h=10000): 
        tk.Frame.__init__(self, root) 
        self.node_count = 0
        self.h_scrollbar = tk.Scrollbar(self, orient=constants.HORIZONTAL) 
        self.v_scrollbar = tk.Scrollbar(self, orient=constants.VERTICAL)
        self.canvas = tk.Canvas(self, background=settings.STAGE_BG, scrollregion=(0,0,w,h), \
                                yscrollcommand=self.v_scrollbar.set,\
                                xscrollcommand=self.h_scrollbar.set)
        self.h_scrollbar['command'] = self.canvas.xview 
        self.v_scrollbar['command'] = self.canvas.yview
        self.pack() 
    
    def pack(self): 
        self.canvas.grid(row=0,column=0,sticky="NSEW")
        self.h_scrollbar.grid(row=1,column=0,sticky="EW")
        self.v_scrollbar.grid(row=0,column=1,sticky="NS")
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1) 
    
if __name__=="__main__":
    root = tk.Tk()
    can = TreeCanvas(root)

    can.grid(row=0,column=0,sticky=("NSEW"))
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)

    root.mainloop()