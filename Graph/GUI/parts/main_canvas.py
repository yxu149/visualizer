import sys
from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

class MainCanvas(Frame): 
    def __init__(self, root, width=200, height=200): 
        self.width = width
        self.height = height
        Frame.__init__(self, root, width=width, height=height)
        # cursor 

