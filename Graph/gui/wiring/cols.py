import tkinter as tk

import gui.modules.columns as columns
import gui.modules.panel6 as panel6
import gui.modules.panel8 as panel8 

import gui.wiring.l0 as l0
import gui.wiring.s0 as s0
import gui.wiring.s1 as s1
import gui.wiring.s2 as s2
import gui.wiring.s3 as s3

import gui.wiring.io as io

from settings.settings import *

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


class Col0(tk.Frame): 
    def __init__(self, root, w=w1, h=h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=COL_BG)
        self.__top = tk.Label(justify="left", text=str_i0)
        self.__mid = panel6.Panel(self, events=l0.get_events(), icons=l0.get_icons())
        self.__down = panel8.Panel(self, events=s0.get_events(), icons=s0.get_icons())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")

class Col1(tk.Frame): 
    def __init__(self, root, w=w1, h=h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=COL_BG)
        self.__top = tk.Label(justify="left", text=str_i1)
        self.__mid = panel6.Panel(self, events=l0.get_events(), icons=l0.get_icons())
        self.__down = panel8.Panel(self, events=s1.get_events(), icons=s1.get_icons())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")

class Col2(tk.Frame): 
    def __init__(self, root, w=w1, h=h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=COL_BG)
        self.__top = tk.Label(justify="left", text=str_i2)
        self.__mid = panel6.Panel(self, events=l0.get_events(), icons=l0.get_icons())
        self.__down = panel8.Panel(self, events=s2.get_events(), icons=s2.get_icons())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")

class Col3(tk.Frame): 
    def __init__(self, root, w=w1, h=h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=COL_BG)
        self.__top = tk.Label(justify="left", text=str_i3)
        self.__mid = panel6.Panel(self, events=l0.get_events(), icons=l0.get_icons())
        self.__down = panel8.Panel(self, events=s3.get_events(), icons=s3.get_icons())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")
