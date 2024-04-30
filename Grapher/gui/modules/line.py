import settings.settings as settings 
import gui.wirings.element_ctrl as element_ctrl
import gui.modules.element as element 
import gui.modules.stage as stage 
from abc import abstractmethod

class Line(element.Element): 
    def __init__(self, stage, start_node, end_node, weight=1): 
        self.__id = None
        self.__stage = stage 
        self.start_node = start_node  
        self.end_node = end_node 
        self.__weight = weight 
    
    def get_save_data(self): 
        return str(
            str(self.__weight) + '\t' + \
            str(self.start_node.get_id()) + '\t' + \
            str(self.end_node.get_id())  +  '\n'
        )
    
    def get_weight(self): 
        return self.__weight 
    
    def get_id(self): 
        return self.__id
    
    def set_weight(self, weight): 
        if weight != self.__weight: 
            self.__weight = weight 
            self.__stage.itemconfig(self.__label_id, text=str(weight))

    def create_label(self): 
        x1, y1, x2, y2 = self.__stage.coords(self.__id) 
        x = (x1 + x2) // 2
        y = (y1 + y2) // 2
        self.__label_id = self.__stage.create_text((x, y), text=self.__weight)

    def create_line(self): 
        start_node_x, start_node_y = self.start_node.get_coords() 
        end_node_x, end_node_y = self.end_node.get_coords() 

        dy = abs(end_node_y - start_node_y)
        dx = abs(end_node_x - start_node_x) 

        if(dx > dy): 
            if(end_node_y < start_node_y): 
                self.__id = self.__stage.create_line(start_node_x, start_node_y+settings.NODE_RADIUS, end_node_x, end_node_y+settings.NODE_RADIUS, arrow="last", fill=settings.LINE_COLOR_NORMAL)
            else: 
                self.__id = self.__stage.create_line(start_node_x, start_node_y-settings.NODE_RADIUS, end_node_x, end_node_y-settings.NODE_RADIUS, arrow="last", fill=settings.LINE_COLOR_NORMAL)
        else: 
            if(end_node_x > start_node_x): 
                self.__id = self.__stage.create_line(start_node_x+settings.NODE_RADIUS, start_node_y, end_node_x+settings.NODE_RADIUS, end_node_y, arrow="last", fill=settings.LINE_COLOR_NORMAL)
            else: 
                self.__id = self.__stage.create_line(start_node_x-settings.NODE_RADIUS, start_node_y, end_node_x-settings.NODE_RADIUS, end_node_y, arrow="last", fill=settings.LINE_COLOR_NORMAL)

        self.create_label()
        self.__stage.lower(self.__id) 

        return self 
    
    def reset(self): 
        self.__tree = None 
        self.__line = None 
        self.deselect() 
    
    def set_active(self): 
        self.select() 
        self.__tree.itemconfig()