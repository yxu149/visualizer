from .base_class import BaseAlgorithm
import time
import threading
from GUI.settings import SLEEP_AMOUNT

class DepthFirstSearch7(BaseAlgorithm):

    """
    workflow: check goal -> expand node -> mark visited -> pick node -> check goal -> repeat
    """
    def expand_node(self):
        """
        expand children of current node and add them to fringe
        """
        self.current_node.expand_node()
        children = self.get_current_node_children()
        i = len(children)-1
        while i >=0 :
            self.fringe.append(children[i])
            i-=1 

    def pick_node(self):
        """
        pick a node from fringe
        """

        try: 
            self.current_node = self.fringe.pop()
            self.current_node.mark_active()
            time.sleep(SLEEP_AMOUNT)
            while self.current_node.is_visited():
                
                self.get_wait_flag().wait() # use to pause the thread when the user click on pause button

                self.current_node.mark_already_visited()
                self.current_node = self.fringe.pop()
                self.current_node.mark_active()
                time.sleep(SLEEP_AMOUNT)
        except :
            
            self.current_node = None