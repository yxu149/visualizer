import sys
import os 

from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

class ButtonBar(Frame, ): 
    def __init__(self, root, width=BUTTON_L_WIDTH, height=BUTTON_L_HEIGHT): 
        Frame.__init__(self, root, width=width, height=height)
        self.root = root 