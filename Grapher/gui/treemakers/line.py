import tkinter as tk 
import utils.exceptions as exceptions

import settings

class Line(): 
    def __init__(self, canvas, prev_node, next_node, weight=1): 
        self.__id = None 
        self.land = canvas
        self.prev_node = prev_node 
        self.next_node = next_node 
        self.weight = weight 

    # data io
    def load_data(self): 
        pass 

    def save_data(self): 
        pass 
    
    # gets 
    def get_prev(self): 
        return self.prev_node 
    
    def get_next(self): 
        return self.next_node
    
    def get_weight(self): 
        return self.weight 
    
    # sets 
    def set_prev(self, prev): 
        self.prev_node = prev 
    
    def set_next(self, next): 
        self.next_node = next 
    
    def set_weight(self, weight): 
        self.weight = weight 
    
    # display elements 
    