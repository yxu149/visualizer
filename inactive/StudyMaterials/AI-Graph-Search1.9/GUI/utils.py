"""
Utilities

Handle  - OverlapException 
        - DuplicateConnectionException. 
Define  - Mouse_state. 
"""

class OverlapException(Exception):
    """
    Parameters: Exception
    Note: Mouse position overlaps an existing node. 

    Potential for a delete node function. 
    """

    def __init__(self,message="Can't place the node as it overlaps with another node"
                ,title="Overlaping Error"):
        self.message = message
        self.title = title
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return self.message

class DuplicateConnectionException(Exception):
    """
    Parameters: Exception
    Note: Duplicate paths between two nodes. 

    Potential for a delete connection function. 
    """

    def __init__(self,message="This connection already exists"
                ,title="Duplicate Connection Error"):
        self.message = message
        self.title = title
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return self.message


class Mouse_state:
    """
    Define: mouse states, auto set their UI icons. 
    """
   
    normal  = 1          # neither circle nor line is clicked 
    circle = 2           # circle is clicked
    line   = 3           # line is clicked
    initial_node = 4     # initial node clicked
    goal_node = 5        # goal node clicked
    disabled = 6         # clicks is disabled

    def __init__(self):
        self.__state = Mouse_state.normal
        self.callback = None    
        self.__root = None

    def set_root(self,root):
        self.__root = root

    def set_callback(self,callback):
        self.callback = callback

    def __reset_cursor(self):
        """
        Parameters: self

        Checks self.__state and reassign corresponding 
        values by calling self.__root.config(cursor="") 
        """
        if (self.__state == Mouse_state.goal_node):
            self.__root.config(cursor="target")
        elif(self.__state == Mouse_state.initial_node):
            self.__root.config(cursor="spider")
        elif(self.__state == Mouse_state.line):
            self.__root.config(cursor="plus")
        elif(self.__state == Mouse_state.circle):   
            self.__root.config(cursor="cross")
        else:
            self.__root.config(cursor="arrow")
            
    def set_state(self,new_state):
        """
        Parameters: self, new_state

        Sets self.__state = new_state when safe. 
        Then resets cursor. 
        """
        if self.callback :
            self.callback()
            self.__state = new_state
        else:
            self.__state = new_state
        self.__reset_cursor()

    def get_state(self):
        """
        Parameters: self
        Returns: self.__state
        
        Access function. 
        """
        return self.__state

mouse = Mouse_state()

def filter_options(options, item_type):
    valid_options = {
        'rectangle': {'fill', 'outline', 'width', 'dash', 'activefill', 'activeoutline', 'activewidth'},
        'oval': {'fill', 'outline', 'width', 'dash', 'activefill', 'activeoutline', 'activewidth'},
        'line': {'fill', 'width', 'dash', 'arrow', 'arrowshape', 'activefill', 'activewidth'},
        'text': {'text', 'font', 'fill'}
        # Add other item types and their valid options as needed
    }
    return {k: v for k, v in options.items() if k in valid_options.get(item_type, set())}

def copy_canvas(original, new):
    # Get all items from the original canvas
    items = original.find_all()
    
    for item in items:
        # Get the item's coordinates and options
        coords = original.coords(item)
        options = original.itemconfig(item)
        item_type = original.type(item)
        
        # Flatten options dictionary
        flattened_options = {}
        for k, v in options.items():
            flattened_options[k] = v[-1]
        
        # Filter options based on item type
        valid_options = filter_options(flattened_options, item_type)
        
        # Create the same item on the new canvas
        if item_type == "rectangle":
            new.create_rectangle(*coords, **valid_options)
        elif item_type == "oval":
            new.create_oval(*coords, **valid_options)
        elif item_type == "line":
            new.create_line(*coords, **valid_options)
        elif item_type == "text":
            new.create_text(*coords, **valid_options)
        # Add other item types as needed