import sys
import os 

from tkinter import Misc
from settings.settings import *

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox

from buttonbar_l import *
from buttonbar_s0 import *
from buttonbar_s1 import *
from buttonbar_s2 import *
from buttonbar_s3 import *

class Col_0(Frame): 
    def __init__(self, root, width=250, height=500): 
        Frame.__init__(self, root, width=width, height=height) 
        self.root = root 
        self.__top = Text()