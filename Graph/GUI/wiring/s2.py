import sys 
import os 

from settings.settings import *

# Improve: 
dir_icon_0 = os.path.join(BASE_DIR,'gui','icons','S2_1.png')
dir_icon_1 = os.path.join(BASE_DIR,'gui','icons','S2_2.png')
dir_icon_2 = os.path.join(BASE_DIR,'gui','icons','S2_3.png')
dir_icon_3 = os.path.join(BASE_DIR,'gui','icons','S2_4.png')
dir_icon_4 = os.path.join(BASE_DIR,'gui','icons','S2_5.png')
dir_icon_5 = os.path.join(BASE_DIR,'gui','icons','S2_6.png')
dir_icon_6 = os.path.join(BASE_DIR,'gui','icons','S2_7.png')
dir_icon_7 = os.path.join(BASE_DIR,'gui','icons','S2_8.png')

icons = [dir_icon_0, dir_icon_1, dir_icon_2, dir_icon_3, \
         dir_icon_4, dir_icon_5, dir_icon_6, dir_icon_7]
# END Improve

"""
Core Logics
"""
def f2_0(): 
    print(dir_icon_0)
    pass 

def f2_1(): 
    print(dir_icon_1)
    pass 

def f2_2(): 
    print(dir_icon_2)
    pass 

def f2_3(): 
    print(dir_icon_3)
    pass 

def f2_4(): 
    print(dir_icon_4)
    pass 

def f2_5(): 
    print(dir_icon_5)
    pass 

def f2_6(): 
    print(dir_icon_6)
    pass 

def f2_7(): 
    print(dir_icon_7)
    pass 

events = [f2_0, f2_1, f2_2, f2_3, \
          f2_4, f2_5, f2_6, f2_7]

"""
Utils
"""
def get_icons(): 
    return icons 

def get_events(): 
    return events 