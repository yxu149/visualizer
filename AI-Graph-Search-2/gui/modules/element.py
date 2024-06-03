from abc import abstractmethod 
from settings.settings import *

class Element(): 
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def delete(self):
        pass
    
    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def deselect(self):
        pass

    @abstractmethod
    def bind_event(self,callback):
        pass
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def get_savedata(self):
        pass
