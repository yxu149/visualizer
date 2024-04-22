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
# END Improve

"""
Core Logics
"""
def f0(): 
    print(dir_icon_0)
    pass 

def f1(): 
    print(dir_icon_1)
    pass 

def f2(): 
    print(dir_icon_2)
    pass 

def f3(): 
    print(dir_icon_3)
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

events = [f0, f1, f2, f3, \
          f4, f5, f6, f7]

"""
Utils
"""
def get_icons(): 
    return icons 

def get_events(): 
    return events 