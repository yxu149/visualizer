from .base_class import BaseAlgorithm
import time
import threading
from GUI.settings import SLEEP_AMOUNT

class DepthFirstSearch2(BaseAlgorithm):


    def expand_node(self):

        
        self.current_node.expand_node()
        children = self.current_node.getchildren()
        i = len(children)-1
        while i >=0 :
            self.fringe.append(children[i])
            i-=1 

    def pick_node(self):

        try: 
            self.current_node = self.fringe.pop()
            self.current_node.mark_active()
            time.sleep(SLEEP_AMOUNT)
            while self.current_node.is_visited():
                
                self.get_wait_flag().wait()
                self.current_node.mark_already_visited()
                self.current_node = self.fringe.pop()
                self.current_node.mark_active()
                time.sleep(SLEEP_AMOUNT)
        except :
            
            self.current_node = None