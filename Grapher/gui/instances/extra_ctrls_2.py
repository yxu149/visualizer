import sys 
import os 

from settings.settings import *

# Improve: 
dir_icon_0 = os.path.join(BASE_DIR,'gui','icons','S3_1.png')
dir_icon_1 = os.path.join(BASE_DIR,'gui','icons','S3_2.png')
dir_icon_2 = os.path.join(BASE_DIR,'gui','icons','S3_3.png')
dir_icon_3 = os.path.join(BASE_DIR,'gui','icons','S3_4.png')
dir_icon_4 = os.path.join(BASE_DIR,'gui','icons','S3_5.png')
dir_icon_5 = os.path.join(BASE_DIR,'gui','icons','S3_6.png')
dir_icon_6 = os.path.join(BASE_DIR,'gui','icons','S3_7.png')
dir_icon_7 = os.path.join(BASE_DIR,'gui','icons','S3_8.png')

icons = [dir_icon_0, dir_icon_1, dir_icon_2, dir_icon_3, \
         dir_icon_4, dir_icon_5, dir_icon_6, dir_icon_7]
tips = [
    None, 
    None, 
    None, 
    None, 
    None, 
    None, 
    None, 
    None
]
# END Improve

"""
Core Logics
"""
def f3_0(): 
    print(dir_icon_0)
    pass 

def f3_1(): 
    print(dir_icon_1)
    pass 

def f3_2(): 
    print(dir_icon_2)
    pass 

def f3_3(): 
    print(dir_icon_3)
    pass 

def f3_4(): 
    print(dir_icon_4)
    pass 

def f3_5(): 
    print(dir_icon_5)
    pass 

def f3_6(): 
    print(dir_icon_6)
    pass 

def f3_7(): 
    print(dir_icon_7)
    pass 

events = [f3_0, f3_1, f3_2, f3_3, \
          f3_4, f3_5, f3_6, f3_7]

"""
Utils
"""
def get_icons(): 
    return icons 

def get_events(): 
    return events 

def get_tips(): 
    return tips