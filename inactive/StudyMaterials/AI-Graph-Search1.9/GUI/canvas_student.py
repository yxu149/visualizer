from tkinter import *
from tkinter import messagebox
from .Node import Node ,Line
from .Buttons import Button_Bar
from .settings import CANVAS_BACKGROUND_COLOR
from .utils import mouse,Mouse_state,copy_canvas
from .canvas import DrawingCanvas


class DrawingCanvasStudent(Frame):

    def __init__(self,root,canvas_width=2000,canvas_height=1300,event_root=None,onselect=None,onrelease=None):
        '''
        constructor
        '''
        self.root = root
        Frame.__init__(self, root) 
        self.__count_nodes = 0 # this variable used to count nodes helpful in labeling nodes
        self.hor_scrollbar = Scrollbar(self, orient=HORIZONTAL)
        self.ver_scrollbar = Scrollbar(self, orient=VERTICAL)
        
        self.canvas = Canvas(self,background=CANVAS_BACKGROUND_COLOR,scrollregion=(0, 0, canvas_width, canvas_height),yscrollcommand=self.ver_scrollbar.set,xscrollcommand=self.hor_scrollbar.set) # canvas object
        self.hor_scrollbar['command'] = self.canvas.xview
        self.ver_scrollbar['command'] = self.canvas.yview
         
        self.connection_node = None # node which carry the id of previously selected node needed only in line case as line needs to connects two nodes so this is considered as the first node  
        self.mainObjectsLookup = dict() # hash-map used for mapping main object id to student objects id
        self.objects = dict() # hash-map used for mapping objects_id (Lines and Nodes) on canvas to objects (Line or Node) 
        self.selected = None # carry the id of selected node to be edited , deleted
        self.initial_node = None # carry initial node
        
        self.canvas.grid(row=0,column=0,sticky=(N,W,E,S)) # places the canvas in row : 0 , column :0 in the frame
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        self.hor_scrollbar.grid(column=0, row=1, sticky=(W,E))
        self.ver_scrollbar.grid(column=1, row=0, sticky=(N,S))
        self.main_canvas = None #main canvas will set this variable to the main canvas object
        

    def delete_all(self):

        self.__count_nodes = 0 
        self.connection_node = None 
        del self.objects
        self.objects = dict()  
        self.selected = None
        self.initial_node = None
        self.canvas.delete("all")
    
    def reset(self):
        for _,element in self.objects.items():
            element.reset()


        




if __name__=="__main__":


    root =  Tk()
    root.geometry("1000x720")
    b = Button_Bar(root)
    student_can = DrawingCanvasStudent(root,920,720)
    canvas = DrawingCanvas(root,920,720,student_canvas=student_can)
    
    

    canvas.grid(row=0,column=0,sticky="NSEW")
    student_can.grid(row=0,column=2,sticky="NSEW")
    b.grid(row=0,column=1,sticky="NSEW")
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)

    root.mainloop()







