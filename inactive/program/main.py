import sys 
import os
import tkinter as tk
import gui.columns.columns as col

from settings import *

"""
Some basic UI size definitions

* Not to Scale 
Layout: 
| I0 | I1 | I2 | I3 | 
---
| G0 | G1 | G2 | L0 |
---
| S0 | S1 | S2 | S3 |

Sample size: 
(h3) | Canvas | Standard Graph | User Graph     | Algorithm Selection | ( 
---
(h2) |< w1   >|< w1 > (h2)     |< w1 > (h2)     | Media Controls      | h0
---
(h1) | S0     | S1             | S2             | S3                  | )
      < w0                                                           >
w0 = total left to right <>
h0 = total top to buttom ()

"""
w1 = BUTTON_S_WIDTH*4 + BUTTON_S_PADX*5 
h1 = BUTTON_S_HEIGHT*4 + BUTTON_S_PADY*3
h2 = BUTTON_L_HEIGHT*3 + BUTTON_L_PADY*4
h3 = 20
w0 = w1 * 4
h0 = h3 + h2 + h1 
"""
str_i0 = "".join(["Path Found: ", io.get_path() ])
str_i1 = "".join(["Path Cost: ", io.get_cost() ])
str_i2 = "Score: {score}".format(score=io.get_score())
str_i3 = "".join(["First Wrong Node ID: ", io.get_fwni()])
"""

sys.path.append(BASE_DIR)

class RootCanvas(tk.Frame): 
    def __init__(self, root, w, h):
        self.__width = w
        self.__height = h
        self.__root = root
        tk.Frame.__init__(self, root, width=w, height=h)
        
        self.__label_path = tk.Label(self, text="Found path:")
        self.__label_cost = tk.Label(self, text='')

    def __pack(self): 
        """
        Pack on Screen
        """
        
        
if __name__ == "__main__": 
    root = tk.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 1200 if w > 1200 else w
    h = 720 if h > 720 else h
    root.geometry("%dx%d+0+0" % (w, h))

    root.title('AI Graph Search')
    can = RootCanvas(root,10,720)

    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)
    for arg in sys.argv:
        if arg[-5:] == '.gtxt':
          can.get_drawing_canvas().load(arg)  

    root.mainloop()