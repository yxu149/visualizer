import sys 
import os 

from settings.settings import *

# Improve: 
dir_icon_0 = os.path.join(BASE_DIR,'gui','icons','L1.png')
dir_icon_1 = os.path.join(BASE_DIR,'gui','icons','L2.png')
dir_icon_2 = os.path.join(BASE_DIR,'gui','icons','L3.png')
dir_icon_3 = os.path.join(BASE_DIR,'gui','icons','L4.png')
dir_icon_4 = os.path.join(BASE_DIR,'gui','icons','L5.png')
dir_icon_5 = os.path.join(BASE_DIR,'gui','icons','L6.png')

icons = [dir_icon_0, dir_icon_1, dir_icon_2, dir_icon_3, dir_icon_4, dir_icon_5]
# END Improve
"""
Core Logics
"""
def play(): 
    print("[PLAY]")
    pass

def next_step(): 
    print("[NEXT STEP]")
    pass 

def pause(): 
    print("[PAUSE]")
    pass 

def prev_step(): 
    print("[PREV STEP]")
    pass 

def stop(): 
    print("[STOP]")
    pass 

def more(): 
    print("[MORE]")
    pass 

events = [play, next_step, pause, prev_step, stop, more] 

"""
Utils
"""
def get_icons(): 
    return icons 

def get_events(): 
    return events 