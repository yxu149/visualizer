# Some state definitions

default = 0

add_node = 1
remove_node = 2
    
add_line = 3 
remove_line = 4

start_node = 5
end_node = 6 

disabled = -1 

class CursorStates(): 
    """
    Define: Cursor states, set their UI icons
    """

    def __init__(self): 
        self.__state = CursorStates.default 
        self.callback = None 
        self.__root = None 

    def set_root(self, root): 
        self.__root = root 
    
    def set_callback(self, callback): 
        self.callback = callback 

    def set_icon(self): 
        pass

    def get_state(self): 
        return self.__state 
    
mouse = CursorStates() 