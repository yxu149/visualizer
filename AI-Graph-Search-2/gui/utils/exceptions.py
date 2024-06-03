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

