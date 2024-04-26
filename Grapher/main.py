import sys
import tkinter as tk

from settings.settings import *
from gui import main_canvas

sys.path.append(BASE_DIR)

if __name__ == "__main__":
    root = tk.Tk()

    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    w = 1100 if w > 1100 else w
    h = 575 if h > 575 else h
    root.geometry("%dx%d+0+0" % (w, h))

    root.title('Visualizer App')
    canvas = main_canvas.MainCanvas(root, w, h) 
    canvas.grid(row=0, column=0)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    for arg in sys.argv:
        if arg[-5:] == '.gtxt':
            canvas.get_drawing_canvas().load(arg)  

    root.mainloop()