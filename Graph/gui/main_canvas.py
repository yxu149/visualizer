import tkinter as tk
from settings.settings import *
from gui.wiring import l0, s0, s1, s2, s3, io
from gui.modules import canvas, columns, cursor, node, panel6, panel8, path, silverscreen, textblock

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

str_i0 = "".join(["Path Found: ", io.get_path() ])
str_i1 = "".join(["Path Cost: ", io.get_cost() ])
str_i2 = "Score: {score}".format(score=io.get_score())
str_i3 = "".join(["First Wrong Node ID: ", io.get_fwni()])

class MainCanvas(tk.Frame): 
    def __init__(self, root, width=200, height=200): 
        #cursor.mouse.set_root(self)
        tk.Frame.__init__(self, root, width=width, height=height) 

        self.__i0 = tk.Label(self, width=w1, height=h3, justify='left', text=str_i0)
        self.__i1 = tk.Label(self, width=w1, height=h3, justify='left', text=str_i1)
        self.__i2 = tk.Label(self, width=w1, height=h3, justify='left', text=str_i2)
        self.__i3 = tk.Label(self, width=w1, height=h3, justify='left', text=str_i3)

        self.__l0 = panel6.Panel(self, events=l0.get_events(), icons=l0.get_icons(), width=w1, height=h2)
        self.__s0 = panel8.Panel(self, events=s0.get_events(), icons=s0.get_icons(), width=w1, height=h1)
        self.__s1 = panel8.Panel(self, events=s1.get_events(), icons=s1.get_icons(), width=w1, height=h1)
        self.__s2 = panel8.Panel(self, events=s2.get_events(), icons=s2.get_icons(), width=w1, height=h1)
        self.__s3 = panel8.Panel(self, events=s3.get_events(), icons=s3.get_icons(), width=w1, height=h1)

        self.__col0 = columns.Col(self, width=w0, height=h0, top=self.__i0, mid=self.__l0, down=self.__s0)
        self.__col1 = columns.Col(self, width=w0, height=h0, top=self.__i1, mid=self.__l0, down=self.__s1) 
        self.__col2 = columns.Col(self, width=w0, height=h0, top=self.__i2, mid=self.__l0, down=self.__s2)
        self.__col3 = columns.Col(self, width=w0, height=h0, top=self.__i3, mid=self.__l0, down=self.__s3)
        
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        # Assemble Parts: 
        # Column 0
        self.__col0.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), stick = "NSEW")
        # Column 1
        self.__col1.grid(row=0, column=1, padx=(0, 5), pady=(0, 5), stick = "NSEW")
        # Column 2
        self.__col2.grid(row=0, column=2, padx=(0, 5), pady=(0, 5), stick = "NSEW")
        # Column 3
        self.__col3.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), stick = "NSEW")
        
if __name__ == "__main__": 
    root = tk.Tk() 
    
    root.mainloop() 