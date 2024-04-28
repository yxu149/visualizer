import tkinter as tk

import gui.modules.panel6 as panel6
import gui.modules.panel8 as panel8 

import gui.instances.media_ctrl as media_ctrl
import gui.instances.penbrush_ctrl as penbrush_ctrl
import gui.instances.io_ctrl as io_ctrl
import gui.instances.extra_ctrls_1 as extra_ctrls_1
import gui.instances.extra_ctrls_2 as extra_ctrls_2

import gui.wirings.io as io

import settings.settings as settings

str_i0 = "".join(["Path Found: ", io.get_path() ])
str_i1 = "".join(["Path Cost: ", io.get_cost() ])
str_i2 = "Score: {score}".format(score=io.get_score())
str_i3 = "".join(["First Wrong Node ID: ", io.get_fwni()])

class Col0(tk.Frame): 
    def __init__(self, root, w=settings.w1, h=settings.h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=settings.COL_BG)
        self.__top = tk.Label(justify="left", text=str_i0, foreground=settings.TEXT_FG, background=settings.TEXT_BG)
        self.__mid = panel6.Panel(self, events=media_ctrl.get_events(), icons=media_ctrl.get_icons(), tips=media_ctrl.get_tips())
        self.__down = panel8.Panel(self, events=penbrush_ctrl.get_events(), icons=penbrush_ctrl.get_icons(), tips=penbrush_ctrl.get_tips())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")

class Col1(tk.Frame): 
    def __init__(self, root, w=settings.w1, h=settings.h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=settings.COL_BG)
        self.__top = tk.Label(justify="left", text=str_i1, foreground=settings.TEXT_FG, background=settings.TEXT_BG)
        self.__mid = panel6.Panel(self, events=media_ctrl.get_events(), icons=media_ctrl.get_icons(), tips=media_ctrl.get_tips())
        self.__down = panel8.Panel(self, events=io_ctrl.get_events(), icons=io_ctrl.get_icons(), tips=io_ctrl.get_tips())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")
    
    def __tool_tips(self): 
        tk.CreateToolTip()

class Col2(tk.Frame): 
    def __init__(self, root, w=settings.w1, h=settings.h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=settings.COL_BG)
        self.__top = tk.Label(justify="left", text=str_i2, foreground=settings.TEXT_FG, background=settings.TEXT_BG)
        self.__mid = panel6.Panel(self, events=media_ctrl.get_events(), icons=media_ctrl.get_icons(), tips=media_ctrl.get_tips())
        self.__down = panel8.Panel(self, events=extra_ctrls_1.get_events(), icons=extra_ctrls_1.get_icons(), tips=extra_ctrls_1.get_tips())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")

class Col3(tk.Frame): 
    def __init__(self, root, w=settings.w1, h=settings.h0): 
        tk.Frame.__init__(self, root, width=w, height=h, bg=settings.COL_BG)
        self.__top = tk.Label(justify="left", text=str_i3, foreground=settings.TEXT_FG, background=settings.TEXT_BG)
        self.__mid = panel6.Panel(self, events=media_ctrl.get_events(), icons=media_ctrl.get_icons(), tips=media_ctrl.get_tips())
        self.__down = panel8.Panel(self, events=extra_ctrls_2.get_events(), icons=extra_ctrls_2.get_icons(), tips=extra_ctrls_2.get_tips())
        self.__pack_on_screen()

    def __pack_on_screen(self): 
        print("packed", self.__top, self.__mid, self.__down)
        self.__top.grid(in_=self, row=0, column=0, padx=0, pady=0, stick="NSEW")
        self.__mid.grid(in_=self, row=1, column=0, padx=0, pady=0, stick="NSEW") 
        self.__down.grid(in_=self, row=2, column=0, padx=0, pady=0, stick="NSEW")
