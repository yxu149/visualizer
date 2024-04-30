from pathlib import Path
import math 

BASE_DIR = Path(__file__).resolve().parent.parent.__str__()

"""
Apparences
"""
"""
Node
"""
NODE_RADIUS = 20
NODE_COLOR = 'green'

NODE_ACTIVE_BG = ""
NODE_VISITED_BG = ""
NODE_FRINGE_BG = ""
"""
Line
"""
LINE_COLOR_NORMAL = ""


LINE_GOAL_BG = "purple"
LINE_VISITED_BG = "black"
LINE_GOAL_LABEL_COLOR = "white"

radian45 = 45 * math.pi/180 
LINE_LEN = NODE_RADIUS * math.cos(radian45)
"""
Small Buttons
"""
BUTTON_S_WIDTH = 50 
BUTTON_S_HEIGHT = 50
BUTTON_S_PADX = 5
BUTTON_S_PADY = 5
"""
Large Buttons
"""
BUTTON_L_WIDTH = 100 
BUTTON_L_HEIGHT = 100
BUTTON_L_PADX = 10
BUTTON_L_PADY = 10
"""
All Buttons
"""
BUTTON_BG = "#36393e"
"""
Backdrop / Root Frame 
"""
ROOT_BG = "#1e2124"
"""
Stage / Canvas
"""
STAGE_BG = "black"
"""
Texts
"""
TEXT_PADX = 1
TEXT_PADY = 1
TEXT_FG = "white"
TEXT_BG = "#36393e"
"""
Columns
"""
COL_PADX = 0
COL_PADY = 0
COL_BG = "#282b30"
"""
Panels
"""
PANEL6_BG = "#282b30"
PANEL8_BG = "#282b30"
"""
Shared Common Variables
"""
w1 = BUTTON_S_WIDTH*4 + BUTTON_S_PADX*5
h1 = BUTTON_S_HEIGHT*4 + BUTTON_S_PADY*3
h2 = BUTTON_L_HEIGHT*3 + BUTTON_L_PADY*4
h3 = 20
w0 = w1 * 4
h0 = h3 + h2 + h1