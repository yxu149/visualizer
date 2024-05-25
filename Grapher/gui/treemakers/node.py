import tkinter as tk 
import uuid as uuid

class Node(): 
    def __init__(self, canvas, x, y, label, heuristic=0, \
                 is_goal=False, is_entry=False): 
        
        # node locale information
        self.adjacent_nodes = [] 
        self.lines_in = []
        self.lines_out = [] 

        # node properties 
        self.is_goal = is_goal 
        self.is_entry = is_entry 
        self.is_visited = False 

        # none boolean properties 
        self.__id = uuid.uuid4()
        self.__label = label 
        self.__heuristic = heuristic

        # x y coordinates of this node
        self.__x = x
        self.__y = y

    def load_save(self): 
        pass 

    # gets 
    def get_id(self): 
        return self.__id 
    
    def get_coors(self): 
        return self.__x, self.__y 

    def get_heuristic(self): 
        return self.__heuristic
    
    def get_label(self): 
        return self.__label 
    
    # sets 
    

    # gui