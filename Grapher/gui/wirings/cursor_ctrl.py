class CursorStates(): 
    """
    Define: Cursor states, set their UI icons
    """
    default = 0

    add_node = 1
    remove_node = 2
    
    add_line = 3 
    remove_line = 4

    start_node = 5
    end_node = 6 

    disabled = -1 

    def __init__(self): 
        self.__state = CursorStates.default 
        self.callback = None 
        self.__root = None 

    def set_root(self, root): 
        self.__root = root 
    
    def set_callback(self, callback): 
        self.callback = callback 

    def reset(self): 
        """
        Parameters: self 

        Checks self.__state and reassign corresponding 
        values by calling self.__root.config(cursor="")
        """
        if (self.__state == )