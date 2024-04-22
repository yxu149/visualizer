import sys 
import os 

from settings.settings import *

# Improve: 
dir_icon_0 = os.path.join(BASE_DIR,'gui','icons','S0_1.png')
dir_icon_1 = os.path.join(BASE_DIR,'gui','icons','S0_2.png')
dir_icon_2 = os.path.join(BASE_DIR,'gui','icons','S0_3.png')
dir_icon_3 = os.path.join(BASE_DIR,'gui','icons','S0_4.png')
dir_icon_4 = os.path.join(BASE_DIR,'gui','icons','S0_5.png')
dir_icon_5 = os.path.join(BASE_DIR,'gui','icons','S0_6.png')
dir_icon_6 = os.path.join(BASE_DIR,'gui','icons','S0_7.png')
dir_icon_7 = os.path.join(BASE_DIR,'gui','icons','S0_8.png')

icons = [dir_icon_0, dir_icon_1, dir_icon_2, dir_icon_3, \
         dir_icon_4, dir_icon_5, dir_icon_6, dir_icon_7]
# END Improve

"""
Core Logics
"""
def set_start(): 
    print("[SET START]")
    pass 

def set_end(): 
    print("[SET GOAL]")
    pass 

def set_weight(): 
    print("[SET WEIGHT]")
    pass 

def add_node(): 
    print("[NODE +]")
    pass 

def remove_node(): 
    print("[NODE -]")
    pass 

def add_path(): 
    print("[PATH +]")
    pass 

def remove_path(): 
    print("[PATH -]")
    pass 

def unused(): 
    print("[UNUSED]")
    return 

events = [set_start, set_end, set_weight, unused, \
          add_node, remove_node, add_path, remove_path]

"""
Utils
"""
def get_icons(): 
    return icons 

def get_events(): 
    return events 