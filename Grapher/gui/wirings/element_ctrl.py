from settings.settings import *
"""
Element Controls

Controls various display elements and their status on the display canvas
"""
class ElementCtrl(): 
    def __init__(self, stage):
        self.__stage = stage
        self.has_cross = False
        
    def set_id(self,id):
        self.__id = id

    def mark_active(self):
        self.__stage.itemconfig(self.__id, fill=NODE_ACTIVE_BG)

    def mark_visited(self):
        self.__stage.itemconfig(self.__id, fill=NODE_VISITED_BG)

    def mark_fringe(self):
        self.__stage.itemconfig(self.__id, fill=NODE_FRINGE_BG)
    
    def __delete_cross(self):
        self.__stage.delete(self.__cross_line1)
        self.__stage.delete(self.__cross_line2)

    def mark_goal_path(self):
        self.reset_cross()
        self.__stage.itemconfig(self.__id, fill=LINE_GOAL_BG)
    
    def reset_cross(self):
        if self.has_cross:
            self.__delete_cross()
            self.has_cross = False

    def mark_already_visited(self):
        self.mark_visited()
        if not self.has_cross:
            self.__draw_cross()
        
    def __draw_cross(self):
        
        self.has_cross = True
        x,y = self.get_coor()
        self.__cross_line1 = self.__stage.create_line(x+LINE_LEN , y+LINE_LEN,x-LINE_LEN , y-LINE_LEN,fill=LINE_VISITED_BG)
        self.__cross_line2 = self.__stage.create_line(x-LINE_LEN , y+LINE_LEN,x+LINE_LEN , y-LINE_LEN,fill=LINE_VISITED_BG)
    
    def move_cross(self):
        x,y = self.get_coor()
        self.__stage.coords(self.__cross_line1,x+LINE_LEN , y+LINE_LEN,x-LINE_LEN , y-LINE_LEN)
        self.__stage.coords(self.__cross_line2,x-LINE_LEN , y+LINE_LEN,x+LINE_LEN , y-LINE_LEN)
