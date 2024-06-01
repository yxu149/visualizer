import tkinter as tk 
import utils.exceptions as exceptions

import settings

class Line(): 
    def __init__(self, canvas, prev_node, next_node, weight=1, \
                 is_goal=False, is_entry=False): 
        self.id = None 
        self.land = canvas
        self.prev_node = prev_node 
        self.next_node = next_node 
        self.weight = weight 

        # node properties 
        self.is_goal = is_goal
        self.is_entry = is_entry
        self.is_visited = False 

        # none boolean properties 
        self.__label = label 
        self.__heuristic = heuristic

    # data io
    def load_data(self): 
        pass 

    def save_data(self): 
        pass 
    