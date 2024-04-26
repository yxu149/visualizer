from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.__str__()

"""
Apparences
"""
"""
Node
"""
NODE_RADIUS = 20
NODE_COLOR = '#FFFFFF'
NODE_OUTLINE_THICKNESS = 2
NODE_OUTLINE_COLOR = '#000000'
NODE_TEXT_COLOR = '#000000'
NODE_TEXT_FONT = ''
"""
Line
"""
LINE_THICKNESS = 2
LINE_COLOR = '#000000'
LINE_TEXT_COLOR = '#000000'
LINE_TEXT_FONT = ''
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
BUTTON_BG = None
"""
Canvas / Backdrop
"""
CANVAS_BG_COLOR = None
CANVAS_PADX = 5
CANVAS_PADY = 5
"""
Pathfinding
"""
NODE_SELECTED = 'orange'
NODE_BEGIN_COLOR = 'red'
NODE_END_COLOR = 'green'
NODE_HERE_COLOR = 'cyan'
NODE_VISITED_COLOR = 'grey'

PATH_LINE_THICKNESS = 2
PATH_LINE_COLOR = None
PATH_NODE_COLOR = 'green'
"""
Texts
"""
TEXT_PADX = 1
TEXT_PADY = 1
"""
Columns
"""
COL_PADX = 0
COL_PADY = 0
COL_BG = None
"""
Panels
"""
PANEL6_BG = None
PANEL8_BG = None