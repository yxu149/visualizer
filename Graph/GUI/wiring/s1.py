import sys 
import os 

from settings.settings import *

# Improve: 
dir_icon_0 = os.path.join(BASE_DIR,'gui','icons','S1_1.png')
dir_icon_1 = os.path.join(BASE_DIR,'gui','icons','S1_2.png')
dir_icon_2 = os.path.join(BASE_DIR,'gui','icons','S1_3.png')
dir_icon_3 = os.path.join(BASE_DIR,'gui','icons','S1_4.png')
dir_icon_4 = os.path.join(BASE_DIR,'gui','icons','S1_5.png')
dir_icon_5 = os.path.join(BASE_DIR,'gui','icons','S1_6.png')
dir_icon_6 = os.path.join(BASE_DIR,'gui','icons','S1_7.png')
dir_icon_7 = os.path.join(BASE_DIR,'gui','icons','S1_8.png')

icons = [dir_icon_0, dir_icon_1, dir_icon_2, dir_icon_3, \
         dir_icon_4, dir_icon_5, dir_icon_6, dir_icon_7]
# END Improve

"""
Core Logics
"""
def upload(): 
    print("[UPLOAD]")
    pass 

def download(): 
    print("[DOWNLOAD]")
    pass 

def clear_graph(): 
    print("[CLEAR GRAPH]")
    pass 

def clear_cursor(): 
    print("[CLEAR CURSOR]")
    pass 

def f4(): 
    print(dir_icon_4)
    pass 

def f5(): 
    print(dir_icon_5)
    pass 

def f6(): 
    print(dir_icon_6)
    pass 

def f7(): 
    print(dir_icon_7)
    pass 

events = [upload, download, clear_graph, clear_cursor, \
          f4, f5, f6, f7]

"""
Utils
"""
def get_icons(): 
    return icons 

def get_events(): 
    return events 