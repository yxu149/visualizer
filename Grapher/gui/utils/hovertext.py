import tkinter as tk
import tkinter.constants as constants
"""
This file was adapted from  
https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
and modified to fit this program 
"""

class ToolTip(object): 
    def __init__(self, widget): 
        self.widget = widget 
        self.tipwin = None 
        self.id = None 
        self.winx = self.winy = 0
    
    def show_tip(self, text): 
        self.text = text 
        if self.tipwin or not self.text: 
            return 
        x, y, cx, cy = self.widget.bbox("insert")

        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 30

        self.tipwin = tw = tk.Toplevel(self.widget) 
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=constants.LEFT,
                      background="#ffffe0", relief=constants.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
        
    def hide_tip(self): 
        tw = self.tipwin
        self.tipwin = None 
        if tw: 
            tw.destroy() 

def create_tool_tip(widget, text=None): 
    if text is None: 
        return 
    else: 
        tip = ToolTip(widget) 
        def enter(event): 
            tip.show_tip(text) 
        def leave(event): 
            tip.hide_tip()
        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)
