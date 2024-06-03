import tkinter as tk 
import utils.exceptions as exceptions

import settings

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
        self.__label = label 
        self.__heuristic = heuristic

        # x y coordinates of this node
        self.__x = x
        self.__y = y

        # logistics 
        self.land = canvas
        self.circle = None
        self.name_label = None 
        self.heuristic_label = None 

    # data io
    def load_data(self): 
        pass 

    def save_data(self): 
        pass 

    # gets 
    def get_id(self): 
        return self.__id 
    
    def get_coords(self): 
        return self.__x, self.__y 

    def get_heuristic(self): 
        return self.__heuristic
    
    def get_label(self): 
        return self.__label 
    
    # sets 
    def set_coords(self, x, y): 
        self.__x = x
        self.__y = y

    def set_heuristic(self, heuristic): 
        self.__heuristic = heuristic

    def set_label(self, label): 
        self.__label = label 
    
    # gui
    def make_circle(self): 
        x0 = self.__x - settings.RADIUS 
        y0 = self.__y - settings.RADIUS 
        x1 = self.__x + settings.RADIUS 
        y1 = self.__y + settings.RADIUS 

        overlap = self.land.find_overlapping(x0, y0, x1, y1) 
        if len(overlap): 
            raise exceptions.OverlapException() 
        
        return self.land.create_oval(\
            # four corners of the square that contain the circle
            x0, y0, x1, y1, \
            # node default color 
            fill=settings.NODE_COLOR_DEFAULT)
    
    def node_maker(self): 
        self.circle = self.make_circle()
        self.name_label = self.land.create_text((self.__x, self.__y),\
            text=self.__label)
        self.heuristic_label = self.land.create_text((\
            # where to put the text 
            self.__x-settings.RADIUS, self.__y-settings.RADIUS), \
            # what to put in the text + text color 
            text=self.__heuristic, fill=settings.TEXT_COLOR_HEURISTIC)
        
    