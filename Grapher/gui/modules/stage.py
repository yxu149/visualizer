import tkinter as tk 
import tkinter.constants as constants
import tkinter.messagebox as messagebox 
import gui.wirings.element_ctrl as element_ctrl 
import settings.settings as settings

class Stage(tk.Frame): 
    def __init__(self, root, width=settings.w1, height=settings.h2,\
                 event_root=None, onselect=None, onrelease=None): 
        self.__root = root 
        tk.Frame.__init__(self, root) 
        self.__node_count = 0 
        self.h_scrollbar = tk.Scrollbar(self, orient=constants.HORIZONTAL)
        self.v_scrollbar = tk.Scrollbar(self, orient=constants.VERTICAL) 

        self.canvas = tk.Canvas(self, bg=settings.STAGE_BG, scrollregion=(0, 0, width*2, height*2), yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)

        self.h_scrollbar['command'] = self.canvas.xview 
        self.v_scrollbar['command'] = self.canvas.yview
        
        # Previously Selected Node
        # Takes on the ID of the previously selected node 
        # Used to form a line between the two nodes
        self.previously_selected_node = None 

        self.objects = dict() 
        self.selected_node = None 
        self.root_node = None 