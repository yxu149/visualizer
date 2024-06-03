"""
Get current cursor status
 - coords 
 - click
 - mode of operation
Calls treemakers 
Output tk.canvas 
"""
import tkinter as tk 
import tkinter.constants as tkconstants

LAND_BACKGROUND = '#808080'

class Land(tk.Frame): 
    def __init__(self,root,canvas_width=225,canvas_height=2000):
        tk.Frame.__init__(self, root) 
        self.count_nodes = 0 # this variable used to count nodes helpful in labeling nodes
        self.hor_scrollbar = tk.Scrollbar(self, orient=tkconstants.HORIZONTAL)
        self.ver_scrollbar = tk.Scrollbar(self, orient=tkconstants.VERTICAL) # height=height-20,width=width-20
        self.canvas = tk.Canvas(self,background=LAND_BACKGROUND,scrollregion=(0, 0, canvas_width, canvas_height),yscrollcommand=self.ver_scrollbar.set,xscrollcommand=self.hor_scrollbar.set, width=canvas_width, height=canvas_height) # canvas object
        self.hor_scrollbar['command'] = self.canvas.xview
        self.ver_scrollbar['command'] = self.canvas.yview
        self.pack_on_screen()
    
    def pack_on_screen(self):
        self.canvas.grid(row=0,column=0,sticky=(tkconstants.N,tkconstants.W,tkconstants.E,tkconstants.S))  # places the canvas in row : 0 , column :0 in the frame
        self.hor_scrollbar.grid(column=0, row=1, sticky=(tkconstants.W,tkconstants.E))
        self.ver_scrollbar.grid(column=1, row=0, sticky=(tkconstants.N,tkconstants.S))
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

if __name__=="__main__":
    root = tk.Tk()
    can = Land(root)

    can.grid(row=0,column=0,sticky=(tkconstants.N, tkconstants.S, tkconstants.E, tkconstants.W))
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)

    root.mainloop()